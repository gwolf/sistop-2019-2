#!/usr/bin/env python
# -*- coding: utf-8 -*-

def estadisticaP(duracionOri,perdida,lista,Tprom,Eprom,Pprom,i):
    T = perdida + duracionOri
    Tprom = Tprom + T
    P = float(T)/float(duracionOri)
    Pprom = Pprom + P
    E = T - duracionOri
    Eprom = Eprom + E
    print("Proceso: "+str(lista[i][0])+" valor T = "+str(T)+" valor de E = "+str(E)+" valor de P = "+str(float(P)))
    return Tprom,Pprom,Eprom

def RR4(lista,quantum):

    print("---------------EJECUCIÓN RR4----------------")
    print("\nLista de procesos"+str(lista))
    numEle = len(lista)
    perdidas = [0,0,0,0,0]
    ultFin = 0
    ultInicio = 0
    Tprom = 0
    Eprom = 0
    Pprom = 0
    i = 0
    while (len(lista)>0):
        for element in lista:
            print("Lista de perdidas"+str(perdidas))
            if(len(lista) == 0):
                break
            print("longitud: "+str(len(lista)-1))
            print("Consecutivo:" +str(i))
            llegada = lista[i][1]
            duracionOri = lista[i][2]
            duracion = duracionOri
            print("Proceso: "+str(lista[i][0])+" con llegada en: "+str(llegada)+" en duracion: "+str(duracion))
            #print("Duracion"+str(duracion))
            #print("Quantum"+str(quantum))
            determinante = duracion - quantum
            ultInicio = llegada
            lista[i][2] = determinante
            #print("resta:"+str(duracion))

            if(determinante == 0):
                ultFin = ultInicio + quantum
                print("Asignando pérdida a elemento: "  + str(i))
                perdida = perdidas[i]
                Tprom,Pprom,Eprom = estadisticaP(duracionOri,perdida,lista,Tprom,Eprom,Pprom,i)
                lista.pop(i)
                perdidas.pop(i)
                print("Se eliminó")
                print("Lista: "+str(lista))
                i = i + 1

            if(determinante < 0):
                ultFin = ultInicio + duracion
                print("Asignando pérdida a elemento: "  + str(i))
                perdida = perdidas[i]
                Tprom,Pprom,Eprom = estadisticaP(duracionOri,perdida,lista,Tprom,Eprom,Pprom,i)
                lista.pop(i)
                perdidas.pop(i)
                print("Se eliminó")
                print("Lista: "+str(lista))
                i = i + 1
            if(duracion > quantum):
                perdida = ultFin - ultInicio
                perdida = abs(perdida)
                perdidas[i] = perdidas[i] + perdida
                i = i + 1
                print("entró a duracion > quantum")

            if(i >= len(lista)-1):
                i = 0
                print("Se restableció el contador")
                print("Consecutivo r:" +str(i))

    print("--------Resumen RR4 "+"T : "+str(float(Tprom)/float(numEle))+" E: "+str(float(Eprom)/float(numEle))+" P: "+str(float(Pprom)/float(numEle))+"---------")
    print("fin")
