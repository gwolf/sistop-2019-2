import os
import math
import time
import datetime

directorio = 'FiUnamFS.img'
tamano_dato = 64
info = []
tamano = []
ubicacion = []
opc = 0

def obtenerarchivos():
    
    sistema = open(directorio,'r')
    posicion = 1024
    while posicion < 5120:
        sistema.seek(posicion)
        query = sistema.read(15)
        
        if query != 'AQUI_NO_VA_NADA':
            info.append(query.replace(" ", ""))
            sistema.seek(posicion+16)
            tamano.append(int(sistema.read(8)))
            sistema.seek(posicion+25)
            ubicacion.append(int(sistema.read(5)))
        posicion = posicion + 64

    posicion = 5120
    sistema.close()


def obtenerinfo():
    global aux1
    sistema = open(directorio,'r')
    
    posicion = 0
    sistema.seek(posicion)
    query = sistema.read(8)
    info.append(query)

    posicion = 10
    sistema.seek(posicion)
    query = sistema.read(3)
    info.append(query)

    posicion = 20
    sistema.seek(posicion)
    query = sistema.read(15)
    info.append(query)

    posicion = 40
    sistema.seek(posicion)
    query = sistema.read(5)
    info.append(query)

    posicion = 47
    sistema.seek(posicion)
    query = sistema.read(2)
    info.append(query)

    posicion = 52
    sistema.seek(posicion)
    query = sistema.read(8)
    info.append(query)

    sistema.close()

def copiarpc(archivo):
    sistema = open(directorio, 'r+b')
    posicion_archivo = info.index(archivo)
    tamano_archivo = tamano[posicion_archivo]
    ubicacion_archivo = ubicacion[posicion_archivo]*1024
    sistema.seek(ubicacion_archivo)

    copia_archivo = open(archivo,'wb')
    copia.write(sistema.read(tamano_archivo))
    sistema.close()

def eliminar(archivo): 
    sistema = open(directorio,'r+')
    posicion = 1024
    sistema.seek(posicion)
    while posicion < 5120:
        nombre_archivo = sistema.read(15)
        archivo_act = nombre_archivo.strip()
        
        if archivo_act == archivo:
            sistema.seek(posicion)
            sistema.write("AQUI_NO_VA_NADA")
            sistema.wirte('0'*49)
        
            for i in range(len(archivos)):
                info.pop(0)
                tamano.pop(0)
                ubicacion.pop(0)
            obtenerarchivos()
        else:
            posicion = posicion + 64
            sistema.seek(posicion)
    sistema.close
    print "Se elimino el archivo"

def copiardepc(path):
    sistema = open(directorio,'r+b')
    tamano_archivo = os.path.getsize(path)
    cluster = math.datetime.strptime(time.ctime(os.path.getctime(path)), "%a %b %d %H:%M:S %Y")
    creacion = str(t.year)+str(t.month).zfill(2) + str(t.hour).zfill(2) + str(t.minute).zfill(2) + str(t.second).zfill(2)
    aux = ubicacion.index(max(ubicacion))
    dir_cluster = (ubicacion[aux] + math.ceil(tamano[aux]/1024))*1024
    dir_archivo = open(path,'rb')
    info_archivo = dir_archivo.read(tamano_archivo)
    sistema.seek(dir_cluster)
    sistema.write(info_archivo)

    nombre_archivo = path.rjust(15)
    posicion = 1024

    while posicion < 5120:
        sistema.seek(posicion)
        query = sistema.read(15)
        
        if query == 'AQUI_NO_VA_NADA':
            sistema.seek(posicion)
            sistema.write(nombre_archivo.encode('ascii'))
            sistema.seek(posicion+16)
            sistema.write(str(tamano_archivo).encode('ascii'))
            sistema.seek(posicion+25)
            sistema.write(str(dir_cluster).encode('ascii'))
            sistema.seek(posicion+46)
            sistema.write(creacion.encode('ascii'))
            sistema.close()
            dir_archivo.close
            return 
        posicion = posicion + 64
    posicion = 5120
      

sistema = open(directorio,'r')
posicion = 0
sistema.seek(posicion)
query = sistema.read(8)
if (query == 'FiUnamFS'):
    obtenerarchivos()
    while (opc != 6):
        print "Ingresa:"
        print "1 Para obtener la informacion del sistema"
        print "2 Para listar archivos"
        print "3 Copiar un archivo a la PC"
        print "4 Copiar un archivo desde la PC"
        print "5 Eliminar un archivo"
        print "6 Para salir.."
        opc = input("Opcion:")
        if opc == 1:
            print "Informacion del sistema"
            obtenerinfo()
            print "Nombre: " + info[0]
            print("Version: "+info[1])
            print("Etiqueta Volumen: "+info[2])         
            print("Tamano Cluster: "+info[3])   
            print("Num. Cluster (Directorio): "+info[4])
            print("Num. Cluster Total: "+info[5])
        if opc == 2:
            for info in info:
                print info
        if opc == 3:
            nombre_archivo = raw_input("Ingresa el nombre archivo sin extension: ")
            copiarpc(nombre_archivo)
        if opc == 4:
            nombre_archivo = raw_input("Ingresa el nombre del archivo sin extension: ")
            copiardepc(nombre_archivo)
        if opc == 5:
            archivo = raw_input("Ingresa el nombre del archivo a eliminar: ")
            eliminar(archivo)
        if opc == 6:
            print "bye"
