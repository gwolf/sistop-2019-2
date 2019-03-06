#!/usr/bin/python
# -*- coding: utf-8 -*-
import threading
import time
import random

prob_falla = 0.03
num_renos = 9
num_elfos = 100
elfos_atorados = 0
umbral_elfo = 3

mutex_elfos = threading.Semaphore(1)
barrera_elfo = threading.Semaphore(0)
sem_santa = threading.Semaphore(0)
renos = []
renos_en_casa = 0
mutex_ctr_renos = threading.Semaphore(1)
barrera_renos = threading.Semaphore(0)

def elfo(yo):
    global elfos_atorados
    while True:
        # Tiempo de fabricación del juguete canónico
        time.sleep(2.5+random.random())
        if random.random() < prob_falla:
            print "¡El elfo %d tuvo un problema!" % yo
            mutex_elfos.acquire()
            elfos_atorados += 1
            if elfos_atorados == umbral_elfo:
                sem_santa.release()
                for i in range(umbral_elfo):
                    barrera_elfo.release()
            mutex_elfos.release()
            barrera_elfo.acquire()
            print "¡Santaaaa! Al elfo %d se le rompió su trabajo" % yo

def santa():
    global elfos_atorados
    print "¡Hola! Soy Santa y estoy vivo."
    while True:
        sem_santa.acquire()
        mutex_elfos.acquire()
        if elfos_atorados == umbral_elfo:
            print "Vamos a arreglar %d juguetes..." % umbral_elfo
            elfos_atorados -= umbral_elfo
        else:
            print "¡Hora de repartir regalos, jo jo jo jo!"
        mutex_elfos.release()


def reno(yo):
    global renos_en_casa
    print "¡Hola! Soy el reno número %d y me voy de vacaciones." % yo
    while True:
        # Descansamos 11 meses y algunos días
        time.sleep(11 + random.random() )
        # Terminaron tus vacaciones.
        mutex_ctr_renos.acquire()
        print "Reno %d volviendo a casa" % yo
        renos_en_casa += 1
        if renos_en_casa == num_renos:
            print "Despertando al rebaño"
            for i in range(num_renos):
                barrera_renos.release()
            sem_santa.release()
        mutex_ctr_renos.release()
        print "Esperemos al resto del grupo... (%d)" % yo
        barrera_renos.acquire()
        print "¡Vámonos a repartir por todo el mundo!"

threading.Thread(target=santa, args=[]).start()
for i in range(num_renos):
    threading.Thread(target=reno, args=[i]).start()
for i in range(num_elfos):
    threading.Thread(target=elfo,args=[i]).start()
