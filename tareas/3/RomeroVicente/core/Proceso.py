from random import randint
class Proceso:
    def __init__(self):
        self.nombre = "["+str(randint(10,99))+"]"
        self.t = randint(1,10) # Asigna un tiempo de ejecucion t entre 1 y 10 quantum
        self.llegada = randint(1,20)
    