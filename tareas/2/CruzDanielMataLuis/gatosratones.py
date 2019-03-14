import threading
import time

ratones = 0
mutex = threading.Semaphore(1)
plato_disponible = threading.Semaphore(1)
torniquete = threading.Semaphore(1)

def gato(num):
    global ratones
    print "El gato %d esta en la casa" % num
    torniquete.acquire()
    if ratones >= 1:
        print "Hay %d ratones en la casa!" %ratones
        gato_come_raton(num)
        ratones = ratones - 1  
    plato_disponible.acquire()
    gato_come(num)
    print "Soy el gato %d y termine de comer" %num
    plato_disponible.release()
    torniquete.release()

def raton(num):
    global ratones
    torniquete.acquire()
    torniquete.release()
    print "El raton %d esta en la casa" % num
    mutex.acquire()
    ratones = ratones + 1
    if ratones == 1:
        plato_disponible.acquire()
    mutex.release()

    raton_come(num)

    mutex.acquire()
    ratones = ratones - 1
    if ratones == 0:
        plato_disponible.release()
    print "Soy el raton %d y termine de comer" %num
    mutex.release()

def gato_come(num):
    print "Se acerca el gato %d" %num
    print "Gato %d: comiendo..." % num
    time.sleep(1)

def raton_come(num):
    print "Raton %d comiendo.........." % num
    time.sleep(7)

def gato_come_raton(num):
    print "El gato %d se comio un raton" %num
    

def lanza_raton():
    for i in range(30):
        threading.Thread(target=raton, args=[i]).start()
        time.sleep(0.3)

def lanza_gato():
    for i in range(30):
        threading.Thread(target=gato, args=[i]).start()
        time.sleep(5)

threading.Thread(target=lanza_gato).start()
threading.Thread(target=lanza_raton).start()
