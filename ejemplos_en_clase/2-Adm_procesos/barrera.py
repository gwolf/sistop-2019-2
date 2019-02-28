#!/usr/bin/python

from threading import Semaphore,Thread
from time import sleep
from random import random
maximo = 5
num = 0
mut = Semaphore(1)
barr = Semaphore(0)

def todos_juntos(yo):
    global num, mut, barr
    espera = random()
    print "Soy el hilo %d y me toca esperar %f" % (yo, espera)
    sleep(espera)

    mut.acquire()
    num = num + 1
    print "Y ya somos %d hilos..." % num
    if num == maximo:
        print "Liberemos esa barrera!"
        barr.release()
    mut.release()
    barr.acquire()
    barr.release()

    print "Soy el hilo %d y ya termine" % yo


for i in range(10):
    Thread(target=todos_juntos, args=[i]).start()
