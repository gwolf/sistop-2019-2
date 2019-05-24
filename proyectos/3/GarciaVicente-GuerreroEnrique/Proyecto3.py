import os
import math
import time
import datetime

#declaramos las variables a utilizar
archivos = []
tamano = []
localizacion = []
info=[]
version=[]
archivo_copia=[]
list_destino=[]
list_origen=[]

#Abro y recorro el arhivo obteniendo listas de los nombres, tamanos y cluster inicial de cada archivo
def obtener_archivos():

	sistema_de_archivos = open('fiunamfs.img','r')
	posicion_actual = 1024
	while posicion_actual < 5120:
		sistema_de_archivos.seek(posicion_actual)
		query = sistema_de_archivos.read(15)
		#print(query)
		if query != 'AQUI_NO_VA_NADA':
			archivos.append(query.replace(" ",""))
			sistema_de_archivos.seek(posicion_actual+16)
			tamano.append(int(sistema_de_archivos.read(8)))
			sistema_de_archivos.seek(posicion_actual+25)
			localizacion.append(int(sistema_de_archivos.read(5)))
		posicion_actual += 64
	posicion_actual = 5120
	sistema_de_archivos.close()


#Aqui se obtine y guarda la informacion del sistema para luego ser mostrada
def obt_info():
	sistema_de_archivos = open('fiunamfs.img','r')
	posicion_actual = 0
	sistema_de_archivos.seek(posicion_actual)
	query = sistema_de_archivos.read(8)
	info.append(query)
	#####################
	posicion_actual = 10
	sistema_de_archivos.seek(posicion_actual)
	query = sistema_de_archivos.read(3)
	info.append(query)
	######################
	posicion_actual = 20
	sistema_de_archivos.seek(posicion_actual)
	query = sistema_de_archivos.read(15)
	info.append(query)
	########################
	posicion_actual = 40
	sistema_de_archivos.seek(posicion_actual)
	query = sistema_de_archivos.read(5)
	info.append(query)
	########################
	posicion_actual = 47
	sistema_de_archivos.seek(posicion_actual)
	query = sistema_de_archivos.read(2)
	info.append(query)
	########################
	posicion_actual = 52
	sistema_de_archivos.seek(posicion_actual)
	query = sistema_de_archivos.read(8)
	info.append(query)
	########################
	sistema_de_archivos.close()


#Aqui se copiara el archivo del sistema al CP
def copiar_un_archivo_a_mi_PC(archivo):
	###Obtencion
	sistema_de_archivos = open('fiunamfs.img', 'r+b')
	posicion_arch = archivos.index(archivo) #obtengo la posicion donde se encuentra en la lista archivos
	tamano_archivo_a_copiar = tamano[posicion_arch] #obtengo el tamano del archivo
	ubicacion = localizacion[posicion_arch]*1024
	sistema_de_archivos.seek(ubicacion) #me muevo a la ubicacion del archivo

	longi = len(archivo)
	#Copiado a mi PC
	#print("No se como copiar una imagen")
	copia = open(archivo,'wb') #se le asigna el mismo nombre que el original
	copia.write(sistema_de_archivos.read(tamano_archivo_a_copiar)) #escribo el archivo
	copia.close()
	sistema_de_archivos.close()
	print("\nArchivo copiado con exito\n")


def eliminar_archivo(archivo_a_eliminar):
	with open('fiunamfs.img','r+') as sistema_de_archivos:
		posicion_actual = 1024
		sistema_de_archivos.seek(posicion_actual)
		# mientras la posicion este dentro del directorio puedo buscar el archivo
		while posicion_actual < 5120:
			# vamos a leer el nombre de los archivos en el directorio
			nombre_arch = sistema_de_archivos.read(15)
			nombre_arch_stp = nombre_arch.strip()
			# compruebo que el nombre del archivo a eliminar exista en directorio en la posicion actual en fiunamfs.img
			if (nombre_arch_stp == archivo_a_eliminar):
				# si se encuentra, se eliminan metadatos del archivo
				sistema_de_archivos.seek(posicion_actual)
				sistema_de_archivos.write("AQUI_NO_VA_NADA")
				sistema_de_archivos.write('0'*49)
				print(" Archivo eliminado.\n")
				x = len(archivos)
				# actualizacion de las listas de informacion de los archivos
				for i in range(x):
					archivos.pop(0)
					tamano.pop(0)
					localizacion.pop(0)
				obtener_archivos()
				break
			else:
				# no se encuentra el archivo: se recorre nuestro puntero para encontrarlo
				posicion_actual += 64
				sistema_de_archivos.seek(posicion_actual)
				# si acabamos de recorrer el directorio y no se encuentra el archivo, no existe
				if(posicion_actual==5120):
					print(" El archivo no existe.")

#solo se puede copiar archvios que esten en la misma direccion que el programa
def copiar_desde_CP(path):
	sistema_de_archivos = open('fiunamfs.img', 'r+b') #Abro el archivo
	peso = os.path.getsize(path) #obtengo el tamano del archivo a copiar
	clusters =  math.ceil(peso/ 1024.00) #calculo cuantos cluster se van a utilizar
	t = datetime.datetime.strptime(time.ctime(os.path.getctime(path)),"%a %b %d %H:%M:%S %Y")
	fecha_creacion = str(t.year)+str(t.month).zfill(2) + str(t.hour).zfill(2)+ str(t.minute).zfill(2) + str(t.second).zfill(2) #obtengo fecha de creacion
	fm = datetime.datetime.now()
	fecha_modificacion = str(fm.year)+str(fm.month).zfill(2) + str(fm.hour).zfill(2)+ str(fm.minute).zfill(2) + str(fm.second).zfill(2) #obtengo fecha de modificacion
	x =localizacion.index(max(localizacion)) #obtengo el indice de la maxima cantidad de cluster
	clu = localizacion[x] #obtengo el cluster origen
	ta_clu = math.ceil(tamano[x]/1024.00) #obtener el tamano que ocupa en cluster el archivo
	total = (clu + ta_clu)*1024 #calculo la direccion del cluster
	archivopath = open(path,'rb') #abro el archivo a copiar
	datos = archivopath.read(peso) #leo y guardo los datos
	sistema_de_archivos.seek(total) # me muevo a la direccion del cluster
	sistema_de_archivos.write(datos) #escribo los datos
	sistema_de_archivos.close()

	name = path.rjust(15) #obtengo el nombre del archivo agregando espacios

	sistema_de_archivos = open('fiunamfs.img','r+b')
	posicion_actual = 1024

	while posicion_actual < 5120:
		sistema_de_archivos.seek(posicion_actual)
		query = sistema_de_archivos.read(15)
		if query == 'AQUI_NO_VA_NADA':
			#guardo la informacion correspondiente del archivo en su lugar indicado
			sistema_de_archivos.seek(posicion_actual+0)
			sistema_de_archivos.write(name.encode('ascii'))
			sistema_de_archivos.seek(posicion_actual+16)
			sistema_de_archivos.write(str(peso).encode('ascii'))
			sistema_de_archivos.seek(posicion_actual+25)
			sistema_de_archivos.write(str(total).encode('ascii'))
			sistema_de_archivos.seek(posicion_actual+31)
			sistema_de_archivos.write(fecha_modificacion.encode('ascii'))
			sistema_de_archivos.seek(posicion_actual+46)
			sistema_de_archivos.write(fecha_creacion.encode('ascii'))
			sistema_de_archivos.close()
			archivopath.close()
			print("Archivo Copiado a FiUnamFS")
			return
		posicion_actual += 64
	posicion_actual = 5120


def desframentacion():
	print("Lo siento no logramos este punto :(")


def main():
	#Abrimos el archivo y leemos donde se encuentra el nombre del sistema
	valida=[]
	sistema_de_archivos = open('fiunamfs.img','r')
	posicion_actual = 0
	sistema_de_archivos.seek(posicion_actual)
	query = sistema_de_archivos.read(8)
	valida.append(query)
	print(valida[0])
	#Aqui se verifica que el sistema tenga el nombre de FiUnamFS
	if (valida[0] == 'FiUnamFS'): 
		sistema_de_archivos = open('fiunamfs.img', 'r+')
		sistema_de_archivos.close()
		obtener_archivos()
		
		while(True):
			#Iniciamos el menu con las opciones a realizar
			print("\n\n-----------Menu-----------------")
			print("\nOpciones:\n0. Informacion del sistema\n1. Listar archivos\n2. Copiar un archivo a mi PC\n3. Copiar un archivo desde mi PC\n4. Eliminar un archivo\n5. Desfragmentar\n6. Salir")
			opcionMenu = input("Inserta una opcion >> ")
			#Se obtine la informacion del sistema
			if(opcionMenu==0):
				os.system('clear')
				obt_info()
				print("\n\n------------Informacion---------------\n")
				print("Nombre: "+info[0])
				print("Version: "+info[1])
				print("Etiqueta Volumen: "+info[2])
				print("Tamano Cluster: "+info[3])
				print("Num. Cluster (Directorio): "+info[4])
				print("Num. Cluster Total: "+info[5])
			elif(opcionMenu==1):
				os.system('clear')
				print("\n\n------------Archivos-----------------\n")
				x = len(archivos)
				for i in range(x):
					archivos.pop(0)
					tamano.pop(0)
					localizacion.pop(0)
				obtener_archivos()
				for i in range(len(archivos)):
					print(archivos[i])
				x = len(archivos)
				for i in range(x):
					archivos.pop(0)
					tamano.pop(0)
					localizacion.pop(0)
				obtener_archivos()
			elif(opcionMenu==2):
				os.system('clear')
				print("\n\n------------Copiar archivo a mi PC-----------\n")
				nombreArchivo = raw_input("Ingresa el nomnbre del archivo >> ")
				copiar_un_archivo_a_mi_PC((nombreArchivo))
			elif(opcionMenu==3):
				os.system('clear')
				print("\n\n------------Copiar archivo desde mi PC-----------\n")
				nombreArchivo = raw_input("Ingresa el nomnbre del archivo >> ")
				copiar_desde_CP((nombreArchivo))
			elif(opcionMenu==4):
				os.system('clear')
				print("\n\n--------------Eliminar un archivo-------------\n")
				archivo_a_eliminar = raw_input("\nArchivo a eliminar >> ")
				eliminar_archivo(archivo_a_eliminar)
			elif(opcionMenu==5):
				os.system('clear')
				print("\n\n--------------Desgragmentador------------\n")
				desframentacion()
			elif(opcionMenu==6):
				os.system('clear')
				print("\n\n------------Adios-----------------\n")
				print("Gracias por usar nuestro sistema")
				break
				
	else:
		print("No es el archivo de Wolf.....BYE")

main()