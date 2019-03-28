import threading
import random
from d_museum.lenguajes import language
#import d_museum.var_glob
from d_museum.guia import Guia,mis_guias

from threading import Semaphore

# varibles globales para el controlar nuestra
# implementacion de la primera parte del proyecto
    #turista_esp=0
    #turista_ing=0

lista_turista_esp=Semaphore(0)
lista_turista_ing=Semaphore(0)
total=4
mutex_guia=Semaphore(1)

# Al inicio todos los guias estan dispoibles
# Se los paso por referencia para poderlos sacar
# en caso de quue ya haya la suficiente cantidad de turistas
guias_disponibles = mis_guias
mutex_guias = [Semaphore(1) for i in range(5)]
lista_turistas = [Semaphore(0) for i in range(5)]

class Turista(threading.Thread):
    """Esta es una clase Turista"""
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id = id
        self.idioma = random.choice(language)

    def run(self):
        print("Soy el turista %d y hablo %s" %(self.id,self.idioma))

        #buscar en la lista de guias dispoibles quein habla su idioma y sumarle al contador

        for index,j in enumerate(guias_disponibles):
            if j.idiomas[0] ==  self.idioma or j.idiomas[1] == self.idioma :
                mutex_guias[index].acquire()
                j.contador+=1
                if j.contador==4:
                    #sacarlo de la lista de guias disp
                    del guias_disponibles[index]
                    for i in range(4):
                        lista_turistas[index].release()
                j.contador=0
                print("Inicia recorrido")
                mutex_guias[index].release()
                lista_turistas[index].acquire()
            else :
                print("me voy solo :( ... ")

        if len(guias_disponibles) == 0:
            print("No hay guias! que mal servicio, me voy solo")




        #print("Estoy imprimendo el contador del tercer guia = %d " %mis_guias[2].contador)
