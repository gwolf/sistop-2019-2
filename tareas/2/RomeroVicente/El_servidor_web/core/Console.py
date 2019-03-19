#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
from threading import Thread, enumerate
from time import sleep
from core.Jefe import Jefe
from core.Conexion import Conexion




class Console:
    def __init__(self):
        self.parser = parser = argparse.ArgumentParser()
        self.parser.add_argument('-t','--threads',nargs='?', default=1, type=int, help='define con un numero entero cuantos hilos se van a crear')
        self.parser.add_argument('-l','--log', nargs='?', default="log.txt", type=str,help='define el nombre del archivo de texto que guardara la informacion de contabilidad')
        self.args = parser.parse_args()

    def iniciar_consola(self):
        jefe = Jefe(self.args.log,self.args.threads)
        conexion = Conexion(jefe)
        Thread(target = conexion.intentar_conexion, name="programa principal").start()