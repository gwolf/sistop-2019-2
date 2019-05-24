#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Version de python 3.7
import os
import math
import time
import datetime

class FileSystem:
    file = object()
    ########## (Inicio,Tamanio) ######
    FS_info ={'FiUnamFS':(0,8), '0.4':(10,3)}
    #Diccionario que contiene el nombre del objeto y las direcciones de memoria (Inicio,Offset) que se definieron
    SB ={'Etiqueta':(20,15),'ClusterSize':(40,5),'NumClustersDir':(47,2),'NumClustersU':(52,8)}
    #Diccionario que guarda la informacion de las variables anteriores
    SB_Info = {}
    #File Info
    FileInfo = {'Nombre':(0,15),'Tamanio':(16,8),'ClusterInicial':(25,5),'Hora-Fecha-Creacion':(31,14),'Hora-Fecha-Mod':(46,14)}
    ClusterSizeP = 1024
    Files = []
    KEY_N = 'AQUI_NO_VA_NADA'
    FileInfoSizeDir = 64
    Inicio_MD={}

    def __init__(self,pathFile):
        self.file = open(pathFile,'r+b')
        self.valida_FS()
        self.getDataSB()
        self.Files = []
        self.getFilesInfo()
        return
    # Valida Si el nombre y la version son correctos
    def valida_FS(self):

        for key in self.FS_info:
            value = self.FS_info[key]
            self.file.seek(value[0])
            data = self.file.read(value[1]).decode()
            print(data)
            if  not data in list(self.FS_info.keys()):
                raise Exception ('Sistema de archivos no soportado')
        return
    #Obtiene los datos del primer cluster
    def getDataSB(self):
        for key in self.SB:
            value = self.SB[key]
            self.file.seek(value[0])
            data = self.file.read(value[1]).decode()
            self.SB_Info[key] = data
            #print(self.SB_Info)
        return
    #Obtiene los metadatos iniciando desde que termina el cluster 0 hasta el numero de clusters del directorio
    def getFilesInfo(self):
        self.Inicio_MD={}
        NumClustersDir = 4
        offset = self.ClusterSizeP
        while offset != ( NumClustersDir + 1) *  self.ClusterSizeP:
            self.file.seek(offset)
            data = self.file.read(self.FileInfoSizeDir).decode()
            if not self.KEY_N in data:
                values = self.FileInfo['Nombre']
                nombre = data[ values[0] :  values[1] ].strip()
                self.Inicio_MD[nombre] = offset
                self.dataToFile(data)
                self.Files.append( self.dataToFile(data) )
            offset += self.FileInfoSizeDir
        return
    #Convierte los metadatos en un objeto tipo File para una manipulacion mas facil
    #Contiene todos los atributos como nombre, numero de bytes etc.
    def dataToFile(self,data):
        ListAtrb = []
        for key in self.FileInfo:
            value = self.FileInfo[key]
            ini = value[0]
            off = value[1]
            ListAtrb.append(data[ini:ini+off])
            #print(ListAtrb)
        return File(ListAtrb[0], int(ListAtrb[1]), int(ListAtrb[2]), ListAtrb[3], ListAtrb[4])
    #Realiza el listado de todos los archivos
    def ls(self):
        self.Files = []
        self.getFilesInfo()
        print('Listado de Archivos:')
        for file in self.Files:
            print(file)
        return
    #Realiza la copia de un archivo del FS a la computadora del usuario
    def copytoUser(self,nombre_archivo,ruta):
        nombres = self.getNamesFiles()
        if not nombre_archivo in nombres:
            print('Nombre de archivo inexistente')
            return
        i = nombres.index(nombre_archivo)
        archivo = self.Files[i]
        print('Copiando ...')
        print(archivo)
        offset = archivo.getCluster() * self.ClusterSizeP
        self.file.seek(offset)
        data = self.file.read(archivo.getSize())
        ruta = os.path.join(ruta,nombre_archivo)
        nuevo = open(ruta,'wb')
        nuevo.write(data)
        nuevo.close()
        print('Listo!!!!!')
        return
    #Obtiene los nombres de los archivos existentes en el FS
    def getNamesFiles(self):
        Nombres = []
        for file in self.Files:
            Nombres.append(file.getName().strip())
        return Nombres
    #Copia un archivo del usuario al FS
    def copyToFS(self,path):
        sizeFreeClusters,Cluster_ini = self.AvailableSpace()
        sizeFile = os.path.getsize(path)
        num_Clusters = math.ceil(sizeFile/ self.ClusterSizeP)
        if num_Clusters > sizeFreeClusters:
            print('El archivo es demasiado grande')
            return
        nombre = os.path.basename(path)
        if len(nombre)>15:
            print('El nombre del archvio es muy grande :( ')
            return
        #Comienza a escribir el archivo
        user_file = open(path,'rb')
        #Aqui se podria hacer con un buffer pero solo en caso de que sean archivos mas grandes, por simplicidad se lee todo xD
        data = user_file.read(sizeFile)
        offset = Cluster_ini * self.ClusterSizeP
        self.file.seek(offset)
        self.file.write(data)
        #Buscamos en el directorio para agregar el archivo
        #Creamos las fechas de modificacion y creacion en el formato especificado
        t = datetime.datetime.strptime(time.ctime(os.path.getctime(path)),"%a %b %d %H:%M:%S %Y")
        fecha_creacion = str(t.year)+str(t.month).zfill(2) + str(t.hour).zfill(2)+ str(t.minute).zfill(2) + str(t.second).zfill(2)
        fm = datetime.datetime.now()
        fecha_modificacion = str(fm.year)+str(fm.month).zfill(2) + str(fm.hour).zfill(2)+ str(fm.minute).zfill(2) + str(fm.second).zfill(2)
        self.agregaMD(nombre,sizeFile,Cluster_ini,fecha_creacion,fecha_modificacion)
        return

    #Escribe los metadatos en el primer lugar que encuentra con la palabra "Aqui no hay nada"
    def agregaMD(self,nombre,sizeFile,Cluster_ini,fecha_creacion,fecha_modificacion):
        NumClustersDir = 4
        offset = self.ClusterSizeP
        while offset != ( NumClustersDir + 1) *  self.ClusterSizeP:
            self.file.seek(offset)
            data = self.file.read(self.FileInfoSizeDir).decode()
            if self.KEY_N in data:
                #Añade la entrada
                ListAtrb = [str(nombre),str(sizeFile),str(Cluster_ini),str(fecha_creacion),fecha_modificacion]
                self.dataToMD(ListAtrb,offset)
                return
            offset += self.FileInfoSizeDir
        return

    #Cuando encuentra el espacio ahi guarda los datos
    def dataToMD(self,Atrb,inicio):
        i = 0
        for key in self.FileInfo:
            value = self.FileInfo[key]
            ini = value [0]
            tam = value [1]
            self.file.seek(inicio+ini)
            dato = Atrb[i].rjust(tam)
            self.file.write(dato.encode('ascii'))
            i+=1
        return

    #Determina el espacio disponible en el FS
    def AvailableSpace(self):
        Clusters = []
        Size =[]
        for file in self.Files:
            Clusters.append( file.getCluster() )
            Size.append( file.getSize())
        max_cluster = max(Clusters)
        i = Clusters.index(max_cluster)
        Cluster_ini = max_cluster + math.ceil(Size[i]/ self.ClusterSizeP)
        disponible = int(self.SB_Info['NumClustersU'])-Cluster_ini
        return disponible,Cluster_ini

    #Funcion que elimina un archivo (como vimos en clase, solo elimina la parte de los metadatos)
    def remove(self,nombre_archivo):
        print(self.Inicio_MD)
        if not nombre_archivo in list(self.Inicio_MD.keys()):
            print ("El archivo a eliminar no existe")
            return
        zeros = self.KEY_N + '0'*(self.FileInfoSizeDir- len(self.KEY_N))
        zeros = zeros.encode('ascii')
        offset = self.Inicio_MD[nombre_archivo]
        self.file.seek(offset)
        self.file.write(zeros)
        return

    #Para la desfragmentacion lo que se hace es acomodar todos los archivos existentes
    #de manera contigua para asi al escribir un archivo en el fs se escriba al final
    def desfragmentacion(self):
        self.ls()
        Clusters =[]
        cluster_ini = 5
        tam = 0
        for archivo in self.Files:
            cluster_ini = cluster_ini + math.ceil(tam/self.ClusterSizeP)
            Clusters.append(cluster_ini)
            tam = archivo.getSize()
            data = self.getDataFromFileName(archivo.getName().strip())
            offset = cluster_ini * self.ClusterSizeP
            # busca y escribe los datos en los nuevos clusters
            self.file.seek(offset)
            self.file.write(data)
            #se actualiza en los metadatos
            self.setAtrb_MD(archivo.getName().strip(),'ClusterInicial',cluster_ini)
        return
    #Retorna los datos (bytes) de un archivo dado su nombre
    def getDataFromFileName(self,nombre_archivo):
        nombres = self.getNamesFiles()
        i = nombres.index(nombre_archivo)
        archivo = self.Files[i]
        offset = archivo.getCluster() * self.ClusterSizeP
        self.file.seek(offset)
        data = self.file.read(archivo.getSize())
        return data
    #sobreescribe un atributo dado en los metadatos
    def setAtrb_MD(self,nombre,atrb,valor):
        values = self.FileInfo[atrb]
        offset = self.Inicio_MD[nombre]
        self.file.seek(offset+values[0])
        self.file.write(str(valor).rjust(values[1]).encode('ascii'))
        return

class File:
    nombre =''
    tamanio_bytes = 0
    cluster_inicial = -1
    hora_fecha_creacion = ''
    hora_fecha_modficacion = ''
    def __init__(self,nombre,tam,cluster,crea,mod):
        self.nombre = nombre
        self.tamanio_bytes = tam
        self.cluster_inicial = cluster
        self.hora_fecha_creacion = crea
        self.hora_fecha_modficacion = mod
        return
    def getName(self):
        return self.nombre
    def getCluster(self):
        return self.cluster_inicial
    def getSize(self):
        return self.tamanio_bytes
    def __str__(self):
        return str(self.nombre)
