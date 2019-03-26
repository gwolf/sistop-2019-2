from threading import Semaphore,Thread
from time import sleep
import random

turista_esp=0
turista_ing=0
lista_turista_esp=Semaphore(0)
lista_turista_ing=Semaphore(0)
total=4
mutex_guia=Semaphore(1)



def esp(num):

	global turista_esp,turista_ing,esCap
	#print("esp %d esperando ..." %num)
	mutex_guia.acquire()
	turista_esp+=1
	print("Turista que habla español %d formado para recorrido" %num)
	if (turista_ing + turista_esp) >=4:
		for i in range(turista_ing):
			lista_turista_ing.release()
		for i in range(turista_esp):
			lista_turista_esp.release()
		turista_ing=0
		turista_esp=0
		print("*** Inicia recorrido")
	
	mutex_guia.release()
	
	lista_turista_esp.acquire()
	

def ing(num):

	global turista_esp,turista_ing, esCap
	#print("ing %d esperando ..." %num)
	mutex_guia.acquire()
	print("Turista que habla inglés %d listo para recorrido" %num)
	turista_esp+=1
	if (turista_ing + turista_esp) >=4:
		for i in range(turista_ing):
			lista_turista_ing.release()
		for i in range(turista_esp):
			lista_turista_esp.release()
		turista_ing=0
		turista_esp=0
		print("*** Inicia recorrido")
	mutex_guia.release()
	
	lista_turista_ing.acquire()

for i in range(20):
	Thread(target=esp, args=[i]).start()

for i in range(60):
	Thread(target=ing, args=[i]).start()