#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import threading
import time

#En esta variable se define en numero de peces que puede haber por cada corriente
pecesPorCorriente=2
#Se definen los multiplex que nos permiten controlar el flujo en cada direccion
multiplexReloj = threading.BoundedSemaphore(pecesPorCorriente)
multiplexContrareloj = threading.BoundedSemaphore(pecesPorCorriente)

def esSeguroIrAReloj():
    if (numPecesContrareloj - (numPecesReloj + 1)) == 0:
        return False
    return True

def esSeguroIrAContrareloj():
    if (numPecesReloj - (numPecesContrareloj + 1)) == 0:
        return False
    return True

#Estas variables nos permiten calcular si es seguro cruzar o no. 
numPecesReloj = 0
numPecesContrareloj = 0
mutexAReloj = threading.BoundedSemaphore(0)
mutexContrareloj = threading.BoundedSemaphore(0)
cruzarAReloj = esSeguroIrAReloj()
cruzarAContraReloj = esSeguroIrAContrareloj()

def elegirDireccion():
        if random.random() < 0.5:
            #1 es en sentido del reloj
            return 1
        else:
            #0 es en sentido contrareloj
            return 0

AReloj=set()
AContrareloj = set()
Centro = set()
class Pez():
    
    def __init__(self, nombre):
        global numPecesContrareloj
        global numPecesReloj
        

        self.nombre = nombre
        self.direccionActual = -1
        #print(self.nombre + " está en espera")
        self.isWaiting = True
        Centro.add(self)

    def __str__(self):
        direccion =  "de sentido del reloj" if self.direccionActual == 1 else "contra reloj"
        return self.nombre + " está nadando " + direccion
    

    def nadar(self):
        global numPecesContrareloj
        global numPecesReloj
        global cruzarAContraReloj
        global cruzarAReloj
        """mutexAReloj.acquire()
        cruzarAReloj = esSeguroIrAReloj()
        mutexAReloj.release()

        mutexAReloj.acquire()
        cruzarAContraReloj = esSeguroIrAContrareloj()
        mutexAReloj.release()"""

        iteracion = 1
        while(True):
            nuevaDireccion = elegirDireccion()
            if nuevaDireccion == self.direccionActual:
                tmp =  "de sentido del reloj" if self.direccionActual == 1 else "contra reloj"
                #print(self.nombre+" va a seguir nadando "+tmp)
                continue
            if self.isWaiting:
                Centro.remove(self)
                if nuevaDireccion == 1 and iteracion == 1 and cruzarAReloj:
                     #Quiere decir que la corriente en la que estaba era contrareloj
                    multiplexReloj.acquire()
                    AReloj.add(self)
                    self.direccionActual = 1
                    self.isWaiting = False
                    numPecesReloj+=1
                    #print(self)
                    continue   
                elif nuevaDireccion  == 0 and iteracion == 1 and cruzarAContraReloj:
                    multiplexContrareloj.acquire()
                    AContrareloj.add(self)
                    self.direccionActual = 0
                    self.isWaiting = False
                    numPecesContrareloj+=1
                    #print(self)
                    continue

                if nuevaDireccion == 1:
                    #Quiere decir que la corriente en la que estaba era contrareloj
                    multiplexContrareloj.release()
                    AContrareloj.remove(self)

                elif nuevaDireccion  == 0:
                    multiplexReloj.release()
                    AReloj.remove(self)  


                if nuevaDireccion == 1 and cruzarAReloj:# and numPecesReloj < pecesPorCorriente and (numPecesContrareloj - numPecesReloj) >= 1:
                     #Quiere decir que la corriente en la que estaba era contrareloj
                    multiplexReloj.acquire()
                    AReloj.add(self)
                    self.direccionActual = 1
                    self.isWaiting = False
                    numPecesReloj+=1
                    numPecesContrareloj -= 1
                    #print(self)

                elif nuevaDireccion  == 0 and  cruzarAReloj:#and numPecesContrareloj < pecesPorCorriente and (numPecesReloj - numPecesContrareloj) >= 1:
                    multiplexContrareloj.acquire()
                    AContrareloj.add(self)
                    self.direccionActual = 0
                    self.isWaiting = False
                    numPecesContrareloj+=1
                    numPecesReloj -= 1
                    #print(self)
                else:
                    Centro.add(self)
                    self.isWaiting = True
                    #print(self.nombre+" va a esperar en el centro de la pecera")
    
            elif not self.isWaiting:
                Centro.add(self)
                self.isWaiting  = True
                #print(self.nombre+" está en el centro de la pecera.")
            
            iteracion += 1
            time.sleep(5)
            
                
def getStatus():
    while(True):
        string="************************************\n"
        string += "Peces circulando a reloj[ " + "*"*len(AReloj)+" ]\n"
        for pez in AReloj:
            string += "><((( °-° ) : "+pez.nombre+"\n"
        string += "Peces circulando en contrareloj[ " + "*"*len(AContrareloj)+" ]\n\n"
        for pez in AContrareloj:
            string += "      ( °-° )))>< : "+pez.nombre+"\n"
        time.sleep(5)
        print(string)

def main():
    nemo = Pez("Nemo")
    marlin = Pez("Marlin")
    dory = Pez("Dory")
    bruce = Pez("Bruce")
    chiqui = Pez("Chiqui")
    crush = Pez("Crush")
    jacques = Pez("Jacques")
    peces=[nemo, dory, marlin, bruce, chiqui, crush, jacques]
    print("*"*30)
    hilos = []
    hilos.append(threading.Thread(target=getStatus))

    for pez in peces:
        hilo = threading.Thread(target=pez.nadar)
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()


if __name__ =="__main__":
    main()