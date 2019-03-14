#!/usr/bin/python
# -*- coding: utf -8 -*-

import threading 
import time
import random


mutex_prof = threading.Semaphore(1)
mutex_alum = threading.Semaphore(1)
mutex_sill = threading.Semaphore(0)
sem_ace = threading.Semaphore(1)
num_alumnos=30
num_sillas = 5
sillas_ocupadas=0
alumnos_ace=0
def profesor():
	global sillas_ocupadas
	global alumnos_ace
	print "profesor vivo"
	mutex_prof.acquire() #Esta es la sección crítica para que si no hay sillas ocupadas
	if sillas_ocupadas == 0:
		print "profesor duerme" 
	        time.sleep(3)
	        mutex_prof.release()

	sem_ace.acquire() #mutex para saber si hay alumnos que acesorar
	if sillas_ocupadas > 0:

		if alumnos_ace == 1:
			print "Acesorando a alumno"
			time.sleep(5)
	alumnos_ace = alumnos_ace + 1
        

	sem_ace.release()
def alumno(espera):
	global sillas_ocupadas
	global alumnos_ace
	time.sleep(2)
	mutex_alum.acquire()	
	print"Alumno vivo"
	time.sleep(1)
	mutex_alum.release()
def sillas(num):
	global sillas_acupadas
	print "soy una silla"

	mutex_sill.acquire() #las sillas se van llenando conforme pasa los alumnos, solo hay 5 sillas
	
	
	if sillas_ocupadas == 5:

                
                print "%d sillas ocupadas" % num
                sillas_ocupadas = sillas_ocupadas - 1
	

        mutex_sill.release()

	sillas_ocupadas = sillas_ocupadas + 1	



threading.Thread(target=profesor, args=[]).start()
for i in range(num_alumnos):
        threading.Thread(target=alumno, args=[i]).start()

for i in range(num_sillas):
        threading.Thread(target=sillas, args=[i]).start()
