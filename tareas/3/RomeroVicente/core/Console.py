#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
from threading import Thread
from core.FCFS import FCFS
from core.Proceso import Proceso
from core.RoundRobin import RoundRobin
from core.RoundRobin4 import RoundRobin4



class Console:
    def __init__(self):
        self.parser = parser = argparse.ArgumentParser()
        self.parser.add_argument('-p','--process',nargs='?', default=5, type=int, help='define con un numero entero cuantos procesos concurrentes se van a crear')
        self.parser.add_argument('-q','--quantum',nargs='?', default=80, type=int, help='define con un numero entero el tamaño del quantum a simular en ticks = ms')
        self.parser.add_argument('-l','--log', nargs='?', default="log.txt", type=str,help='define el nombre del archivo de texto que guardara la informacion de contabilidad')
        self.args = parser.parse_args()

    def iniciar_consola(self):
        procesos = []
        for i in range(self.args.process):
            procesos.append(Proceso()) ## se inicializa la lista de procesos
        fcfs = FCFS(self.args.log,self.args.quantum,procesos)
        round_robin = RoundRobin(self.args.log,self.args.quantum,procesos)
        round_robin4 = RoundRobin4(self.args.log,self.args.quantum,procesos)
        fcfs.iniciar_planificador()
        round_robin.iniciar_planificador()
        round_robin4.iniciar_planificador()