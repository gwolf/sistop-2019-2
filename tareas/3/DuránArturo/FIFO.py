#!/usr/bin/env python
# -*- coding: utf-8 -*-

def FIFO(lista):
    print("-------------EJECUCIÓN FIFO----------------")
    print("Lista de procesos: " + str(lista))
    i = 0
    retraso = 0
    ubicacionact = 0
    Tprom = 0
    Eprom = 0
    Pprom = 0
    for element in lista:
        print("longitud de la lista:"+str(len(lista))+" tipo: "+str(type(lista)))
        llegada = lista[i][1]
        duracion = lista[i][2]
        print("Proceso: "+str(lista[i][0])+" con llegada en: "+str(llegada)+" en duracion: "+str(duracion))
        if(i == 0):
            retraso = 0
        else:
            retraso = ubicacionact - llegada
        T = retraso + duracion
        Tprom = Tprom + T
        P = float(T)/float(duracion)
        Pprom = Pprom + P
        E = T - duracion
        Eprom = Eprom + E
        ubicacionact = ubicacionact + duracion
        print("Proceso: "+str(lista[i][0])+" valor T = "+str(T)+" valor de E = "+str(E)+" valor de P = "+str(float(P)))
        i = i + 1
    print("--------Resumen FIFO "+"T : "+str(float(Tprom)/float(len(lista)))+" E: "+str(float(Eprom)/float(len(lista)))+" P: "+str(float(Pprom)/float(len(lista)))+"---------")
