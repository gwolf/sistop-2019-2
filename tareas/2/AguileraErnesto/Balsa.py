#Tarea Semaforos
from threading import Semaphore,Thread
from time import sleep
from random import random

mutex=Semaphore(1)
mutexCreator=Semaphore(1)
mutexGlobal=Semaphore(1)
serfs=0
hackers=0
balsa=0

def creator():
    global serfs
    global hackers
    mutexCreator.acquire()
    if random()>=0.5:
        print("Creando un serf")
        serfs+=1
    else:
        print("Creando un hacker")
        hackers+=1
    sleep(0.3+random()/2)
    mutexCreator.release()

def serfDispatcher():
    global serfs
    global balsa
    mutex.acquire()
    if serfs>=2:
        balsa+=2
        print("Agregamos 2 serfs a la balsa")
        serfs-=2
    sleep(0.1+random()/2)
    mutex.release()

def hackerDispatcher():
    global hackers
    global balsa
    mutex.acquire()
    if hackers>=2:
        balsa+=2
        print("Agregamos 2 hackers a la balsa")
        hackers-=2
    sleep(0.1+random()/2)
    mutex.release()

def cruzaRio():
    global balsa
    global hackers
    global serfs
    while True:
        mutexGlobal.acquire()
        mutex.acquire()
        if balsa==4:
            print("La balsa se va...")
            print("Hackers esperando")
            print(hackers)
            print("Serfs esperando")
            print(serfs)
        sleep(random()/3)
        mutexGlobal.release()

Thread(target=creator).start()
Thread(target=creator).start()
Thread(target=cruzaRio).start()
Thread(target=hackerDispatcher).start()
Thread(target=serfDispatcher).start()
