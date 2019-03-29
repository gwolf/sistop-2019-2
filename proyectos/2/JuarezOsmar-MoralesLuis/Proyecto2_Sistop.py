#Juarez Aguilar Osmar
#Morales Garcia Luis Angel
#Proyecto 2
#from tkinter import *
import threading
import time
import random
from random import randint

num_compradores_por_turno = 10
contador_compradores = 0
contador_compradorOnline = 0
contador_compradorFisico = 0
num_boletos = 20

mutex_compradoresOnline = threading.Semaphore(1)
mutex_compradoresFisico = threading.Semaphore(1)
barrera_Online = threading.Semaphore(0)
barrera_Fisico = threading.Semaphore(0)
sem_compraBoleto = threading.Semaphore(0)
#desarrolladores = []
mutex_ctr_compradores = threading.Semaphore(1)

def compraBoleto():
	global contador_compradores
	global contador_compradorOnline
	global contador_compradorFisico
	global num_compradores_por_turno
	global num_boletos
	print "La compra se esta realizando"
	while contador_compradores > 0:
		sem_compraBoleto.acquire()
		mutex_ctr_compradores.acquire()
		if num_boletos==0:
			print "LO SENTIMOS, LOS BOLETOS SE HAN AGOTADO :( "
			break
		if contador_compradorOnline > 0:
			print "Ingresando al sistema el comprador %d " % num_compradores_por_turno
			contador_compradores = contador_compradores - 1
			num_boletos = num_boletos -1
			totalPersonas= totalPersonas-1
		elif contador_compradorFisico > 0:
			print "Ingresando al sistema el comprador %d " % num_compradores_por_turno
			contador_compradores = contador_compradores - 1
			num_boletos = num_boletos -1
			totalPersonas = totalPersonas-1
		mutex_ctr_compradores.release()
	print "COMPRA REALIZADA CON EXITO"



def compradorOnline(nOnline):
	global contador_compradorOnline
	global contador_compradorFisico
	while True:
		#despues de 5 seg aleatoriamente empezaran a entrar al sistema de boletos personas 
		time.sleep(5 + random.random())
		print "La persona %d entra al sistema online" % contador_compradorOnline
		#Entra al sistema online una persona

		contador_compradorOnline +=1
		mutex_compradoresOnline.acquire()
		print "Una personna en el sistema online lista para realizar su compra"
		#En el primer caso se considera que entraron 10 compradores al sistema online  
		if contador_compradorOnline ==  num_compradores_por_turno:
			print "La compra esta lista para realizarse desde el sistema online"
			for i in range(num_compradores_por_turno):
				barrera_Online.release()
			sem_compraBoleto.release()
			compraBoleto()
			contador_compradorOnline = 0
		#En este segundo caso se considera que al realizar la compra en el sistema online hay n personas comprando en este sistema online
		#pero al mismo tiempo se encuentran n personas comprando el boleto en la tienda fisicamente por lo que si la suma de esas n personas
		#que quieren comprar el boleto es igual al numero de personas admitidas por el sistema se realiza la compra.
		elif contador_compradorOnline + contador_compradorFisico == num_compradores_por_turno:
			print "Personas en el sistema online y en la tienda listas para realizar su compra"
			for i in range(contador_compradorOnline):
				barrera_Fisico.release()
				#compraBoleto()
			for i in range(contador_compradorFisico):
				barrera_Online.release()
				#compraBoleto()
			sem_compraBoleto.release()
			compraBoleto()
			contador_compradorFisico = 0
			contador_compradorOnline = 0
		elif num_boletos==0:
			print "BOLETOS AGOTADOS"
			break
		mutex_compradoresOnline.release()
		##print "Esperamos a que entren todas las personas al sistema"
		barrera_Online.acquire()
		barrera_Fisico.acquire()
		print "Realizando la compra de boletos las personas admitidas por el sistema"

def compradorFisico(nPersonaFisico):
	global contador_compradorOnline
	global contador_compradorFisico
	while True:
		#despues de 5 seg aleatoriamente empezaran a llegar personas a la tienda fisicamnte a comprar su boleto
		time.sleep(5 + random.random())
		print "la persona %d llega a la tienda fisicamnte a comprar su boleto" % contador_compradorFisico

		contador_compradorFisico +=1
		mutex_compradoresFisico.acquire()
		print "La persona se ha formado en la tienda fisicamente"
		#Este primer caso considera que 10 personas admitidas por el sistema estan en la tienda fisicamente para comprar el boleto
		#por lo que ninguna persona lo esta comprando en el sistema onliene 
		if contador_compradorFisico ==  num_compradores_por_turno:
			print "Personas en la tienda en fisico listos para comprar su boleto"
			for i in range(num_compradores_por_turno):
				barrera_Online.release()
			sem_compraBoleto.release()
			compraBoleto()
			contador_compradorFisico = 0
		#Segundo caso es que hay personas tanto en el sistema online como en la tienda en fisico para comprar sus boletos
		elif contador_compradorFisico + contador_compradorOnline == num_compradores_por_turno:
			print "Personas en la tienda fisicamente y en el sistema online listas para comrpar su boleto"
			for i in range(contador_compradorFisico):
				barrera_Online.release()
				#compraBoleto()
			for i in range(contador_compradorOnline):
				barrera_Fisico.release()
				#compraBoleto()
			sem_compraBoleto.release()
			compraBoleto()
			contador_compradorOnline = 0
			contador_compradorFisico = 0
		elif num_boletos==0:
			print "BOLETOS AGOTADOS"
			break
		mutex_compradoresFisico.release()
		#print "Esperamos a que entren todas las personas al sistema"
		barrera_Fisico.acquire()
		barrera_Online.acquire()
		print "Realizando la compra de boletos las personas admitidas por el sistema"
	
totalPersonas = randint(19, 29)
print (totalPersonas)
for i in range(totalPersonas):
    threading.Thread(target = compradorOnline, args = [i]).start()
    threading.Thread(target = compradorFisico, args = [i]).start()
