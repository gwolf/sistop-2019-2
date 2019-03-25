import sys
import ast
class Analisis(object):
    def __init__(self):
        self.times = []
        self.state_codes = []
        self.estados = []
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

    def analizar_state_codes(self):
        codigos = []
        for codigo in self.state_codes:
            if codigo not in codigos:
                codigos.append(codigo)
                self.state_codes_dict[codigo] = 0
            self.state_codes_dict[codigo] = self.state_codes_dict[codigo] + 1