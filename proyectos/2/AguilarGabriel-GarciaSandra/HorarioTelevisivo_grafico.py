from tkinter import *
import os
from PIL import Image, ImageTk
import threading
import random
import time

def Programa():
	global numeroTeles
	global numeroIntegrantes
	global telesGrafo

	#Obtencion variables de entrada
	StrTelevisiones=teleEnt.get()
	StrIntegrantes=intEnt.get()

	numeroTeles=int(StrTelevisiones)
	numeroIntegrantes=int(StrIntegrantes)

	pasillo = threading.Semaphore(numeroTeles)

	entrada.pack_forget()

	desarrollo=Frame(ventana, bg="#33D4AE")
	desarrollo.pack(padx=1, pady=40, fill=BOTH, expand=1)
	desarrollo.config(width=480,height=600)


	desarrollo.columnconfigure(numeroTeles-1,weight=1)
	desarrollo.rowconfigure(3, weight=1)

	mensaje = Label(desarrollo, text="mensajes al usuario", fg="green",
	font=("Verdana", 15),borderwidth=2, relief="sunken")

	#Definicion de etiquetas que simulan la television
	
	
	for i in range(0,numeroTeles):
		teLb=Label(desarrollo,bg="black",fg="white")
		teLb.grid(row=1,column=i,sticky="nsew",padx=10, pady=10)
		teLb['text']="Canal: "+teles
		desarrollo.columnconfigure(i,weight=1)

	

	espera=Label(desarrollo,text="",font=("Verdana", 15))
	users=Label(desarrollo, text="Integrantes en espera",font=("Verdana", 15))

	#Conficugracines grid
	espera['text']=numeroIntegrantes
	mensaje.grid(row=0, column=0, columnspan=numeroTeles)
	espera.grid(row=2, column=0, columnspan=numeroTeles,sticky="s")
	users.grid(row=3, column=0, columnspan=numeroTeles)
	desarrollo.rowconfigure(0,weight=1)
	desarrollo.rowconfigure(1,weight=2)
	desarrollo.rowconfigure(2,weight=1)
	desarrollo.rowconfigure(3,weight=1)


	generarProgramacion()
	for i in range(0,numeroIntegrantes): #Se crea a los usuarios
		threading.Thread(target=Usuario, args=[i]).start()
	threading.Thread(target=padreTiempo).start()



def impresion():
	global tiempo
	global teles
	global numeroTeles
	global telesGrafo

	for i in range(0, numeroTeles):
		teLb.insert(0,"pureb")


def padreTiempo():
	global tiempo
	global tiempoMax
	continuar = True
	print('Inicia simulacion')
	while continuar:
		queHoraEs.acquire()
		ActualizarTeles()
		if tiempo < tiempoMax+20:
			tiempo += 1
		else:
			continuar = False
		queHoraEs.release()
		print(tiempo)
		time.sleep(0.5)
	return 'Fin simulacion'

def ActualizarTeles():
	global tiempo
	global programas
	global teles
	global TelesEnUso
	global numeroTeles
	for i in range(0,numeroTeles-1):
		if TelesEnUso[i] == 1:
			canal = teles[i][0]
			programa = teles[i][1]
			#queHoraEs.acquire()
			if programas[canal][programa][2] == tiempo:
				for x in range(1,len(teles[2])):
					control[i].release()
				pasillo.release()
			else:
				for x in  programas[canal][programa][1]:
					if x == tiempo:
						for x in range(1,len(teles[2])):
							control[i].release()
						pasillo.release()
			#queHoraEs.release()
	Programa()
	print('En uso:', TelesEnUso, '\nTeles:', teles)#-/**********


def Usuario(who):
	global canales
	global programas
	global tiempo
	global teles

	global TelesEnUso
	canal = random.randint(0,len(canales)-1)
	programa = random.randint(0,len(programas[canal])-1)
	otroPrograma = random.random() % 0.1
	print('Usuario:', str(who), '; quiero ver:', canal, programa, 'que empieza en', programas[canal][programa][0], 'y termina en', programas[canal][programa][2])
	time.sleep(0.1)
	queHoraEs.acquire()
	tiempoAux = tiempo
	#print('checkpoint1 usuarioTiempo')
	queHoraEs.release()
	while programas[canal][programa][0] > tiempoAux:
		queHoraEs.acquire()
		tiempoAux = tiempo
		#print('checkpoint1 usuarioTiempo')
		queHoraEs.release()
	while programas[canal][programa][2] > tiempoAux:
		#print('checkpoint2 usuarioWhile')
		print('soy usuario', str(who), 'estoy en el pasillo esperando')
		pasillo.acquire()
		queHoraEs.acquire()
		tiempoAux = tiempo
		queHoraEs.release()
		if programas[canal][programa][2] > tiempoAux:
			print('soy usuario', str(who), 'busco una tele')
			tomarTele.acquire()
			for x in range(0,len(TelesEnUso)-1):
				if TelesEnUso[x] == 1 and teles[x][0] == canal and teles[x][1] == programa:
					teles[x][2].append(who)
					lugar = x
					compartiendo = True
					#tomarTele.release()
				else:
					compartiendo = False
			if not compartiendo:
				#tomarTele.acquire()
				lugar = TelesEnUso.index(0)
				TelesEnUso[lugar] = 1
				teles[lugar] = [canal, programa, [who]]
			tomarTele.release()
			control[lugar].acquire()
			print('Usuario', str(who), 'Dejo la tele', lugar)
			tomarTele.acquire()
			TelesEnUso[lugar] = 0
			teles[lugar][2].remove(who)
			tomarTele.release()
		#pasillo.release()
		queHoraEs.acquire()
		tiempoAux = tiempo
		queHoraEs.release()
	print('\n\t-----------Usuario', str(who), 'El programa que queria ver termino-----------')
	if random.random() <= otroPrograma:
		Usuario(who)
	print('\n\t*****************Usuario', str(who), 'termine*****************')

def generarProgramacion():
	global canales
	global programas
	global tiempoMax
	for i in range(0,10):
		canales.append([random.randint(1,3), random.randint(4,7)])
		programas.append([])
		acumulado = 0
		programa = 0
		while acumulado < tiempoMax:
			programas[i].append([])
			programas[i][programa].append(acumulado)
			programas[i][programa].append([])
			duracion = random.randint(1,5) #ATENCION
			for j in range(0,duracion):
				acumulado += canales[i][1]
				programas[i][programa][1].append(acumulado)
				acumulado += canales[i][0]
			acumulado += canales[i][1]
			programas[i][programa].append(acumulado)
			programa += 1
	print('Se generarron los canales y programas\ncanales:', canales, '\nprogramas:', programas)

###Varibles 
numeroTeles=0
tiempo = 0 #Este contador se utiliza para indicar la hora actual
pasillo = threading.Semaphore(numeroTeles) #Este semaforo sirve para indicar si hay televisiones disponibles, si un integrante desea una television pero todos estan ocupadas el hilo se queda esperando
queHoraEs = threading.Semaphore(1) #Mutex para acceder al contador de tiempo
tomarTele = threading.Semaphore(1)
canales = [] #Este arreglo sirve para indicar el numero de canales disponibles y el tamaño de sus bloques comerciales y la frecuencia de los mismos
programas = [] #Este arreglo idica los programas de los canales con su duracion [[[horaInicio, [bloquesComerciales], horaFin], ...], ...]
teles = [[]*3]*numeroTeles #En este arreglo se guarda el canal sintonizado en cada tele [[canal, programa, [usuarios]], ...]
control = [threading.Semaphore(0)]*numeroTeles
tiempoMax = 100
TelesEnUso = [0]*numeroTeles
telesGrafo=[]


ventana=Tk()
ventana.geometry("800x800")
ventana.configure(bg="#33D4AE")
ventana.title("EL problema de las televisiones")


#Definicion de etiquetas
titulo=Label(ventana,text='Horario Familiar',relief=RAISED, fg="white", justify=CENTER, font=("Verdana", 36),bg="#33D4AE")
titulo.pack(padx=1, pady=15)

entrada=Frame(ventana,bg="white")
entrada.pack(padx=1, pady=40)
entrada.config(width=480,height=350)

instrucciones=Label(entrada,text="Indica las variables a utilizar ;)",fg="black", justify=CENTER, font=("Verdana", 12))
instrucciones.place(relx=0.2,rely=0.0)

integrantes=Label(entrada,text="Num. Integrantes",fg="black", justify=CENTER, font=("Verdana", 12))
integrantes.place(relx=0,rely=0.2)
intEnt=Entry(entrada)
intEnt.place(relx=0.4,rely=0.2)



tele=Label(entrada,text="Num. Televisiones",fg="black", justify=CENTER, font=("Verdana", 12))
tele.place(relx=0,rely=0.5)
teleEnt=Entry(entrada)
teleEnt.place(relx=0.4,rely=0.5)


adelante = Button(entrada, text="¡ADELANTE!",width=10, justify=CENTER, command=Programa)
adelante.place(relx=0.4,rely=0.7)



#numTelevisiones=float(teleEnt.get())

#numIntegrantes=float(intEnt.get())

ventana.mainloop()
