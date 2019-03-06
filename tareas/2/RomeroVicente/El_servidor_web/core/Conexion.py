#!/usr/bin/python
# -*- coding: utf-8 -*-
from threading import Thread
from time import sleep
from random import randint


class Conexion:
    def __init__(self,jefe):
        self.jefe = jefe
                
    def intentar_conexion(self):
        while(True):
            rand_num = str(randint(1000000,9999999))
            print("{0} esperando trabajo".format(rand_num))
            while len(self.jefe.get_trabajadores_disponibles()) == 0: ## En caso de que no existan trabajadores devolvera un codigo de error de servidor saturado
                print("Codigo 500 servidor saturado")
                sleep(randint(0,1))
            Thread(target=self.jefe.set_conexion,args=(rand_num,)).start()
            sleep(randint(0,1))
