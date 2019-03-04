#!/usr/bin/python
# -*- coding: utf-8 -*-

#Hecho por Benda Paola Lara Moreno
#Sistop-2019-1|FI-UNAM|iPaw
#Ejercicio: Santa Claus
#Lenguaje: Python
#Este trabajo se desarrollo en la version 2.7.10
#Para ejecutarlo requiere de Python, y ejecutarlo desde la terminal posisionandose en
#el directorio donde se encuentre guardado el archivo y
#posteriormente ejecutarlo de la sig manera ----> python santaiPaw.py


import time
import threading

global reno
global elfo

reno = 0 #contador para el reno
elfo = 0 #contador para el elfo

# se declaran variables con los contenidos de los mensajes a mostrar
mensaje = 'Llega un '
santaDuerme = 'zzZZzz Santa Vuelve a  Dormir zzZZzz\n'
total = 'Total de '
despierta = 'Despertando a Santa...'
santaDespierto = '¡Santa Desperto! \n ⊙﹏⊙ \n' #Es santa con los ojos abiertos (despierto)
ayuda = 'Santa Ayudando a Elfos'
mutex = threading.Semaphore(1)
santaClaus = threading.Semaphore(0)

#se declaran funciones que realiza santa
def viaje_anual():		#Santa se va a su viaje anual
	print '»------(¯` Inicia Viaje Anual ´¯)------»'
	time.sleep(2)
	print '*'
	print '*'
	print '*'
	print '*'
	print '»------(¯` Termina Viaje Anual ´¯)------»'
	print '\n¡Renos de Vacaciones!'

def ayuda_santa(): #Santa ayuda a elfos
	time.sleep (2)
	print (ayuda)

def Elfo():
			global elfo
			mutex.acquire()
			elfo += 1 #Añade a los elfos que van llegandop al contador
			print (mensaje + 'Elfo') + '\n' + (total) + 'Elfos = %d' %(elfo)
			if elfo == 3: #Si son 3 elfos, santa despierta
				santaClaus.release()
				print '\t\n 3 Elfos... \n\n' + (despierta)
			mutex.release()

def Reno():
	global reno
	mutex.acquire()
	reno += 1 #añade a los renos que van llegando
	print (mensaje + 'Reno') + '\n' + (total) + 'Renos = %d' %(reno)
	if reno == 9: #Si llegan los 9 renos
		santaClaus.release() #Santa despierta
	mutex.release()

def Santa():
	global elfo
	global reno
	while True:
		santaClaus.acquire() #santa despierta para ayudar a elfos o irse al viaje anual
		print (santaDespierto) #muestra mensaje que santa esta despierto
		mutex.acquire()

		if reno == 9: #Si llegan los 9 renos santa se va al viaje
			print '¡Los Renos han regresado!'
			viaje_anual() #Inicia y termina el viaje anual de santa con los 9 renos
			reno -= 9 #Vacia el contador de renos restandole los 9 renos que ya se habian ido
		elif elfo >= 3: #Si hay tres elfos llaman a santa
			ayuda_santa()
			elfo -= 3 #se vacia el contador de elfos porque ya fueron auxiliados
		print (santaDuerme) #Mensaje que santa se vuelve a dormir
		mutex.release()

threading.Thread(target = Santa, args = []).start()
while True:
	threading.Thread(target = Reno, args = []).start()
	time.sleep(0.5)
	threading.Thread(target = Elfo, args = []).start()
	time.sleep(0.5)