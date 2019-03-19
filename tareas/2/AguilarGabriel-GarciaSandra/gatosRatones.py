#Importamos librerias necesarias
import threading
import random
import time
#Variables Globales
numeroPlatos = 8 #numero de platos totales
numeroGatos = 8 #numero de gatos totales
numeroRatones = 13 #numero de ratones totales
ratones=0 #contador de ratones
gatos=0 #contador de gatos
#Semaforos
platos = [threading.Semaphore(1)]*numeroPlatos #cada plato sera un semaforo
hay_gato = threading.Semaphore(1) #semaforo que servira como mutex para proteger variables e indicara si hay gatos comiendo
hay_raton = threading.Semaphore(1)#semaforo que servira como mutex para proteger variables e indicara si hay ratones comiendo

def raton(quien):
	global ratones
	print('Soy el raton', quien)
	time.sleep(random.random()*2)
	#Comenzaran a llegar los ratones
	#mutex para proteger el contador de ratones
	#tambien verifica que no hayan gatos comiendo para evitar ser comidos
	hay_gato.acquire()
	#Si es el primer raton avisa que los ratones van a empezar
	#a comer
	if ratones == 0:
		hay_raton.acquire()
	ratones += 1
	hay_gato.release()
	comer('raton '+str(quien))
	#Comenzaran a irse los ratones
	#mutex para proteger contador de ratones
	hay_gato.acquire()
	#Si es el ultimo raton libera el recurso para que los gatos 
	#puedan comer despues
	if ratones == 1:
		hay_raton.release()
		print('\nYA NO HAY RATONES\n')
	ratones -= 1
	hay_gato.release()

def gato(quien):
	global gatos
	print('Soy el gato', quien)
	time.sleep(random.random()*3)
	#Comenzaran a llegar los gatos
	#mutex para proteger contador de gatos
	#Verifica que no haya ratones comiendo
	hay_raton.acquire()
	#Si es el primer gato avisa que los gatos van a empezar a comer
	#toma el recurso y de esa forma los ratones no pueden pasar
	if gatos == 0:
		hay_gato.acquire()
	gatos += 1
	hay_raton.release()
	comer('gato '+ str(quien))
	#Comenzaran a irse los gatos
	#mutex para proteger contador de gatos
	hay_raton.acquire()
	#Si es el ultimo gato libera recurso para que los ratones
	#puedan comer
	if gatos == 1:
		hay_gato.release()
		print('\nYA NO HAY GATOS\n')
	gatos -= 1
	
	hay_raton.release()

def comer(quien):
	global numeroPlatos
	#Numero al azar para escoger un plato
	p = random.randint(0, numeroPlatos-1)
	#Toma el plato del numero anterior
	platos[p].acquire()
	print(quien, 'esta comiendo en el plato', p, '...')
	#Tiempo para comer
	time.sleep(0.3)
	print('El plato', p, 'se desocupo')
	#Liberamos el plato para que alguien mas coma
	platos[p].release()

#Creacion y lanzamiento de hilos
for i in range(0,numeroRatones):
	threading.Thread(target=raton, args=[i]).start()

for i in range(0,numeroGatos):
	threading.Thread(target=gato, args=[i]).start()

