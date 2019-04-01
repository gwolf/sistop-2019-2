#!/usr/bin/python
# -*- coding: utf-8 -*-

#Hecho por Brenda Paola Lara Moreno | Luis Arvizu
#Sistop-2019-2| FI-UNAM |
#Ejercicio Implementado: Pumabus
#Lenguaje: Python
#Este trabajo se desarrollo en la version 2.7.10
#Para ejecutarlo requiere de Python, y ejecutarlo desde la terminal posisionandose en
#el directorio donde se encuentre guardado el archivo y
#posteriormente ejecutarlo de la sig manera ----> python PumabusiPaw_Luis.py


import time
import threading

global minutos
global personas

minutos = 0 #contador para los minutos pasados
personas = 0 #contador para el numero de personas en la fila


# Se declaran variables para minimizar el codigo y solo utilizar llamadas de los mensajes a mostras

llegada = 'Llega un '
pumaInactivo = ' Pumabus Estacionado\n'
total = 'Total de '
arrancaPumabus = 'Encendiendo Pumabus...'

mutex = threading.Semaphore(1)
pumaBus = threading.Semaphore(0)


#se declaran funciones 
def Recorrido():		#Inicia recorrido de ruta 1
	print '»------(¯` Inicia Recorrido ´¯)------»'
	time.sleep(2)
	print '*'
	print '*'
	print '*'
	print '*'
	print '»------(¯` Termina Recorrido ´¯)------»'
	

def Personas():
	global personas
	mutex.acquire()
	personas += 1 #Añade a las personas que van formandose en la fila
	print (llegada + 'Persona') + '\n' + (total) + 'Personas = %d' %(personas)
	if personas == 15: #Si son 15  personas sale el pumabus
		pumaBus.release()
	mutex.release()


def Minutos():
	global minutos
	mutex.acquire()
	minutos += 1 #añade a los "minutos" que van pasando 
	print  'Ha pasado un minuto' + '\n' + (total) + 'Minutos = %d' %(minutos)
    if minutos == 25: #Si pasan 25  min sale el pumabus
		pumaBus.release() 
	mutex.release()


def PumaBus():
	global minutos
	global personas
	while True:
		pumaBus.acquire() 
		print (arrancaPumabus)
		mutex.acquire()

		if minutos == 25: #Si pasan 25 min. sale el pumabus
			print (arrancaPumabus)
			Recorrido() 
			minutos -= 25 #Vacia el contador de minutos 
			personas -= personas
		elif personas >= 15: 
			Recorrido()
			personas -= 15 #se vacia el contador de las personas que se fueron en el pumabus
		print (pumaInactivo) 
		mutex.release()


#Definen los tiempos que tardara cada hilo
threading.Thread(target = PumaBus, args = []).start()
while True:
	threading.Thread(target = Personas, args = []).start()
	time.sleep(0.5)
	threading.Thread(target = Minutos, args = []).start()
	time.sleep(0.5)






