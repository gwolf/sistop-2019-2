#!/usr/bin/python
# -*- coding: utf-8 -*-
from threading import Semaphore, Thread
from core.Conexion import Conexion
from core.Trabajador import Trabajador
from time import time
from datetime import datetime
from random import randint
from time import sleep
class Jefe:
    def __init__(self,log,max_workers):
        self.worker = []
        self.num_workers = 0
        self.max_workers = max_workers
        self.log = log
        self.sem = Semaphore(1)
        Thread(target = self.control).start()

    def asignar_worker(self):
        self.num_workers = self.num_workers + 1
        uid = self.num_workers
        trabajador = Trabajador(uid)
        self.worker.append(trabajador)
        tiempo_inicio = time()
        trabajador.procesar_conexion()
        tiempo_fin = time()
        tiempo_total = tiempo_fin - tiempo_inicio
        self.sem.acquire()
        with open(self.log,"a") as outfile:
            outfile.write("{2} trabajador {0} proceso conexion {3} en {1} segundos\n".format(uid,tiempo_total,datetime.now(),trabajador.conexion_id))
        self.sem.release()
        print("Trabajador {0} escuchando conexion".format(trabajador.uid))

    def set_conexion(self,conexion_id):
        self.get_trabajador_disponible().despertar(conexion_id)

    def get_trabajadores_disponibles(self):
        worker_temp = []
        for worker in self.worker:
            if worker.is_listening() == True:
                worker_temp.append(worker)
        self.worker = worker_temp
        return worker_temp
    
    def get_trabajador_disponible(self):
        return self.get_trabajadores_disponibles()[0]

    def control(self):
        while(True):
            while len(self.get_trabajadores_disponibles()) < self.max_workers: #Este ciclo estara activo hasta que existan el numero definido de trabajadores a la espera
                Thread(target=self.asignar_worker).start()
            sleep(randint(0,1))