import os.path
import sys
from datetime import time,datetime
from math import ceil, log10
import time

##Funciones
#Funcion para evitar que cambien el nombre del sistema en el archivo
def ComprobNombre():
	file=open("fiunam.img","r")	
	aux=file.read(8)
	if aux!="FiUnamFS":
		print("El nombre del sistema de archivos ha sido cambiado. No es posible trabajar")
		sys.exit()
	file.close()

#Funcion que regresa el formato requerido para guardar las fechas
def tiempo(fecha):
	fecha=time.strptime(fecha)
	fecha=time.strftime("%Y%m%d%H%M%S",fecha)
	return(fecha)

#Funcion para aniadir archivo de la computadora al sistema de archivos
def aniadir(nombre):
	size=os.path.getsize(nombre)
	fechaMod=time.ctime(os.path.getmtime(nombre))
	fechaCre=time.ctime(os.path.getctime(nombre))
	contador=0
	cluster_ant=0
	tamanio=0
	cluster=ceil(size/1024)
	file=open("fiunam.img","r+")
	file.seek(0,os.SEEK_SET)
	file.seek(1024)
	aux=file.read(15)
	while aux != 'AQUI_NO_VA_NADA':
		file.seek(file.tell()+49)
		aux=file.read(15)
	#Si es el primer archivo en directorio
	if file.tell()==1039:
		cluster_act=4
		print("Es el primer archivo")
		ahora=file.tell()
	else:
		ahora=file.tell()
		anterior=file.seek(file.tell()-63)
		tamanio=file.read(8)
		file.seek(file.tell()+1)
		cluster_ant=file.read(5)
		cluster_act=ceil(int(tamanio)/1024)+int(cluster_ant)-1
		file.seek(file.tell()+49)
	if (1440-(cluster_act+cluster))>0:
		temp=15-len(nombre)
		if(temp>0):
			file.seek(file.tell()-15)
			for i in range(temp):
				file.write(" ")
			file.write(nombre)			
		else:
			return ("El archivo tiene un nombre demasiado grande")
		#Escribimos tamanio archivo nuevo
		file.seek(file.tell()+1)
		temp=8-len(str(size))
		for i in range(temp):
			file.write("0")
		file.write(str(size))
		#Escribimos cluster inicial
		file.seek(file.tell()+1)
		temp=5-len(str(cluster_act+cluster))
		for i in range(temp):
			file.write("0")
		file.write(str(cluster_act+cluster))
		#Escribimos fecha de creacion archivo
		file.seek(file.tell()+1)
		temp=tiempo(fechaCre)
		file.write(temp)
		#Escribimos fecha de modificacion de archivo
		file.seek(file.tell()+1)
		temp=tiempo(fechaMod)
		file.write(temp)
		
		#Agregamos contenido de archivo
		archivo=open(nombre,"r",encoding="Latin-1")
		file.seek((cluster_act+cluster)*1024)
		file.write(archivo.read())
		archivo.close()
		file.close()
		return("Se ha añadido exitosamente")
	else:
		file.close()
		return("El tamanio de tu archivo es demasiado grande")
	
#Funcion que copia archivo del sistema a la computadora
def copiar(nombre):
	size=0
	cluster=0
	name=nombre
	copia=""
	while name==nombre:
		print("Introduce el nombre del nuevo archivo")
		name=input()
	file=open("fiunam.img","r+",encoding="Latin-1")
	file.seek(1024)
	aux=file.read(15)
	while aux.replace(" ","")!=nombre:
		file.seek(file.tell()+49)
		aux=file.read(15)
	file.seek(file.tell()+1)
	size=int(file.read(8))
	file.seek(file.tell()+1)
	cluster=int(file.read(5))	
	file.seek(cluster*1024)
	copia=file.read(size)
	archivo=open(""+name,"w",encoding="Latin-1")
	archivo.write(copia)
	archivo.close()
	file.close()
	return("Archivo copiado con exito")

#Muestra el contenido del FS
def listar():
	file=open("fiUnam.img","r")
	file.seek(1024)
	for i in range(64):
		archivoAux=file.read(15)
		if archivoAux != 'AQUI_NO_VA_NADA':
			print(archivoAux.replace(' ',''))
		file.seek(file.tell()+49)
	file.close()

#Esta funcion elimina del sistema de archivos
def eliminar(nombre):#Recibe el nombre del archivo a eliminar
	file=open("fiUnam.img","r+")
	file.seek(1024)
	for i in range(64):
		archivoAux=file.read(15)
		if archivoAux.replace(' ','') == nombre:
			#Recupera informacion necesaria del archivo a eliminar
			file.seek(file.tell()+1)
			tam=int(file.read(8))
			file.seek(file.tell()+1)
			ini=int(file.read(5))
			#Borra del directorio
			file.seek(file.tell()-30)
			file.write("AQUI_NO_VA_NADA")
			file.seek(file.tell()+1)
			file.write("00000000")
			file.seek(file.tell()+1)
			file.write("00000")
			file.seek(file.tell()+1)
			file.write("00000000000000")
			file.seek(file.tell()+1)
			file.write("00000000000000")
			file.seek(file.tell()+4)
			file.close()
			#Limpia la memoria
			limpiar(ini,ceil(tam/1024))#El tamaño se envia en clusters
			return 'Se borro el archivo'
		else:
			file.seek(file.tell()+49)
	file.close()
	return 'No se encontro el archivo'

#Esta funcion limpia la memoria desde un cluster inicial(ini), el tamaño(tam) esta dado clusters
def limpiar(ini,tam):
	file=open("fiUnam.img","r+")
	file.seek(ini*1024)
	vacio='\x00'
	for i in range(0,tam):
		file.write(vacio*1024)
	file.close()

#Esta funcion desfragmenta el sistema de archivos
def desFragmentar():
	archivos=[]#[archivo1, archivo2, ...]
	archivo=[]#[ini,tam] #tamaño dado en clusters
	countAux=5#inicia en 5 porque esos son los clusters ya utilizados en el FS
	countAux2=0
	datosDic=[]
	file=open("fiUnam.img","r+",encoding="Latin-1")
	file.seek(1024)
	for i in range(64):
		archivoNombre=file.read(15)
		if archivoNombre != 'AQUI_NO_VA_NADA':
			#Recupera informacion importante de los archivos
			file.seek(file.tell()+1)
			tam=int(file.read(8))
			file.seek(file.tell()+1)
			ini=int(file.read(5))
			file.seek(file.tell()-30)
			datosDic.append(file.read(64))
			archivo.append(ini)
			archivo.append(ceil(tam/1024))
			archivos.append(archivo)
			archivo=[]
		else:
			file.seek(file.tell()+49)
	for archivoAux in archivos:
		#Recupera el archivo en copiador
		file.seek(archivoAux[0]*1024)
		copiador=file.read(archivoAux[1]*1024)
		#limpia la memoria
		eliminar(datosDic[countAux2][0:15].replace(' ',''))
		#Coloca el archivo en el primer espacio libre
		file.seek(countAux*1024)
		file.write(copiador)
		#Actualiza el diccionario
		file.seek(1024+(countAux2*64))
		file.write(datosDic[countAux2])
		file.seek(file.tell()-39)
		file.write(('0'*(5-ceil(log10(countAux+1))))+str(countAux))
		#Actualiza el contador de clusters ocupados
		countAux+=archivoAux[1]
		#Actualiza el contador de archivos movidos
		countAux2+=1
	file.close()

#Esta funcion recibe los argumentos e invoca a las funciones requeridas
def opciones(Argumentos):
	opc='Para la correcta ejecucion de las opciones es necesario indicar una de las siguientes opciones:'
	opc+='\nlistar\t\tMuestra el contenido del sistema de archivos\n\n'
	opc+='eliminar\tElimina un archivo del sistema de archivos\n\t\tEliminar requiere proporcionar el nombre del archivo a borrar\n\n'
	opc+='copiar\t\tCopia un archivo del sistema de archivos al directorio actual\n\t\t(En el que se encuentran el archivo y el FS)\n\n'
	opc+='aniadir\t\tCopia un archivo de la carpeta actual al sistema de archivos\n\t\t(En el que se encuentran el archivo y el FS)\n\n'
	opc+='eg: "python Manejador.py listar"'

	if len(Argumentos) == 1 or len(Argumentos)>3:
		print(opc)
	else:
		if Argumentos[1] == 'listar':
			listar()
		elif Argumentos[1] == 'eliminar':
			eliminar(Argumentos[2])
		elif Argumentos[1] == 'copiar':
			copiar(Argumentos[2])
		elif Argumentos[1] == 'aniadir':
			aniadir(Argumentos[2])
		else:
			print(opc)


#Cuerpo del programa
if os.path.exists("fiunam.img"):
	pass
	
else:
	print("Creamos Sistema de Archivos")
	file=open("fiunam.img","w")
	file.write("FiUnamFS")
	file.seek(10)
	file.write("0.4")
	file.seek(20)
	file.write("Sistema Archivo")
	file.seek(40)
	file.write("01024")
	file.seek(47)
	file.write("04")
	file.seek(52)
	file.write("00001440")
	file.seek(1024)
	for i in range(64):
		file.write("AQUI_NO_VA_NADA")
		file.seek(file.tell()+1)
		file.write("00000000")
		file.seek(file.tell()+1)
		file.write("00000")
		file.seek(file.tell()+1)
		file.write("00000000000000")
		file.seek(file.tell()+1)
		file.write("00000000000000")
		file.seek(file.tell()+4)
	file.close()

ComprobNombre()
desFragmentar()
opciones(sys.argv)