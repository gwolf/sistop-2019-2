import threading
import time 
import random

mutexA = threading.Semaphore(1)
mutexB = threading.Semaphore(1)
mutexC = threading.Semaphore(1)
colaA = []
colaB = []
colaC = []
colaGeneral = []


def imprimir():
    print("-------------------")
    print (colaGeneral)
    print (colaA)
    print (colaB)
    print (colaC)
    print("-------------------")

def cliente(numCliente):
    time.sleep(random.randrange(5))
    colaGeneral.append(numCliente)
    print ("Ah llegado el cliente %d" %numCliente)
    operacionBancaria(numCliente) 

def operacionBancaria(numCliente):
    if (len(colaA) < len(colaB) and len(colaA) < len(colaC) or len(colaA) == 0):
        mutexA.acquire()
        print ("El cliente %d sera atendido en la caja 1"%numCliente)
        num = buscarElemento(colaGeneral, numCliente)
        colaGeneral.pop(num)
        colaA.append(numCliente)
        imprimir()
        operacion(numCliente)
        colaA.pop()
        print ("El cliente %d ha terminado y se retira" %numCliente)
        mutexA.release()
    elif (len(colaB) < len(colaA) and len(colaB) < len(colaC) or len(colaB) == 0):
        mutexB.acquire()
        print ("El cliente %d sera atendido en la caja 2"%numCliente)
        num = buscarElemento(colaGeneral, numCliente)
        colaGeneral.pop(num)
        colaB.append(numCliente)
        imprimir()
        operacion(numCliente)
        colaB.pop()
        print ("El cliente %d ha terminado y se retira" %numCliente)
        mutexB.release()
    elif (len(colaC) < len(colaA) and len(colaC) < len(colaB) or len(colaC) == 0):
        mutexC.acquire()
        print ("El cliente %d sera atendido en la caja 3"%numCliente)
        num = buscarElemento(colaGeneral, numCliente)
        colaGeneral.pop(num)
        colaC.append(numCliente)
        imprimir()
        operacion(numCliente)
        colaC.pop()
        print ("El cliente %d ha terminado y se retira" %numCliente)
        mutexC.release()
    elif (len(colaA) == len(colaB) and len(colaB) == len(colaC)):
        print ("Soy el cliente %d y dare una vuelta, espero que no me ganen" %numCliente)      
        time.sleep(1)
        operacionBancaria(numCliente)
          


def operacion(numCliente):
    time.sleep(random.randrange(5))
    

def lanza_cliente(numCliente):
    threading.Thread(target=cliente, args=[numCliente]).start()

def buscarElemento(lista, elemento):
    for i in range(0,len(lista)):
        if(lista[i] == elemento):
            return i

for i in range(7):
        threading.Thread(target=cliente, args=[i]).start()
