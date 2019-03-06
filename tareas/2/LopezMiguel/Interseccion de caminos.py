#Tarea Semaforos 
from threading import Semaphore,Thread
from time import sleep

Secciones=list()
Semaforos=list()
Mutex = Semaphore(1)
#Creacion de semaforos
for i in range(4):
	Secciones.append(Semaphore(1))
	Semaforos.append(Semaphore(0))
#Autos modelados por threads
# Las variables a,b pertenecen al vector mencionado en el texto, D es la direccion (1,2,3) segun las secciones que vaya a ocupar
def Auto(a,b,D,ID):
	n=(a-b*(1-b))
	Semaforos[n%4].acquire()
	Semaforos[n%4].release()
	Mutex.acquire()
	print('Thread ',ID)
	for i in range(D):
		j=(n-i)%4
		Secciones[j].acquire()
		print("pasando por seccion ",j)
		Secciones[j].release()
	Mutex.release()
#Controlador
def Controlador():
	espera=0.001
	while (1) :
		print("#################### U,D Verde ##################")
		Semaforos[0].release()
		Semaforos[2].release()
		sleep(espera)
		print("#################### U,D Rojo ###################")
		Semaforos[0].acquire()
		Semaforos[2].acquire()
		sleep(espera/2)
		print("#################### L,R Verde ##################")
		Semaforos[1].release()
		Semaforos[3].release()
		sleep(espera)
		print("#################### L,R Rojo ###################")
		Semaforos[1].acquire()
		Semaforos[3].acquire()
		sleep(espera/2)	
	return

num=1000
Controlador = Thread(target=Controlador).start()
#Creacion de "Autos"
for i in range(num):
		#Arriba
		Thread(target=Auto,args=(0,1,2,'U S'+ str(i) )).start()
		Thread(target=Auto,args=(0,1,1,'U R'+ str(i) )).start()
		Thread(target=Auto,args=(0,1,3,'U L'+ str(i) )).start()
		#ABAJO
		num2=num*2
		Thread(target=Auto,args=(0,-1,2,'D S'+str(i) )).start()
		Thread(target=Auto,args=(0,-1,1,'D R'+str(i) )).start()
		Thread(target=Auto,args=(0,-1,3,'D L'+str(i) )).start()
		#DERECHA
		num3=3*num
		Thread(target=Auto,args=(1,0,2,'R S'+str(i) )).start()
		Thread(target=Auto,args=(1,0,1,'R R'+str(i) )).start()
		Thread(target=Auto,args=(1,0,3,'R L'+str(i) )).start()
		#IZQUIERDA
		num4=num*4
		Thread(target=Auto,args=(-1,0,2,'L S'+str(i) )).start()
		Thread(target=Auto,args=(-1,0,1,'L R'+str(i) )).start()		
		Thread(target=Auto,args=(-1,0,3,'L L'+str(i) )).start()	













