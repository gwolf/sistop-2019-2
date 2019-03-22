#!/usr/bin/env python
# -*- coding: utf-8 -*-

def estadisticaP1(duracionOri,perdida,lista1,Tprom,Eprom,Pprom,i):
    T = perdida + duracionOri
    Tprom = Tprom + T
    P = float(T)/float(duracionOri)
    Pprom = Pprom + P
    E = T - duracionOri
    Eprom = Eprom + E
    print("Proceso: "+str(lista1[i][0])+" valor T = "+str(T)+" valor de E = "+str(E)+" valor de P = "+str(float(P)))
    return Tprom,Pprom,Eprom

def RR1(lista1,quantum):
    print("---------------EJECUCIÓN RR1----------------")
    print("\nlista1 de procesos"+str(lista1))
    numEle = len(lista1)
    perdidas = [0,0,0,0,0]
    ultFin = 0
    ultInicio = 0
    Tprom = 0
    Eprom = 0
    Pprom = 0
    i = 0
    while (len(lista1)>0):
        for element in lista1:
            print("lista1 de perdidas"+str(perdidas))
            if(len(lista1) == 0):
                break
            print("longitud: "+str(len(lista1)-1))
            print("Consecutivo:" +str(i))
            llegada = lista1[i][1]
            duracionOri = lista1[i][2]
            duracion = duracionOri
            print("Proceso: "+str(lista1[i][0])+" con llegada en: "+str(llegada)+" en duracion: "+str(duracion))
            #print("Duracion"+str(duracion))
            #print("Quantum"+str(quantum))
            determinante = duracion - quantum
            ultInicio = llegada
            lista1[i][2] = determinante
            #print("resta:"+str(duracion))

            if(determinante == 0):
                ultFin = ultInicio + quantum
                print("Asignando pérdida a elemento: "  + str(i))
                perdida = perdidas[i]
                Tprom,Pprom,Eprom = estadisticaP1(duracionOri,perdida,lista1,Tprom,Eprom,Pprom,i)
                lista1.pop(i)
                perdidas.pop(i)
                print("Se eliminó")
                print("lista1: "+str(lista1))
                i = i + 1

            if(determinante < 0):
                ultFin = ultInicio + duracion
                print("Asignando pérdida a elemento: "  + str(i))
                perdida = perdidas[i]
                Tprom,Pprom,Eprom = estadisticaP1(duracionOri,perdida,lista1,Tprom,Eprom,Pprom,i)
                lista1.pop(i)
                perdidas.pop(i)
                print("Se eliminó")
                i = i + 1
            if(duracion > quantum):
                perdida = ultFin - ultInicio
                perdida = abs(perdida)
                perdidas[i] = perdidas[i] + perdida
                i = i + 1

            if(i >= len(lista1)-1):
                i = 0
                print("Se restableció el contador")
                print("Consecutivo r:" +str(i))

    print("--------Resumen RR1 "+"T : "+str(float(Tprom)/float(numEle))+" E: "+str(float(Eprom)/float(numEle))+" P: "+str(float(Pprom)/float(numEle))+"---------")
    print("fin")
