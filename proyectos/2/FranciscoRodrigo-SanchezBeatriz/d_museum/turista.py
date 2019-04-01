import threading, random
from d_museum.guia import Guia,language,mis_guias
from d_museum.colors import bcolors
from threading import Semaphore

from d_museum.argumentos import args

# Se generan tan mutex como guias
mutex_guias = [Semaphore(1) for i in range(args.guias)]
lista_turistas = [Semaphore(0) for i in range(args.guias)]
# es contador nos servira para ver quien es el ultimo turista # -*- coding: utf-8 -*-
# entrar al museo
contador_turistas= 0
# este mutex protege al contador
mutex_contador= Semaphore(1)

class Turista(threading.Thread):
    def __init__(self,id):
        global contador_turistas
        threading.Thread.__init__(self)
        self.id = id
        self.idioma = random.choice(language)
        #print("Soy turista %d y hablo %s" %(self.id,self.idioma))

    def unGuiaMePuedeAtender(self,idioma):
        """ Esta funcion me dice con que guia tiene que "formarase" mis turistas """
        for index,j in enumerate(mis_guias):
            if j.idiomas[0] ==  idioma or j.idiomas[1] == idioma :
                return index
        return -1

    def run(self):
        global contador_turistas
        mutex_contador.acquire()
        contador_turistas += 1
        mutex_contador.release()

        index = self.unGuiaMePuedeAtender(self.idioma)
        if index == -1:
            print("Soy el turista %d y hablo %s y me voy solo" %(self.id,self.idioma))
        else:
                mutex_guias[index].acquire()
                print(bcolors.WARNING +
                "Soy el turista %d y hablo %s me voy con el guia %d" %(self.id,self.idioma,mis_guias[index].id) +bcolors.ENDC )
                mis_guias[index].contador += 1
                if mis_guias[index].contador == 4:
                    print(bcolors.OKBLUE+"Inicia recorrido guia %d" %mis_guias[index].id + bcolors.ENDC)
                    mis_guias[index].contador = 0
                    # liberando barrera...
                    for i in range(4):
                        lista_turistas[index].release()

                if contador_turistas == args.turistas:
                    for  i in range(0, len(lista_turistas)):
                        for j in range(8):
                            lista_turistas[i].release()
                        if mis_guias[i].contador != 0:
                            print("El guia %d se van con %d turistas" %(mis_guias[i].id,mis_guias[i].contador))

                mutex_guias[index].release()
                lista_turistas[index].acquire()

        if len(mis_guias) == 0:
            print("No hay guias! que mal servicio, me voy solo")
