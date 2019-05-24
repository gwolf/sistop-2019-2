#!/usr/bin/env python
#@Osmar Juarez Aguilar
#@Luis Angel Morales Garcia

import os 
import sys 
import struct 

#funcion que lista el contenido de nuestro sistema de archivos
def listado():
	nomAux=''
	#arreglo que contiene las diferentes extensiones que se pueden encontrar
	#en nuestro sistema de archivos fiunamfs
	extensiones=['png','jpg','pdf','docx','txt','org','csv','PNG','JPG','PDF']
	#se si mula montar nuestro sistema de archivos booteable leyendo todos el 
	#contenido binario de nuestro sistema 
	fp=open("fiunamfs.img",'rb').read()
	#a partir de este punto inicia nuestros clousters vacios (valor en hexadecimal)
	offHex="400"
	#se convierte el offset hexadecimal a decimal para un facil manejo
	offset=int(offHex,16)
	#este es el offset total que alcazaria nuestros clousters destinados para el
	#almacenamiento de archivos final=1440x512B
	final= 737280
	#el limite del bloque que contiene el nombre de un archivo  
	limiteCadena = offset + 16
	aux = offset
	while(offset <= final):
		#este ciclo extrae caracter por caracter el contenido del bloque con el nombre
		#del archivo, struct.unpack_from(tipoSalidaDato,pointerFileSyst,offset), la funcion
		#o regresa una tupla con el caracter en ese byte
		while(aux < limiteCadena):
			data=struct.unpack_from('>s',fp,aux)
			nomAux=nomAux+data[0] #se guarda el valor de la tupla en una cadena
			aux = aux + 1
		
		#se limpia la cadena, quitandole espacios y caracteres para ver mejor que tipo de 
		#archivo es
		nomAux = nomAux.translate(None, ' ') 
		nomAux = nomAux.translate(None, '\x00')
		#se obtiene la extension del nombre del archivo
		#(en caso de que sea un nombre de archivo valido con extension)
		extFIle=nomAux.rpartition('.')[-1]
		#se verifica que la extension sea valida con la lista declarada al inicio
		for i in extensiones:
			#de ser asi se imprime el nombre del archivo que se encuenra en nuestro FIUNAMFS
			if (extFIle==i):
				print("\t"+nomAux)
		#se limpia la variable aux que contiene el nombre del clouster
		nomAux=''
		#se avanza al siguinete clouster 
		offset = offset+32
		limiteCadena=offset+16
		aux = offset


def buscaArchivo():
	fileName=raw_input("Ingresa el nombre del archivo a eliminar: ")
	offsetDelete=0
	nomAux=''
	fp=open("fiunamfs.img",'rb').read()
	offHex="400"
	#se convierte el offset hexadecimal a decimal para un facil manejo
	offset=int(offHex,16)
	#este es el offset total que alcazaria nuestros clousters destinados para el
	#almacenamiento de archivos final=1440x512B
	final= 737280
	#el limite del bloque que contiene el nombre de un archivo  
	limiteCadena = offset + 16
	aux = offset
	while(offset <= final):
		#este ciclo extrae caracter por caracter el contenido del bloque con el nombre
		#del archivo, struct.unpack_from(tipoSalidaDato,pointerFileSyst,offset), la funcion
		#o regresa una tupla con el caracter en ese byte
		while(aux < limiteCadena):
			print(aux)
			data=struct.unpack_from('>s',fp,aux)
			print(data)
			nomAux=nomAux+data[0] #se guarda el valor de la tupla en una cadena
			aux = aux + 1

		#se limpia la cadena, quitandole espacios y caracteres para ver mejor que tipo de 
		#archivo es
		nomAux = nomAux.translate(None, ' ') 
		nomAux = nomAux.translate(None, '\x00')
		#se compara que el header extraido sea el nombre del archivo que se busca eliminar
		if(nomAux==fileName):
			offsetDelete=offset
			
			break
		#se limpia la variable aux que contiene el nombre del clouster
		nomAux=''
		#se avanza al inicio del siguinete clouster 
		offset = offset+32
		limiteCadena=offset+16
		aux = offset

	return offsetDelete


def elimina(offsetElimina):
	if offsetElimina==0:
		print(" \t\tERROR: Archivo no encontrado en FIUNAMFS\n")
	else:
		fp=open("fiunamfs.img",'wb')
		offHex="400"
		#se convierte el offset hexadecimal a decimal para un facil manejo
		offset=int(offHex,16)
		#este es el offset total que alcazaria nuestros clousters destinados para el
		#almacenamiento de archivos final=1440x512B
		final= 737280
		#el limite del bloque que contiene el nombre de un archivo  
		limiteCadena = offset + 16
		aux = offset
		emptyClouster='AQUI_NO_VA_NADA'
		varAuxZeros=0
		while(offset <= final):
			#se busca el offset donde se encuentra el archivo a "Eliminar"
			#una vez encontrado se escribe en el espacio designado para su nombre 
			#AQUI_NO_VA_NADA. Esto mediante la funcion struct.pack(tipoArgEscribir, 
			#cadenaEscribir,cerosEspaciosRestantes)
			if offset==offsetElimina:
				while(aux < limiteCadena):
					entry=struct.pack('<p',emptyClouster,varAuxZeros)
					fp.write(entry)
					fp.flush()
					aux=aux+1
				print("\tArchivo eliminado de FIUNAMFS\n")
				break
			#se avanza al inicio del siguiente clouster
			offset = offset+32
			limiteCadena=offset+16
			aux = offset
		fp.close()

#def copiaArchivoDesde():
	#La idea era mandar a pedir la ruta del archivo que queria copiar el usuario
	#haciendo uso de funciones de la biblioteca os que imprtamos, funciones como path
	#para guardar la ruta de ese archivo.
	#El siguiente paso seria abrir ese archivo en modo lectura con las funciones como 
	#open(ruta,'rb') despues guardar ese contenido en un arreglo de bytes del tamanio
	#de un clouster, y despues escribir el contenido de ese arreglo en un clauster que 
	#tuviera la etiqueta AQUI_NO_VA_NADA

#def copiaArchivoHacia():
	#Para la idea de copiar desde nuestro FS hacia nuestra computadora era la ingenieria
	#inversa de la funcion anterior, es decir que el usuario nos inndique el nombre del 
	#arhivo guardado en fiunamfs y buscarlo con la funcion definica mas arriba y una ves 
	#veriicado que exista encontrar el offset donde empieza su clauster y empezar a sacar 
	#su contenido y guardarlo en un arreglo y despues que el usuario nos indique en donde
	#quiere que compiemos eso en su computadora para crar un archivo en con l informacion
	#extraida del clauster

#def defrag():
	#La idea para la desfragmentacion fue complicada pero como lo habiamos pensafo fue que
	#recorrieramos todo el dispositivo FIUNAMFS y guardaramos el numero de clusters libres 
	#y a la vez trataramos de identificar si un archivo ocupaba mas de un clouster para su 
	#informacion y asi determinaramos en que momento moveriamos todo. Guardando el contenido
	#de un clauster a mover en un arreglo de bytes auxiliar	

def main():
	flag=True
	fileName=''
	while(flag):
		print("\n")
		print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
		print("\t\tBienvenido al Micro Sistema de Archivos\n")
		print("\t Seleccione un opcion: \n")
		print("1. Listar contenido de FIUNAMFS \n")
		print("2. Copiar archivo a FIUNAMFS \n")
		print("3. Copiar archivo de FIUNAMFS a su computadora\n")
		print("4. Eliminar archivo de FIUNAMFS \n")
		print("5. Desfragmentar FIUNAMFS \n")
		print("6. Salir \n")
		print("NOTA: opciones 2, 3 y 5 solo se plantea la idea\n")
		opcion=input("---->")

		if opcion==1:
			print("El contenido de FIUNAMFS es: \n")
			listado()
		elif opcion==2:
			print("ERROR001: Nos falto tiempo :(")
			print("LO SENTIMOS :( \n por el momento no se encuentra disponible esta opcion")
		elif opcion==3:
			print("ERROR002: Nos falto mas tiempo :(")
			print("LO SENTIMOS :( \n")
			print("por el momento no se encuentra disponible esta opcion\n")
		elif opcion==4:
			print("Buscando Archivo...")
			offsetDeleteFile=buscaArchivo()
			elimina(offsetDeleteFile)
		elif opcion==5:
			print("ERROR003: Nos falto mas tiempo :(")
			print("LO SENTIMOS :( \n por el momento no se encuentra disponible esta opcion")
			print("Estaba de pensarle mas pero seguiremos desarrollando esta parte")
		elif opcion==6:
			print("\tHasta pronto (*.*)/ \n")
			flag=False

main()