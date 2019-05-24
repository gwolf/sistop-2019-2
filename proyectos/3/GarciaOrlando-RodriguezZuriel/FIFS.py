#!/usr/bin/python

import os
import sys
import random
import time
import math

fs_image = "FIFS.img"
availableClusters=[]
cluster_size=1024
files={}


def clear(): 
    if os.name == 'nt': 
        _ = os.system('cls') 
    else: 
        _ = os.system('clear') 

class Cluster():
    def __init__(self,i,start):
        self.i = i
        self.registries=[]
        self.start=start
        self.numRegistries = 0

    def commit(self):
        try:
            file_system_image = open(fs_image,'+r') 
            i=self.start
            for registry in self.registries:
                file_system_image.seek(i)
                file_system_image.write(registry.name)
                file_system_image.write(registry.size)
                file_system_image.write(registry.initialCluster)
                file_system_image.write(registry.ctime)
                file_system_image.write(registry.mtime)
                i+=64
        except Exception as w:
            print(e)

class Registry():
	size=64
	def __init__(self,name, size, cluster, ctime, mtime):
		if len(name) <= 15:
		    self.name="0"*(15-len(name)) + name
		elif len(name) > 15 :
			self.name = name[:15]
		self.size="0"*(8-len(size)) + size
		self.initialCluster="0"*(5-len(cluster)) + cluster
		self.ctime="0"*(14-len(ctime)) + ctime
		self.mtime="0"*(14-len(mtime)) + mtime

class FIUNAMFS():
	global availableClusters, cluster_size
	def __init__(self):
		self.clusters=[]
		self.clusters_size=1024
		start=0
		for i in range(1440):
			cluster = Cluster(i,start)
			self.clusters.append(cluster)
			start+=	self.clusters_size
			if i > 5:
				availableClusters.append(i)

		try:
			#Si el archivo existe va a inicializar las variables de acuerdo a los valores almacenados
			file_system_image = open(fs_image,'+r') 
			for i in range(1,5):
				j=0
				pointer = self.clusters[i].start
				while (j < cluster_size):
					file_system_image.seek(pointer)
					name=file_system_image.read(15)
					size=file_system_image.read(8)
					cluster=file_system_image.read(5)
					ctime=file_system_image.read(14)
					mtime=file_system_image.read(14)

					register=Registry(name, size,cluster,ctime,mtime)
					self.clusters[i].registries.append(register)

					j+=64
					pointer += 64
			file_system_image.close()
			
		except FileNotFoundError:
			#En caso de que el archivo no exista lo crea y lo inicializa
			file_system_image = open(fs_image,'w') 

			for i in range(1,5):
				j=0
				while (j < cluster_size):
					register=Registry("AQUI_NO_VA_NADA","13",str(i),"00000000000000","00000000000000")
					self.clusters[i].registries.append(register)
					j+=64
				self.clusters[i].commit()
			self.clusters[0].registries.append("FiUnamFS")
			self.clusters[0].registries.append(" "*2)
			self.clusters[0].registries.append("0.4")
			self.clusters[0].registries.append(" "*7)
			self.clusters[0].registries.append("Zuriel/ Orlando")
			self.clusters[0].registries.append(" "*5)
			self.clusters[0].registries.append("1024")
			self.clusters[0].registries.append(" "*2)
			self.clusters[0].registries.append("004")
			self.clusters[0].registries.append(" "*3)
			self.clusters[0].registries.append("005")
			try:
				file_system_image = open(fs_image,'+r') 
				i=self.clusters[0].start
				for word in self.clusters[0].registries:
					file_system_image.seek(i)
					file_system_image.write(word)
					i+=len(word)
			except Exception as w:
				print(e)

def selectCluster(numClusters):
	global availableClusters
	clusterAvailable = True
	while( clusterAvailable):
		selectedcluster = random.choice(availableClusters)
		for i in range(selectedcluster,selectedcluster+numClusters):
			if i not in availableClusters:
				return selectCluster(numClusters)
		return selectedcluster

def computerToDisk(file):
	global fufs, endOfFile, files, availableClusters
	try:
		computerFile = open(file,"r")
		file_system_image = open(fs_image,'+r') 

		fileName = os.path.basename(file)
		ctime = time.strftime('%Y%m%d%H%M%S', time.gmtime(os.path.getctime(fileName)))
		mtime = time.strftime('%Y%m%d%H%M%S', time.gmtime(os.path.getctime(fileName)))
		contents = computerFile.read()
		size = str(len(contents))
		print("Tamaño: "+size)
        
        #El cluster donde se va a asignar el registro
		registryCluster = random.choice(range(1,5))
		#Revisar que el cluster elegido 
		numOfClustersUsed = math.ceil(int(size)/cluster_size)
		selectedcluster = selectCluster(numOfClustersUsed)

		print("Cluster de registro: "+ str(registryCluster))
		print("Cluster asignado: "+ str(selectedcluster))

		index = -1
		for i in range(len(fufs.clusters[registryCluster].registries)):
			if fufs.clusters[registryCluster].registries[i].name == "AQUI_NO_VA_NADA":
				index = i
				break

		if index != -1:
			fufs.clusters[registryCluster].registries[i] = Registry(fileName,size,str(selectedcluster),ctime, mtime)
			fufs.clusters[registryCluster].commit()
			file_system_image.seek(fufs.clusters[selectedcluster].start)
			print("Contenidos: \n\n"+contents)
			file_system_image.write(contents)
			for i in range(selectedcluster,selectedcluster + numOfClustersUsed):
				availableClusters.remove(i)

			print("Se ha insertado con éxito el archivo: %s" % (fileName))

		else:
			print("[ERROR] No hay espacio disponible")

		computerFile.close()
		file_system_image.close()

	except FileNotFoundError:
		print("[Error] el archivo indicado no existe.")

def diskToComputer(file):
	global fufs
	for i in range(1,5):
		for registry in fufs.clusters[i].registries:
			savedName = "0"*(15-len(file))+file
			if registry.name == savedName:
				print("Se ha hallado el archivo %s" % (file))
				cluster = int(registry.initialCluster)
				size = registry.size
				try:
					file_system_image = open(fs_image,'r+')
					outputfile = open(file+"v2",'w')
					file_system_image.seek(int(fufs.clusters[cluster].start))
					content = file_system_image.read(int(size))
					outputfile.write(content)
					print("El contenido es: \n%s" % (content))
					file_system_image.close()
					outputfile.close()
				except Exception as e:
					print(e)

				return
	print("[ERROR] El archivo no se halla en los registros")

def listFiles():
	global fufs
	files = []
	for i in range(1,5):
		for registry in fufs.clusters[i].registries:
			if registry.name != "AQUI_NO_VA_NADA":
				files.append(registry)

	cadena="Nombre del archivo\tTamaño\t\tCluster\t Modificacion\tCreacion\n"
	for file in files:
		cadena += file.name + "\t\t"+file.size +"\t" + file.initialCluster + "\t" + file.mtime + "\t" + file.ctime +"\n"
	print(cadena)

def deleteFile(file):
	for i in range(1,5):
		i=0
		for registry in fufs.clusters[i].registries:
			savedName = "0"*(15-len(file))+file
			if registry.name == savedName:
				print("Se ha hallado el archivo %s" % (file))
				#Usualmente bastaría únicamente con eliminar la referencia al archivo para considerarlo eliminado.
				#para eliminar redundancia vamos a insertar "0" en lugar de bytes vacios
				
				cluster = int(registry.initialCluster)
				size = registry.size
				print("Se va a proceder con la eliminación")
				fufs.clusters[i].registries[i] = Registry("AQUI_NO_VA_NADA","13",str(i),"00000000000000","00000000000000")
				fufs.clusters[i].commit()
				try:
					file_system_image = open(fs_image,'r+')
					file_system_image.seek(int(fufs.clusters[cluster].start))
					content = file_system_image.write("0"*64)
					numOfClustersUsed = math.ceil(int(size)/cluster_size)
					for i in range(cluster,cluster+numOfClustersUsed):
						availableClusters.append(i)
					file_system_image.close()
				except Exception as e:
					print(e)
				print("El archivo fue eliminado exitosamente")
				return

			i += 1
	print("[ERROR] El archivo no se halla en los registros")

def defragmenter():
	global fufs
	files = []
	for cluster in range(1,5):
		registryNum=0
		for registry in fufs.clusters[cluster].registries:
			if registry.name != "AQUI_NO_VA_NADA":
				files.append([registry,cluster,registryNum])
			registryNum+=1
	#Se obtiene la lista de todos los archivos y se ordenan por tamaños
	files.sort(key=lambda x: int(x[0].size), reverse=True)

	#Se van a volver a reasignar 
	registryCluster = 1
	assignedCluster = 6
	i = 0
    """
	while assignedCluster < 1440:
		try:
			file_system_image = open(fs_image,"r+")
			fileCounter = 0
			for file in files:
				#Se anula el registro original
				registro = Registry("AQUI_NO_VA_NADA","13",str(file[1]),"00000000000000","00000000000000")
				file_system_image.seek(fufs.clusters[file[1]].start + file[2]*64)
				file_system_image.write(registro.name)
				file_system_image.write(registro.size)
				file_system_image.write(registro.initialCluster)
				file_system_image.write(registro.ctime)
				file_system_image.write(registro.mtime)

				registry = file[0]
				cluster = int(registry.initialCluster)
				size = registry.size
				file_system_image.seek(int(fufs.clusters[cluster].start))
				content = file_system_image.write("0"*64)
				numOfClustersUsed = math.ceil(int(size)/cluster_size)
				for i in range(registry.initialCluster,registry.initialCluster+numOfClustersUsed):
					availableClusters.append(i)

				file_system_image.seek(fufs.clusters[registryCluster].start + fileCounter*64)
				file_system_image.write(registry.name)
				file_system_image.write(registry.size)
				file_system_image.write(str(assignedCluster))
				file_system_image.write(registry.ctime)
				file_system_image.write(registry.mtime)
				fileCounter += 1
				if fileCounter % 16 == 0:
					registryCluster += 1

		file_system_image.close()

        except Exception as e:
			print(e)
"""


def main(command, args=[]):
    global fufs
    #clear()
    if command == "-h":
        cadena = "\nfifs.py [-a -b -d argumentos] | fifs [ -h -l]\n"
        cadena += "\n -l  Enlista el contenido del direcciorio"
        cadena += "\n -a  Copia un archivo de la computadora al disco"
        cadena += "\n -b  Copia un archivo del disco a la computadora"
        cadena += "\n -d  Eliminaré un archivo del sistema"
        cadena += "\n -f  Defragmentaré el disco"



        print(cadena)
    elif command == "-l":
        print("Enlistaré los archivos")
        listFiles()
    elif command == "-a":
        print("Copiaré un archivo de la computadora al disco")
        computerToDisk(args[0])
    elif command == "-b":
        print("Copiaré un archivo del disco a la computadora")
        diskToComputer(args[0])
    elif command == "-d":
        print("Eliminaré un archivo")
        diskToComputer(args[0])
    elif command == "-f":
    	print("Desfragmentaré el disco")
    	defragmenter()


    else:
        print ("[ERROR] Comando no identificado.")


if __name__ == "__main__":
    fufs = FIUNAMFS()
    if len(sys.argv) <= 1:
        print ("[ERROR] No se halló comando. Usa FIUNAMFS -h")
        exit()
    if (len(sys.argv) > 2 and sys.argv[1] not in ["copyfc","copyfs","-a","-b"]) or len(sys.argv) > 3:
        print ("[ERROR] Exceso de argumentos. Usa FIUNAMFS -h")
        exit()
    if (len(sys.argv) == 2 and sys.argv[1] in ["copyfc","copyfs","-a","-b","-d"]):
        print ("[ERROR] Falta de argumentos. Usa FIUNAMFS -h")
    elif len(sys.argv) >= 3:
        main(sys.argv[1], sys.argv[2:])
    elif sys.argv[1]:
         main(sys.argv[1])
