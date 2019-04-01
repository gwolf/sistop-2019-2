from random import randint
class Proceso:
    def __init__(self,min_tick,max_tick,min_llegada,max_llegada):
        self.color_names = ['\033[31m','\033[32m','\033[33m','\033[34m','\033[36m','\033[37m','\033[91m','\033[92m','\033[93m','\033[94m','\033[95m']
        self.color = self.color_names[randint(0,len(self.color_names)-1)]
        self.nombre = self.color+"["+str(randint(10,99))+"]\033[0m"
        self.t = randint(min_tick,max_tick) # Asigna un tiempo de ejecucion t entre un rango de ticks
        self.llegada = randint(min_llegada,max_llegada) #asigna una llegada aleatoria entre un rango de quantums
    