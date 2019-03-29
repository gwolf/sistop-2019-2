#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scipy.stats as st
import random 
umbral = 0.01
class estacion:
    nombreE = str()
    distanciaT_Panti = float
    distanciaPanti_T = float
    tipoE = str()
    personasEstacion = 0
    def __init__(self,nombreE,distanciaT_P,distanciaP_T,tipoE):
        self.nombreE = nombreE
        self.distanciaT_Panti = distanciaT_P
        self.distanciaPanti_T = distanciaP_T
        self.tipoE = tipoE 
    def getNombreE(self):
        return self.nombreE
    def getTipoE(self):
        return self.tipoE
    def getNumPersonas(self,hora,direccion,t_espera):
        desviacion = random.uniform(3.5,6)
        num_personas = 0
        tasa = 0
        if direccion>0:
            tasa=st.norm.pdf(hora, 7.5, desviacion )
        if direccion<0:
            tasa=st.norm.pdf(hora, 18, desviacion)
        num_personas = tasa*60*20*t_espera
        return int(num_personas)
    def isTerminal(self):
        return self.tipoE == 'T'
    def addPersonasEstacion(self,numero):
        self.personasEstacion += numero
        return
    def personasEnEstacion(self):
        return self.personasEstacion
    def getDistancia(self,Direccion):
        if Direccion > 0:
            return float(self.distanciaPanti_T)
        else:
            return float(self.distanciaT_Panti)

