#!/usr/bin/python
# -*- coding: utf-8 -*-
import threading
import time
import random

umbral_balsa = 4
serfs = 0
hackers = 0
sem_balsa = threading.Semaphore(4)
mutex_hackers = threading.Semaphore(1)
barrera_hackers = threading.Semaphore(0)
mutex_serfs = threading.Semaphore(1)


def serf(yo):
    global serfs
    while True:
        mutex_serfs.acquire()
        serfs += 1
        if serfs == umbral_balsa:
            sem_balsa.release()
        elif serfs == 2 and hackers == 2:
        	sem_balsa.release()
        mutex_hackers.release()
        barrera_hackers.acquire()
		#print "Serf %d subió a la balsa" % yo

def hacker(yo):
    global hackers
    while True:
        mutex_hackers.acquire()
        hackers += 1
        if hackers == umbral_balsa:
            sem_balsa.release()
            for i in range(umbral_balsa):
                barrera_hackers.release()
        mutex_hackers.release()
        barrera_hackers.acquire()
		#print "Hacker %d subió a la balsa" % yo


def balsa():
	global hackers
	global serfs
	while True:
		sem_balsa.acquire
		mutex_hackers.acquire()
		mutex_serfs.acquire()
		if hackers == umbral_balsa:
			print "Balsa saliendo con %d hackers" % umbral_balsa
			hackers -= umbral_balsa
		elif serfs == umbral_balsa:
			print "Balsa saliendo con %d serfs" % umbral_balsa
			serfs -= umbral_balsa
		elif serfs == 2 and hackers == 2:
			print "Balsa saliendo con 2 serfs y 2 hackers"
			serfs -=2
			hackers-=2
		else:
			print "Balsa esperando...."
		mutex_hackers.release()
		mutex_serfs.release()

threading.Thread(target=balsa, args=[]).start()
for i in range(10):
    threading.Thread(target=hacker, args=[i]).start()
for i in range(10):
	threading.Thread(target=serf,args=[i]).start()
