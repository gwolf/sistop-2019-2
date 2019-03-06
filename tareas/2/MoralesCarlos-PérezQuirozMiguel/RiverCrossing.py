from threading import Semaphore,Thread
from time import sleep
from random import random, randrange

raft_capacity = 4
mutex = Semaphore(1)
barrier = Semaphore(0)
hackers_count = 0
serfs_count = 0
hackers_waiting = Semaphore(0)
serfs_waiting = Semaphore(0)
ready = False

def go():
    for i in range (4):
        barrier.release()
    print("Sale la balsa")

def board(name, espera):
    print ("Sube %s" %name)
    sleep(espera)

def hacker(num):
    global hackers_count, serfs_count, ready
    mutex.acquire()
    hackers_count +=1
    if hackers_count == 4:
        #Liberar hackers(4)
        for i in range (4):
            hackers_waiting.release()
        hackers_count = 0
        ready = True
        #Liberar mutex
        #mutex.release()
    elif hackers_count == 2 and serfs_count >= 2:
        #Liberar hackers(2)
        for i in range (2):
            hackers_waiting.release()
        #Liberar serfs(2)
        for i in range (2):
            serfs_waiting.release()
        serfs_count -= 2
        hackers_count = 0
        ready = True
        #Liberar mutex
        #mutex.release()
    else:
        mutex.release()
    #Hacker espera
    hackers_waiting.acquire()
    #Abordar
    board("Hacker", random())
    #Espera para que los demás aborden
    if ready == True:
        ready = False
        #libera la balsa
        go()
        mutex.release()
    barrier.acquire()           

def serf(num):
    global hackers_count, serfs_count, ready
    mutex.acquire()
    serfs_count +=1
    if serfs_count == 4:
        #Liberar serfs(4)
        for i in range (4):
            serfs_waiting.release()
        serfs_count = 0
        ready = True
        #Liberar mutex
        #mutex.release()
    elif serfs_count == 2 and hackers_count >= 2:
        #Liberar serfs(2)
        for i in range (2):
            serfs_waiting.release()
        #Liberar hackers(2)
        for i in range (2):
            hackers_waiting.release()
        hackers_count -= 2
        serfs_count = 0
        ready = True
        #Liberar mutex
        #mutex.release()
    else:
        mutex.release()
    #Serf espera
    serfs_waiting.acquire()
    #Abordar()
    board("Serf", random())
    #Barrera acquire
    if ready == True:
        ready = False
        #libera la balsa
        go()
        mutex.release()
    barrier.acquire()

total = randrange(2, 20, 2)
for i in range(total):
    Thread(target = serf, args = [i]).start()
    Thread(target = hacker, args = [i]).start()