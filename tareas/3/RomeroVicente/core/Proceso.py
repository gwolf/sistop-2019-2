from random import randint
class Proceso:
    def __init__(self,min_tick,max_tick,min_llegada,max_llegada):
        self.nombre = "["+str(randint(10,99))+"]"
        self.t = randint(min_tick,max_tick) # Asigna un tiempo de ejecucion t entre un rango de ticks
        self.llegada = randint(min_llegada,max_llegada) #asigna una llegada aleatoria entre un rango de quantums
    