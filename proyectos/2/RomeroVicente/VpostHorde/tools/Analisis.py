import sys
import ast
import wx
from wx.lib.plot import PlotCanvas, PlotGraphics, PolyLine, PolyMarker
import numpy as np
import math

class Analisis(object):
    def __init__(self):
        self.times = []
        self.state_codes = []
        self.estados = []
        self.fechas = []
        self.tiempo_promedio = 0
        self.exitosVSFallos = {"exitos":0,"fallos":0} #Inicializa el estatus de exitos vs fallas
        self.state_codes_dict = {}

    def analizar_tiempo(self): # calcula el tiempo promedio de todas las peticiones
        self.tiempo_promedio = 0 
        for segundos in self.times:
            self.tiempo_promedio = self.tiempo_promedio + segundos
        self.tiempo_promedio = self.tiempo_promedio / len(self.times)

    def analizar_estados(self): # llena el status de exito vs fallo
        self.exitosVSFallos["exitos"] = 0
        self.exitosVSFallos["fallos"] = 0
        for estado in self.estados:
            if estado == "exito":
                self.exitosVSFallos["exitos"] = self.exitosVSFallos["exitos"] + 1
            else:
                self.exitosVSFallos["fallos"] = self.exitosVSFallos["fallos"] + 1

    def dibujar_state_codes(self): # Genera la ventana grafica de la grafica
        size = int(math.sqrt(float(len(self.state_codes))))
        data = np.zeros((len(self.state_codes),2)) #Crea una matriz especial para el procesamiento y visualizacion de los datos
        codigos=[]
        for codigo in self.state_codes:
            if type(codigo) != int:
                codigos.append(0)
            else:
                codigos.append(codigo)
        data[:,0] = np.array(range(len(codigos))) #Añade los codigos que se obtuvieron por peticion
        data[:,1] = np.array(codigos)
        linea = PolyLine(data, legend="codigos de estado",colour='red') # Se añaden los parametros para la grafica
        return PlotGraphics([linea],"Resultados", "Peticiones", "codigos")

    def analizar_state_codes(self): # Cuenta la cantidad de incidencias por codigo de estado devuelto por parte del servidor
        codigos = []
        for codigo in self.state_codes:
            if codigo not in codigos:
                codigos.append(codigo)
                self.state_codes_dict[codigo] = 0
            self.state_codes_dict[codigo] = self.state_codes_dict[codigo] + 1
