#!/usr/bin/python
# -*- coding: utf-8 -*-
#Durán Romero José Arturo
import threading
import time
from random import randrange
import random
alumnos = 0
sillas = 5
num_preguntas = 4
alumnos_que_iran_hoy = 16
multiplex = threading.Semaphore(sillas)
sem_asesor = threading.Semaphore(0)
mutex_preg_resp = threading.Semaphore(1)
mutex_contador = threading.Semaphore(1)
torniquete = threading.Semaphore(1)

def alumno(num):
    multiplex.acquire()
    global alumnos
    time.sleep(1.6+random.random())
    print "Alumno %d presente" % num
    mutex_contador.acquire()
    alumnos = alumnos + 1
    sem_asesor.release()
    mutex_contador.release()
    for i in range (1,num_preguntas):
        torniquete.acquire()
        torniquete.release()
        pregunta_respuesta(num,i)
    multiplex.release()

def profesor():
    a = True
    global alumnos
    print "Profesor vivo, pero dormido"
    while (a):
        sem_asesor.acquire()
        if(alumnos != 0):
            print "Profesor despierto"
        if (alumnos == alumnos_que_iran_hoy):
            a = False

def pregunta_respuesta(num,i):
    mutex_preg_resp.acquire()
    print "Alumno %d preguntando..." %num
    time.sleep(0.6 + random.random())
    print "El profesor está respondiendo la pregunta "+str(i)+" del alumno "+str(num)
    time.sleep(1.3 + random.random())
    mutex_preg_resp.release()

threading.Thread(target=profesor, args=[]).start()
for i in range(alumnos_que_iran_hoy):
    threading.Thread(target=alumno, args=[i]).start()
