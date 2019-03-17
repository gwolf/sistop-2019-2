#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import threading


global alumno

alumno = 0 #contador para el alumno
preguntas = 0 # ontador para las preguntas
max_preguntas = 3 #maximo de preguntas realizadas por cada alumno
max_alumnos = 5 #maximo de alumnos aceptados en el cubiculo
 

mutex = threading.Semaphore (1)
profesor = threading.Semaphore(0)


def  Asesoria(): #Profesor resuelve dudas a los alumnos
	time.sleep (1)
	print ' ---- Profesor resolviendo dudas a Alumnos ---- '

def Pregunta():	#Los alumnos hacen sus 3 preguntas al profesor
	global preguntas 
	global alumno
	
	print ' \nAlumno preguntando '
	print 'pregunta = 1' 
	preguntas += 1
	print 'pregunta = 2'
	preguntas += 1
	print 'pregunta = 3'
	preguntas += 1
	if preguntas == max_preguntas: #Si el alumno hace sus 3 preguntas 
		print '\nSale el Alumno'	#El alumno sale
		alumno -= 1					#DEja libre un espacio en el cubiculo 
		print ' \nQuedan %d' %(alumno) + ' alumnos'
		if alumno >= 5:
			alumno ==-5
			print 'Quedo vacio el cubiculo \n' 
			print 'El profesor  duerme... \n'


def Profesor():
	global alumno
	global preguntas 
	while True:
		profesor.acquire() #El profesor despierta para dar las asesorias
		print '\n Profesor Despierto!' #mensaje que indica que el profesor desperto
		mutex.acquire()
		Pregunta() #los alumnos preguntan
		mutex.release()


def Alumno():
	global alumno
	global preguntas 

	mutex.acquire()
	alumno += 1 #Añade a los alumnos que van llegandop al cubiculo
	print 'Llega un Alumno \n Total de Alumnos = %d' %(alumno)
	if alumno == max_alumnos: #Si son 5 alumnos, el profesor despierta
		profesor.release()
		print '\t\n 5 Alumnos... \n\n' + 'Despertando al profesor...'
		Asesoria() #inicia la asesoria
		Pregunta()	#los alumnos preguntan
	mutex.release()






threading.Thread(target = Profesor, args = []).start()
while True:
	threading.Thread(target = Alumno, args = []).start()
	time.sleep(1)