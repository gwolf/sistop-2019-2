#!/usr/bin/python
import threading
import time
i = 0
k = 0
print " -------------------------------------------"
print "| Este es el ejercicio 7: El cruce del rio |"
print " -------------------------------------------\n\n"
def cruzar(ident):
    global i
    m.acquire()
    for a in range(4):
        i+=1
        print "Soy el Hacker [%d] y subire" % i
        time.sleep(0.3)
    print "Empieza el viaje" 
    print "La lancha llego\n\n"  
    m.release()

def cruzar2(ident):
    global k
    m.acquire()
    for a in range(4):
        k+=1
        print "Soy el desarrollador [%d] y subire" % k
        time.sleep(0.3)
    print "Empieza el viaje" 
    print "La lancha llego\n\n" 
    m.release()

def cruzar3(ident):
    global k
    global i
    m.acquire()
    for a in range(2):
        k+=1
        print "Soy el desarrollador [%d] y subire" % k
        time.sleep(0.3)
    for b in range(2):
        i+=1
        print "Soy el Hacker [%d] y subire" % i
        time.sleep(0.3)
    print "Empieza el viaje" 
    print "La lancha llego\n\n" 
    m.release()
m = threading.Semaphore(1)

for j in range(2):
    threading.Thread(target=cruzar, args=[i]).start()
    threading.Thread(target=cruzar2, args=[i]).start()
    threading.Thread(target=cruzar3, args=[i]).start()

