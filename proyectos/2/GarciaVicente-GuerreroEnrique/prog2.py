# -*- Encoding: utf-8 -*-
from variables import * #Se importa la informacion del archivo variables.py donde esta definido el valor de pasajeros minimos y el numero de paradas
import turtle
from tkinter import PhotoImage
import threading
import time
import random
from random import randint

# !/usr/bin/python
num_paradas = numeroparadas # para indicar el numero de paradas
pasajeros_listos = 0 #numero de pasajeros que ya estan a bordo
pasajeros_arriba = numeropasajeros #asignacion de oasajeros minimos requeridos para iniciar el viaje
pasajeros_arriba2 = pasajeros_arriba #esta asignacion nos ayudara a saber cuantos pasajeros has subido en total
arriba = 0 #contador
arribaT = 0 #contador total
prob_bajar = 0.03 #probabilidad para decidir si un pasajero baja o no
nuevos_clientes = 0 #numero de clientes nuevos en cada base
num_cliente = 0 #variable que nos ayudara a crear los nuevos hilos de pasajeros
bajados = 0

#Definicion de hilos
sema_conductor = threading.Semaphore(0)
sema_clientes = threading.Semaphore(0)
sema_timbre = threading.Semaphore(1)

# Elementos graficos
ancho_ventana = (num_paradas * 150) + 400 #en pixeles
alto_ventana = 600 #en pixeles
ventana = turtle.Screen()
ventana.setup(width = ancho_ventana, height = alto_ventana)

#Procesamiento de imagenes a utilizar para la interfaz grafica
img_tam3 = PhotoImage(file = "bus-stop-color.png").subsample(3,3)
ventana.addshape("img_tam3",turtle.Shape("image", img_tam3))
img_parada_col = turtle.Turtle("img_tam3")

img_tam1 = PhotoImage(file = "bus1.png").subsample(3,3)
ventana.addshape("img_tam",turtle.Shape("image", img_tam1))
bus1 = turtle.Turtle("img_tam")

img_tam2 = PhotoImage(file = "bus-stop-bco.png").subsample(4,4)
ventana.addshape("img_tam2",turtle.Shape("image", img_tam2))
img_parada_bn = turtle.Turtle("img_tam2")

texto = turtle.Turtle()
texto.hideturtle()
texto.penup()
texto.sety(-250)

#Definición de funciones
def conductor():
    global arriba, arribaT
    print("Soy el conductor y voy a dormir hasta que llegue más pasaje.")
    while (True):
        sema_conductor.acquire() #El conductor estará parado hasta que todos los pasajeros necesarios esten arriba
        print("Vamos a comenzar la ruta con %d pasajeros..." % arriba)
        break

def clientes(ident):
    global pasajeros_listos, arriba, arribaT
    print("Soy el pasajero numero %d, y llegue a la base..." % ident) #mostrará que pasajero llega a la base
    pasajeros_listos += 1 #contador de cuantos pasajeros están en la base
    time.sleep(0.3) #tiempo de espera
    if (pasajeros_listos == pasajeros_arriba): #comparación para determinar siya se crearon todos los clientes
        print("\tEl pasajero %d se sube al camion!" % ident) #se indica que cliente se sube al camión
        arriba += 1 #contador para saber cuantos pasajeros ya están a bordo
        arribaT += 1 #contador para saber cuantos pasajeros han subido en total
        if (arribaT == pasajeros_arriba): #comparacion para determinar si el camion puede avanzar
            sema_conductor.release()  #activa al conductor para iniciar viaje
    time.sleep(4)
    bajar(ident) # se manda al cliente ya arriba para ver si será seleccionado para bajar

def bajar(num): #recibe el identificador de el cliente
    sema_timbre.acquire() #bloqueo para asi garantizar que solo una persona bajara al mismo tiempo
    if random.random() < 0.5: #decisión para saber si el pasajero bajara o no
        print("El pasajero %d tocó el timbre." % num)
        detener_camion(num) #activa la función de detener camión
    else:
        sema_timbre.release() #reactiva la funcion timbre para el siguiente cliente


def detener_camion(num):
    global arriba,bajados
    print("El conductor detiene el camion")
    print("\tEl pasajero %d baja del camión." % num) #indica que pasajero es el que se baja
    arriba -= 1 #se disminuye la cantidad de pasajeros a bordo
    bajados += 1 #variables para saber cuantos bajan
    print("\t\tEl viaje continua con %d pasajeros" % arriba) #se indica cuantos pasajeros a un hay
    sema_timbre.release() #se activa la funcion timbre para el siguiente cliente


def control():
    global pasajeros_arriba2, num_cliente #variables globales para saber cuantos clientes crear
    threading.Thread(target=conductor, args=[]).start() #creación de hilo conductor
    for i in range(pasajeros_arriba2): 
        threading.Thread(target=clientes, args=[num_cliente]).start() #creación de hilos para clientes
        num_cliente += 1 #actualizador de target para cliente

img_parada_col.speed(0)
img_parada_col.penup()
img_parada_col.goto(-(ancho_ventana / 2) + 200, 75)
img_parada_col.stamp()

img_parada_bn.hideturtle()
img_parada_bn.speed(0)
img_parada_bn.penup()
img_parada_bn.goto(-(ancho_ventana / 2) + 200, 75)

bus1.speed(1)
bus1.up()
bus1.goto(-(ancho_ventana / 2) + 200, 0)
bus1.dot()
time.sleep(2.5)

for paradas in range(num_paradas+1):
    
    if (paradas < num_paradas):

        print("\n\n######Se encuentra en la parada numero: " + str(paradas + 1) + "######")
        if(paradas >0):
            img_parada_bn.showturtle()
            img_parada_bn.penup()
            img_parada_bn.speed(0)
            img_parada_bn.forward(150)
            img_parada_bn.stamp()


            img_parada_col.hideturtle()
            img_parada_col.penup()
            img_parada_col.speed(0)
            img_parada_col.forward(150)

            bus1.pendown()
            bus1.speed(1)
            bus1.forward(150)

            texto.clear()
            texto.write("De la parada " + str(paradas) + " a la parada " + str(paradas+1) + " se bajaron " + str(bajados) + " pasajeros")
            bajados = 0
            bus1.dot()

        control()
        time.sleep(7)
        nuevos_clientes = randint(2, 5)
        pasajeros_arriba = pasajeros_arriba + nuevos_clientes
        pasajeros_arriba2 = nuevos_clientes

    else:
        print("\n\n######  Se llegó a la base y todos se bajan   #######")
        texto.clear()
        texto.write("De la parada " + str(paradas) + " a la parada " + str(paradas+1) + " se bajaron " + str(bajados) + " pasajeros")
        img_parada_col.speed(0)
        img_parada_col.showturtle()
        img_parada_col.forward(150)
        bus1.forward(150)
        ventana.exitonclick()
