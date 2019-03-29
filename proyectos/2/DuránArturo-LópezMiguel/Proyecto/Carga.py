#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
from Estacion import *

def cargarObject(arg,listaEsta):
    with open(str(arg)+'.csv') as File:
        reader = csv.reader(File, delimiter=',')
        for element in reader:
            #print("Leyendo" + str(element))
            estac = estacion(element[0],element[1],element[2],element[3])
            listaEsta.append(estac)

    return listaEsta





