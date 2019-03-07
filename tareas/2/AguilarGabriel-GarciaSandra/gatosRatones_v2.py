import threading
import random
import time
numeroPlatos = 8 #Indica  el numero de platos
numeroGatos = 8 #Indica la cantidad total de gatos ฅ/ᐠ｡ᆽ｡ᐟ \
numeroRatones = 13 #Indica el total de ratones  ᘛ⁐̤ᕐᐷ
ratones=0 #Indica la cantidad de ratones en el cuarto
debilidadRatones = 0.05 #Esta variable indica la probabilidad de que un raton rompa el pacto de caballeros
gatos=0 #Indica la cantidad de gatos en el cuarto
platos = [threading.Semaphore(1)]*numeroPlatos #Se define un arreglo de semaforos que representa a los platos
hay_gato = threading.Semaphore(1) #Semaforo que indica la presencia de gatos en el cuarto que ademas se utiliza como un Mutex para la variable ratones
hay_raton = threading.Semaphore(1)#Semaforo que indica la presencia de ratones en el cuarto que ademas se utiliza como un Mutex para la variable gatos

def raton(quien): #La funcion Raton recibe el numero de raton para identificarlos
	global ratones
	global debilidadRatones
	global gatos
	veces = random.randint(1,6) #Aqui se asigna el numero de veces que el raton va a comer
	print('Soy el raton', quien, ', voy a comer', veces, 'veces') #El raton indica que se ha iniciado y se identifica con su numero
	for x in range(0,veces):
		if random.random() > debilidadRatones: #Aqui es donde un raton podria romper el pacto de caballeros
			time.sleep(random.random()*2) #Con esto buscamos la concurrencia
			hay_gato.acquire() #Se adquiere el mutex para utilizar la variable ratones que al mismo tiempo indica si hay un ratogato en el cuarto, lo que dejara dormido al raton
			if ratones == 0:
				hay_raton.acquire() #Si es el primer raton en entrar al cuarto utiliza el semaforo para indicar que hay un raton en el cuarto
			ratones += 1#Se actualiza el contador de ratones
			hay_gato.release() #Se libera el mutex
			comer('RATON '+str(quien)) #El raton come (llama a la funcion comer identificado como un raton y con su numero)
			hay_gato.acquire()
			if ratones == 1:
				hay_raton.release()
				print('\nYA NO HAY RATONES\n') #Se indica que ya no hay ratones en el cuarto
			ratones -= 1
			hay_gato.release()
		else:
			hay_raton.acquire()
			if gatos > 0: #Si el raton rompe el pacto de caballeros y hay gatos en el cuarto el raton muere
				time.sleep(random.random()%0.2)
				print('\n*********** Los GATOS se COMIERON al RATON', quien, '***********\n')
				hay_raton.release()
				return 0
			hay_raton.release()

def gato(quien):#La funcion Raton recibe el numero de gato para identificarlos
	global gatos
	veces = random.randint(1,3) #Aqui se asigna el numero de veces que el raton va a comer
	print('Soy el gato', quien, ', voy a comer', veces, 'veces') #El gato indica que se ha iniciado y se identifica con su numero
	for x in range(0,veces):
		time.sleep(random.random()*3) #Con esto buscamos la concurrencia
		hay_raton.acquire() #Se adquiere el mutex para utilizar la variable gatos que al mismo tiempo indica si hay un raton en el cuarto, lo que dejara dormido al gato
		if gatos == 0:
			hay_gato.acquire() #Si es el primer gato en entrar al cuarto utiliza el semaforo para indicar que hay un gato en el cuarto
		gatos += 1 #Se actualiza el contador de gatos
		hay_raton.release() #Se libera el mutex
		comer('GATO '+ str(quien)) #El gato come (llama a la funcion comer identificado como un gato y con su numero)
		hay_raton.acquire()
		if gatos == 1:
			hay_gato.release()
			print('\nYA NO HAY GATOS\n') #Se indica que ya no hay gatos en el cuarto
		gatos -= 1
		hay_raton.release()

def comer(quien):
	global numeroPlatos
	p = random.randint(0, numeroPlatos-1) #El animal que va a comer elige un plato al azar
	platos[p].acquire() #Intenta adquirir el plato pero si ya hay alguien comiendo ahi se duerme hasta que el plato se desocupe
	print('    ', quien, 'esta comiendo en el plato', p, '...')
	time.sleep(random.random()*2) #El tiempo de comida es aleatorio
	print('   El PLATO', p, 'se desocupo')
	platos[p].release() #Se desocupa el plato

for i in range(0,numeroGatos): #Se crea a los gatos
	threading.Thread(target=gato, args=[i]).start()

for i in range(0,numeroRatones): #Se crea a los ratones
	threading.Thread(target=raton, args=[i]).start()