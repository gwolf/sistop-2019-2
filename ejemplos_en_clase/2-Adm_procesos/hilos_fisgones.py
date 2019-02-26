#!/usr/bin/python
import threading
import time
import random

var = 0

def vive_y_haz_algo():
    global var
    while True:
        var += random.random()
        time.sleep(random.random())

threading.Thread(target=vive_y_haz_algo, args=[], name='Juanito').start()
