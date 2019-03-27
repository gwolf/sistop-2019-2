import threading
import random
from d_museum.lenguajes import language

class Guia(threading.Thread):
    """Clase guia que simular a una persona que puede guiar turistas de distintas nacionalidadesñ"""
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
        # En el problema se definió que los guías solo pueden hablar dos idiomas, por ello usamos la función sample y tomamos dos elementos de la lsita de lenguajes
        self.idiomas = random.sample(language,2)

    def run(self):
        print("Soy el guia %d hablo %s y %s" %(self.id,self.idiomas[0],self.idiomas[1]))
