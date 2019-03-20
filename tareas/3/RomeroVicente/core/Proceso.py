from random import randint
class Proceso:
    def __init__(self):
        self.nombre = "["+str(randint(10,99))+"]"
        self.t = randint(320,800) # Asigna un tiempo de ejecucion t entre 160 y 800 ticks
        self.llegada = randint(1,20)
    