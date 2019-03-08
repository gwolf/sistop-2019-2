#Juarez Aguilar Osmar
#Morales Garcia Luis Angel
#El cruce del rio
import threading
import time
import random

num_desarrolladores = 4
contador_hackers = 0
contador_serfs = 0

mutex_hackers = threading.Semaphore(1)
mutex_serfs = threading.Semaphore(1)
barrera_linux = threading.Semaphore(0)
barrera_windows = threading.Semaphore(0)
sem_balsa = threading.Semaphore(0)
desarrolladores = []
mutex_ctr_desarrolladores = threading.Semaphore(1)

def balsa():
	global contador_hackers
	global contador_serfs
	global num_desarrolladores

	print "La balsa esta en posicion"
	
	while True:
		sem_balsa.acquire()
		mutex_ctr_desarrolladores.acquire()
		if contador_hackers == 4 or contador_serfs == 4:
			print "Abordando a los %d desarrolladores" % num_desarrolladores
			contador_hackers = 0
			contador_serfs = 0
		elif contador_hackers == 2 and contador_serfs == 2:
			print "Abordando a los %d Hackers" % contador_hackers
			print "Abordando a los %d Serfs" % contador_serfs
			contador_hackers = 0
			contador_serfs = 0
		mutex_ctr_desarrolladores.release()

def hacker(nHacker):
	global contador_hackers
	global contador_serfs
	while True:
		#despues de 5 seg aleatoriamente empezaran a llegar desarrolladores LINUX
		time.sleep(5 + random.random())
		print "Soy el hacker %d y estoy vivo" % nHacker
		#llega un desarrollador (hacker)

		mutex_hackers.acquire()
		print "Hacker llegando para entrar a la balsa"
		contador_hackers +=1
		if contador_hackers ==  num_desarrolladores:
			print "Hackers listos para abordar y zarpar"
			for i in range(num_desarrolladores):
				barrera_linux.release()
			sem_balsa.release()
			contador_hackers = 0
		elif contador_hackers + contador_serfs == num_desarrolladores:
			print "Hackers Y Serfs listos para abordar y zarpar"
			for i in range(contador_hackers):
				barrera_linux.release()
			for i in range(contador_serfs):
				barrera_windows.release()
			sem_balsa.release()
			contador_serfs = 0
			contador_hackers = 0
		mutex_hackers.release()
		print "Esperamos a que aborden todos los desarrolladores"
		barrera_linux.acquire()
		barrera_windows.acquire()
		print "Zarpando con todos los desarrolladores abordo"

def serfs(nSerf):
	global contador_serfs
	global contador_hackers
	while True:
		#despues de 5 seg aleatoriamente empezaran a llegar desarrolladores
		time.sleep(5 + random.random())
		print "Soy el Serf %d y estoy vivo" % nSerf
		#llega un desarrollador (serf)

		mutex_serfs.acquire()
		print "Serf llegando para entrar a la balsa"
		contador_serfs +=1
		if contador_serfs ==  num_desarrolladores:
			print "Serfs listos para abordar y zarpar"
			for i in range(num_desarrolladores):
				barrera_windows.release()
			sem_balsa.release()
			contador_serfs = 0
		elif contador_serfs + contador_hackers == num_desarrolladores:
			print "Serfs y Hackers listos para abordar y zarpar"
			for i in range(contador_serfs):
				barrera_windows.release()
			for i in range(contador_hackers):
				barrera_linux.release()
			sem_balsa.release()
			contador_hackers = 0
			contador_serfs = 0
		mutex_serfs.release()
		print "Esperamos a que aborden todos los desarrolladores"
		barrera_linux.acquire()
		barrera_windows.acquire()
		print "Zarpando con todos los desarrolladores abordo"
		
threading.Thread(target=balsa, args = []).start()
for i in range(num_desarrolladores):
	threading.Thread(target = hacker, args = [i]).start()

for i in range(num_desarrolladores):
	threading.Thread(target = serfs, args = [i]).start()
