from threading import Semaphore, Thread
from time import sleep
from random import random, randint

cubicles = Semaphore(8)
    
def worker(num, tiempo):
    while (tiempo > 0):
        cubicles.acquire()
        print ("El trabajador %s obtiene un cubículo." %num, "Tiempo restante: %d" %tiempo)
        sleep(1)
        tiempo = tiempo - 2
        print ("El trabajador %s deja un cubículo." %num, "Tiempo restante: %d" %tiempo)
        cubicles.release()

#Horas que trabajan los distintos tipos de trabajadores.

times = [6,8,12]
def get_time():
    global times
    aux = randint(0,2)
    return times[aux]

for i in range(10):
    total = get_time()
    Thread(target = worker, args = [i,total]).start()

