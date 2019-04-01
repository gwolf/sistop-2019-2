#!/usr/bin/python
import threading
import time
import random
from random import randint

pasajeros_listos = 0
pasajeros_arriba = 10
pasajeros_arriba2 = pasajeros_arriba
arriba = 0
arribaT = 0
prob_bajar = 0.03
nuevos_clientes = 0
num_cliente = 0

sema_conductor = threading.Semaphore(0)
sema_clientes = threading.Semaphore(0)
sema_timbre = threading.Semaphore(1)


def conductor():
	global arriba, arribaT
	print ("Soy el conductor y voy a dormir hasta que llegue más pasaje.")
	while (True):
		sema_conductor.acquire()
		print ("Vamos a comensar la ruta con %d pasajeros..." % arriba)
		break

def clientes(ident):
	global pasajeros_listos, arriba, arribaT
	print ("Soy el pasajero numero %d, y llegue a la base..." % ident)
	pasajeros_listos += 1
	time.sleep(0.3)
	if (pasajeros_listos == pasajeros_arriba):
		print ("\tEl pasajero %d se sube al camion!" % ident)
		arriba += 1
		arribaT += 1
		if(arribaT == pasajeros_arriba):
			sema_conductor.release()
	time.sleep(4)
	bajar(ident)

def bajar(num):
	sema_timbre.acquire()
	if random.random() < 0.5:
		print("El pasajero %d toco el timbre." %num)
		detener_camion(num)
	else:
		sema_timbre.release()
	

def detener_camion(num):
	global arriba
	print("El conductor detiene el camion")
	print("\tEl pasajero %d baja del camión." %num)
	arriba -= 1
	print("\t\tEl viaje continua con %d pasajeros" %arriba)
	sema_timbre.release()


def control():
	global pasajeros_arriba2, num_cliente
	threading.Thread(target=conductor, args=[]).start()
	for i in range(pasajeros_arriba2):
		threading.Thread(target=clientes, args=[num_cliente]).start()
		num_cliente += 1


for paradas in range(4):
	if (paradas < 3):
		print("\n\n######Se encuentra en la parada numero: "+str(paradas+1)+"######")
		control()
		time.sleep(7)
		nuevos_clientes = randint(2,5)
		pasajeros_arriba = pasajeros_arriba + nuevos_clientes
		pasajeros_arriba2 = nuevos_clientes
	else:
		print("\n\n######Se llegó a la base y todos se bajan#######")