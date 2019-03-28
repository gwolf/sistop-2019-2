import threading
import random
from d_museum.lenguajes import language

class Guia():
    contador = 0
    """Clase guia que simular a una persona que puede guiar turistas de distintas nacionalidadesñ"""
    def __init__(self, id):
        self.id = id
        # En el problema se definió que los guías solo pueden
        #hablar dos idiomas, por ello usamos la función sample y
        #tomamos dos elementos de la lsita de lenguajes
        self.idiomas = random.sample(language,2)

        print("Soy el guia %d hablo %s y %s" %(self.id,self.idiomas[0],self.idiomas[1]))

mis_guias = []
# tenemos que ver como quitar ese 5 y hacer
# que el usuario cree n numero de guias
for j in range(0,5):
    mis_guias.append(Guia(j))
