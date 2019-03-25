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
        self.exitosVSFallos = {"exitos":0,"fallos":0}
        self.state_codes_dict = {}

    def analizar_tiempo(self):
        self.tiempo_promedio = 0
        for segundos in self.times:
            self.tiempo_promedio = self.tiempo_promedio + segundos
        self.tiempo_promedio = self.tiempo_promedio / len(self.times)

    def analizar_estados(self):
        self.exitosVSFallos["exitos"] = 0
        self.exitosVSFallos["fallos"] = 0
        for estado in self.estados:
            if estado == "exito":
                self.exitosVSFallos["exitos"] = self.exitosVSFallos["exitos"] + 1
            else:
                self.exitosVSFallos["fallos"] = self.exitosVSFallos["fallos"] + 1

    def dibujar_state_codes(self):
        size = int(math.sqrt(float(len(self.state_codes))))
        data = np.zeros((len(self.state_codes),2))
        codigos=[]
        for codigo in self.state_codes:
            if type(codigo) != int:
                codigos.append(0)
            else:
                codigos.append(codigo)
        data[:,0] = np.array(range(len(codigos)))
        data[:,1] = np.array(codigos)
        linea = PolyLine(data, legend="codigos de estado",colour='red')
        return PlotGraphics([linea],"Resultados", "Tiempo", "codigo")
        #plt.matshow(imagen)
        #plt.show()
        #plt.close()

    def analizar_state_codes(self):
        codigos = []
        for codigo in self.state_codes:
            if codigo not in codigos:
                codigos.append(codigo)
                self.state_codes_dict[codigo] = 0
            self.state_codes_dict[codigo] = self.state_codes_dict[codigo] + 1
