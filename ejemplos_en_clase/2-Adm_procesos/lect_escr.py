import threading
import time

lectores = 0
mutex = threading.Semaphore(1)
cuarto_vacio = threading.Semaphore(1)
torniquete = threading.Semaphore(1)

def escritor(num):
    print "Va el escritor %d" % num
    torniquete.acquire()
    cuarto_vacio.acquire()
    escribe(num)
    cuarto_vacio.release()
    torniquete.release()

def lector(num):
    global lectores
    torniquete.acquire()
    torniquete.release()
    print "Va el lector %d" % num
    mutex.acquire()
    lectores = lectores + 1
    if lectores == 1:
        cuarto_vacio.acquire()
    mutex.release()

    lee(num)

    mutex.acquire()
    lectores = lectores - 1
    if lectores == 0:
        cuarto_vacio.release()
    mutex.release()

def lee(num):
    print "Lector %d: leyendo..." % num
    time.sleep(1)

def escribe(num):
    print "Escritor %d escribiendo.........." % num
    time.sleep(7)

def lanza_lect():
    for i in range(50):
        threading.Thread(target=lector, args=[i]).start()
        time.sleep(0.3)

def lanza_escr():
    for i in range(5):
        threading.Thread(target=escritor, args=[i]).start()
        time.sleep(5)

threading.Thread(target=lanza_escr).start()
threading.Thread(target=lanza_lect).start()
