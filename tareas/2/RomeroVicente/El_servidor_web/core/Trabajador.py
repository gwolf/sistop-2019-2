#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import random
from time import sleep
import threading

class Trabajador:
    def __init__(self,uid):
        self.uid = uid
        self.code = False ## Por defecto esta en modo activo o a la escucha
        self.semaforo = threading.Semaphore(0)
        self.conexion_id = 0

    def procesar_conexion(self):
        self.semaforo.acquire()
        self.code = True ##Aqui ya esta despierto y trabajando
        print("Trabajador {0} procesando...".format(self.uid))
        sleep(random())
        print("Trabajador {0} Finalizado".format(self.uid))      

    def is_listening(self):
        if self.code == False:
            return True
        else:
            return False

    def despertar(self,conexion_id):
        self.semaforo.release()
        self.conexion_id = conexion_id
        