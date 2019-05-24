#Aguilera Palacios Luis Ernesto
import sys
import os

def main():
	#Validamos que el sistema de archivos sea uno conocido
	file=open("fiunamfs.img","r")
	nom=file.read(8)
	file.seek(2)
	version=file.read(3)
	if nom="FiUnamFS":
		if version="0.4":
			a=True
			file.close()
			while(a):
				print("\t\tVaderFSM\n")
				print("1. Listar contenido.\n")
				print("2. Copiar archivo.\n")
				print("3. Copiar archivo a su computadora.\n")
				print("4. Eliminar archivo. \n")
				print("5. Desfragmentar.\n")
				print("6. Salir.\n")
				print("\t Seleccione un opcion: \n")
				opc=input("->")

				if opc==1:
					print("Listando contenido: \n")
					list()
				elif opc==2:
					print("No implementado")
				elif opc==3:
					print("No implementado")
				elif opc==4:
					print("Dame el nombre del archivo a borrar...")
					print(delete(input("->")))
				elif op==5:
					print("No implementado")
				elif opc==6:
					print("\tDomo Harigato profesor :D \n")
					a=False
			else
				print("Posible incompatibilidad de versiones, abortando...")
				sys.exit()
		else
			print("No conozco el formato del sistema, adios.")
			sys.exit()

def delete(archivo):
	ret=""
	file=open("fiunamfs.img","r+")
	file.seek(1024)
	for i in range(64):
		if file.read(15)==archivo: #Leemos el nombre del archivo
			#Leemos la longitud del archivo
			file.seek(file.tell()+1)
			tam=int(file.read(8))
			#Leemos el inicio de los datos
			file.seek(file.tell()+1)
			ini=int(file.read(5))
			#Borra del directorio y el archivo
			file.seek(file.tell()-30)
			delDir(file)
			file.seek(ini*1024)
			for i in range(tam):
				file.write(' '*1024))
			file.close()
			ret="Archivo borrado."
			return ret
		else:
			file.seek(file.tell()+49)
	file.close()
	ret='Archivo no encontrado.'
	return ret

def pcToSystem(file): #Recibimos el archivo ya abierto listo para ser leído desde nuestra pc
	sys=open("fiunamfs.img","rw")
	sys.seek(1024)
	for i in range(64):
		if sys.read(15)=='AQUI_NO_VA_NADA': #Leemos un espacio vacío
			#Leemos el inicio del espacio
			sys.seek(sys.tell()+10)
			ini=int(sys.read(5))
			sys.write(file.read()) #Copiamos la informacion
			fin=int(sys.tell())
			sys.seek(ini)
			sys.seek(sys.tell()-14)
			sys.write(ini-fin) #guardamos el tamaño del archivo
		else:
			sys.seek(sys.tell()+49)
	sys.close()
	file.close()

def list(): #Método que lista el directorio
	file=open("fiunamfs.img","r")
	file.seek(1024)
	for i in range(64):
		if file.read(15) != 'AQUI_NO_VA_NADA':
			print(archivoAux)
		file.seek(file.tell()+49)
	file.close()

def systemToPC(nombre, ruta): #recibimos el nombre del archivo y la ruta
	sys=open("fiunamfs.img","rw")
	sys.seek(1024)
	for i in range(64):
		if sys.read(15)==nombre: #Leemos un espacio vacío
			#Leemos el inicio del espacio
			sys.seek(sys.tell()+10)
			ini=int(sys.read(5))
			#Crear objeto archivo nuevo en la ruta dada y copiar en él la información
			fin=int(sys.tell())
			sys.seek(ini)
			sys.seek(sys.tell()-14)
			sys.write(ini-fin) #guardamos el tamaño del archivo
		else:
			sys.seek(sys.tell()+49)
	sys.close()
	file.close()

def delDir(file): #Borramos la entrada en el directorio para marcarlo vacío y listo para usarse
	file.write("AQUI_NO_VA_NADA")
	file.seek(file.tell()+1)
	file.write(' '*8)
	file.seek(file.tell()+1)
	file.write(' '*5)
	file.seek(file.tell()+1)
	file.write(' '*14)
	file.seek(file.tell()+1)
	file.write(' '*14)
	file.seek(file.tell()+4)

main()
