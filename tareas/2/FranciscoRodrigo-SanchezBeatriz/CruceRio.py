from threading import Semaphore,Thread
from time import sleep
import random

hackers=0
serfs=0
lista_hackeres=Semaphore(0)
lista_serfs=Semaphore(0)
total=4
mutex_balsa=Semaphore(1)



def hacker(num):

	global hackers,serfs,esCap
	#print("hacker %d esperando ..." %num)
	mutex_balsa.acquire()
	hackers+=1
	print("hacker %d subiendo a la balsa" %num)
	if hackers == 4:
		for i in range(total):
			lista_hackeres.release()
		hackers=0
		print("*** Zarpando  la balsa")
	elif serfs >= 2 and hackers==2:
		for i in range(2):
			lista_hackeres.release()
			lista_serfs.release()
		serfs-=2
		hackers=0
		print("*** Zarpando la balsa")
	
	mutex_balsa.release()
	
	lista_hackeres.acquire()
	

def serf(num):

	global hackers,serfs, esCap
	#print("serf %d esperando ..." %num)
	mutex_balsa.acquire()
	print("serf %d subiendo a la balsa" %num)
	serfs+=1
	if serfs == 4:
		for i in range(total):
			lista_serfs.release()
		serfs=0
		print("*** Zarpando a la balsa")
	elif hackers >= 2 and serfs==2:
		for i in range(2):
			lista_serfs.release()
			lista_hackeres.release()
		hackers-=2
		serfs=0
		print("*** Zarpando a la balsa" )
	mutex_balsa.release()
	
	lista_serfs.acquire()
	


for i in range(10):
	Thread(target=hacker, args=[i]).start()

for i in range(10):
	Thread(target=serf, args=[i]).start()