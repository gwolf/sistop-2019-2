#Autores: Gonzalez Zepeda Felix & Guzman Marin Yared
#Version 3.7 Python
#Ejercicio El cruce del rio

from threading import Semaphore, Thread # Usamos threading para manejar hilos, Semaphore para usar mutex y colas.
from time import sleep #Usamos sleep para generar un retraso cada que la balza avance

#Utilizado para declarar cada variable
tripulantes = 0
num_H = 0 
num_S = 0
#Se utiliza Queue = cola para contabilizar pasjeros
QueueHackers = Semaphore(0) 
QueueSerfs = Semaphore(0)
#Mutex para crear el bloque del contador y el bote
mutex = Semaphore(1) 
mutexBote = Semaphore(1) 

#Se define la estructura de lo que hara hackers
def hackers(): 
    global num_H
    global num_S
    mutex.acquire()
    num_H += 1
    if num_H == 4: 
        QueueHackers.release() 
        QueueHackers.release()
        QueueHackers.release()
        num_H -= 4 
        mutex.release() 
        suben("Hacker") 
        
    elif (num_H == 2 and num_S ==2): 
        QueueHackers.release() 
        QueueSerfs.release()
        QueueSerfs.release()
        num_H -= 2 
        num_S -= 2
        mutex.release()  
        suben("Hacker") 
    else:
        
        mutex.release() 
        QueueHackers.acquire() 
        suben("Hacker") 

#Se define la estructura de lo que hara serf
def serfs():
    global num_S     #Declarando variables
    global num_H
    mutex.acquire() 
    num_S += 1       #Contador para hackers
    
    if num_S == 4:
        QueueSerfs.release()   #Hilos maximos para la cola de serfs
        QueueSerfs.release()
        QueueSerfs.release()
        num_S -= 4            #Se llega al numero maximo de hackers permitido en el bote
        mutex.release()       #Se libera mutex
        suben("Serf")
    elif (num_H == 2 and num_S == 2):   
        QueueHackers.release() #Se llega a un 50% de Hackers y 50% de Serfs
        QueueHackers.release()
        QueueSerfs.release()
        num_H -= 2
        num_S -= 2
        mutex.release()
        suben("Serf")
    else:
        mutex.release()
        QueueSerfs.acquire()  #Se ocupa un lugar en la fila
        suben("Serf")

def suben(yo):             #Estructura para la funcion de subir al bote
    global tripulantes     
    mutexBote.acquire()
    tripulantes += 1       #Se usa contador de tripulantes que subiran al bote
    print("Soy un "+yo+" y estoy listo") #Se hace el llamado al tripulante que va a subir
    if tripulantes == 4:  #Verifica que se cumpla la regla de cuatro tripulates en el bote que es el tope
        avanza()
        tripulantes = 0
    mutexBote.release()  #Mutex para proteger la variable tripulantes

 #Despliega mensaje una vez que todos los miembros de la tripulacion estan a bordo 
def avanza():
    print("--¿Estan listos?--")
    sleep(1)
 
for i in range(16):
    Thread(target = hackers, args = []).start()
    Thread(target = hackers, args = []).start()
    Thread(target = serfs, args = []).start()
