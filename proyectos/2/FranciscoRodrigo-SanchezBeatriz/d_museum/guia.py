import threading
import random
from d_museum.argumentos import args

# Estos son todos los lenguajes que pueden hablar
# los dos actores principales de nuestro museo (guas y turistas)
language = ['español','inglés','alemán','japonés','francés','portugués','italiano','holandés']

class Guia():
    contador = 0
    mis_turistas = []
    """Clase guia que simular a una persona que puede guiar turistas de distintas nacionalidades"""
    def __init__(self, id):
        self.id = id
        # En el problema se definió que los guías solo pueden
        #hablar dos idiomas, por ello usamos la función sample y
        #tomamos dos elementos de la lsita de lenguajes
        self.idiomas = random.sample(language,2)

        print("Soy el guia %d hablo %s y %s" %(self.id,self.idiomas[0],self.idiomas[1]))

# Se generan una lista n guias
mis_guias = []
for j in range(0,args.guias):
    mis_guias.append(Guia(j))
