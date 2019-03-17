import threading
import time
import random
from random import randint

num_alu = 5 #numero de bancas disponibles en el salon
i = 1

mutex_alum_dudas = threading.Semaphore(1) #este me ayudara a que solo se haga una pregunta a la vez
señal_profe_alum = threading.Semaphore(0) #señalizar que ha terminado de responder y el otro ha entendido
señal_profe_alum_preg = threading.Semaphore(0) #señalizar que ha terminado de responder y el otro ha entendido

def profe():
    print("Soy el profe y voy a dormir")

def alumno(num):
    dudas = randint(1, 4)  # se selecciona cuantas dudas tendra
    print("El alumno %d entra al salon con %d dudas" % (num, dudas)) # se le asigna id y cantidad de preguntas

    while (dudas > 0):
        time.sleep(0.3)  # este tiempo es para que lleguen mas alumnos

        mutex_alum_dudas.acquire()  # mutex para garantizar un solo alumno preguntando
        control_preguntas(num,dudas)
        dudas -= 1
        mutex_alum_dudas.release()  # libero la opcion de preguntar
        time.sleep(0.3)

def control_preguntas(num,dudas):
    print("\t\tEl alumno %d hace una pregunta..." %num)
    señal_profe_alum_preg.release()#señalizacion

    señal_profe_alum_preg.acquire()#señalizacion
    print("\t\t\t\tEl profe comienza a responder la pregunta %d del alumno %d..." %(dudas, num))
    time.sleep(0.3)
    print("\t\t\t\t\t\tEl profe ha respondido la pregunta %d del alumno %d." % (dudas, num))
    señal_profe_alum.release()#señalizacion

    señal_profe_alum.acquire()#señalizacion
    print("\t\t\t\t\t\t\t\tEl alumno %d ha entendido la pregunta %d.\n" %(num, dudas))

threading.Thread(target=profe, args=[]).start()
while (i <= num_alu):
    time.sleep(0.03)
    if random.random() < 0.03:
        threading.Thread(target=alumno, args=[i]).start()
        i += 1

