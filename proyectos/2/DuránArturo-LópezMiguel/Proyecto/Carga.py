#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
from Estacion import *
"""
#Listas:
linea1 = []
linea5 = []
linea9 = []
lineaA = []
"""
def cargarObject(arg,listaEsta):
    with open(str(arg)+'.csv') as File:
        reader = csv.reader(File, delimiter=',')
        for element in reader:
            #print("Leyendo" + str(element))
            estac = estacion(element[0],element[1],element[2],element[3])
            listaEsta.append(estac)

    return listaEsta

#linea1 = cargarObject("Data/L1",linea1)

#for i in linea1:
#    print(i.getNombreE())
#linea5 = cargarObject("Data/L5",linea5)
#print(linea5)
#linea9 = cargarObject("Data/L9",linea9)
#print(linea9)
#lineaA = cargarObject("Data/LA",lineaA)
#print(lineaA)




