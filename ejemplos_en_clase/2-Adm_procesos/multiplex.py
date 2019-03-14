#!/usr/bin/python
import threading
import time

def haz_algo(ident):
    m.acquire()
    print "Soy el fulano numero %d, y ahi voy..." % ident
    time.sleep(0.3)
    print "Y el fulano %d termina!" % ident
    m.release()

m = threading.Semaphore(5)
for i in range(8):
    threading.Thread(target=haz_algo, args=[i]).start()
