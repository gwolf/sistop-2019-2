#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint
import threading
from time import sleep
import signal


class Conexion:
    def __init__(self,jefe):
        self.jefe = jefe
                
    def intentar_conexion(self):
        while(True):
            rand_num = str(randint(1000000,9999999))
            print("{0} esperando trabajo".format(rand_num))
            while len(self.jefe.get_trabajadores_disponibles()) == 0:
                print("Codigo 500 servidor saturado")
                sleep(randint(0,1))
            self.jefe.set_conexion(rand_num)
            sleep(randint(0,1))
