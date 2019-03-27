import threading
import random
from d_museum.lenguajes import language
class Turista(threading.Thread):
    """Esta es una clase Turista"""
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id = id
        self.idioma = random.choice(language)
    def run(self):
        print("Soy el turista %d y hablo %s" %(self.id,self.idioma))
