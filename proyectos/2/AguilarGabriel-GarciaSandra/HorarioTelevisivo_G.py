from tkinter import *
import os
import threading
import random
import time
import sys
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import tkinter

def Programa():
	global numeroTeles
	global numeroIntegrantes
	global telesGrafo
	global TelesEnUso
	global teles
	global pasillo
	global control
	global desarrollo
	global tiempo 

	#Obtencion variables de entrada
	StrTelevisiones=teleEnt.get()
	StrIntegrantes=intEnt.get()

	numeroTeles=int(StrTelevisiones)
	numeroIntegrantes=int(StrIntegrantes)
	
	pasillo = threading.Semaphore(numeroTeles) #Este semaforo sirve para indicar si hay televisiones disponibles, si un integrante desea una television pero todos estan ocupadas el hilo se queda esperando
	teles = [[]*3]*numeroTeles #En este arreglo se guarda el canal sintonizado en cada tele [[canal, programa, [usuarios]], ...]
	control = [threading.Semaphore(0)]*numeroTeles
	TelesEnUso = [0]*numeroTeles

	entrada.pack_forget()

	desarrollo=Frame(ventana, bg="#33D4AE")
	desarrollo.pack(padx=1, pady=40, fill=BOTH, expand=1)
	desarrollo.config(width=480,height=600)


	desarrollo.columnconfigure(numeroTeles-1,weight=1)
	desarrollo.rowconfigure(3, weight=1)

	mensaje = Text(desarrollo, height=3, width=50, fg="black",font=("Verdana", 15))
	
	S = Scrollbar(desarrollo,command=mensaje.yview)
	mensaje.config(yscrollcommand=S.set)
	
	

	#Definicion de etiquetas que simulan la television
	telesGrafo=[]
	for i in range(0,numeroTeles):
		telesGrafo.insert(i,Label(desarrollo,bg="black",fg="white"))
		telesGrafo[i].grid(row=1,column=i,sticky="nsew",padx=10, pady=10)
		desarrollo.columnconfigure(i,weight=1)


	espera=Label(desarrollo,text="",font=("Verdana", 15))
	users=Label(desarrollo, text="Tiempo",font=("Verdana", 15))

	#Conficugracines grid
	mensaje['yscrollcommand']=S.set
	espera.grid(row=2, column=0, columnspan=numeroTeles,sticky="s")
	users.grid(row=3, column=0, columnspan=numeroTeles)
	desarrollo.rowconfigure(0,weight=1)
	desarrollo.rowconfigure(1,weight=2)
	desarrollo.rowconfigure(2,weight=1)
	desarrollo.rowconfigure(3,weight=1)
	
	###
	generarProgramacion()
	
	#Creacion de usuarios
	for i in range(0,numeroIntegrantes): 
		threading.Thread(target=Usuario, args=[i]).start()
	threading.Thread(target=padreTiempo, ).start()

	espera=Label(desarrollo,text="",font=("Verdana", 15))
	users=Label(desarrollo, text="Tiempo",font=("Verdana", 15))

	
#*********Funciones manejo ineterfaz*******
#Imprime valores televisiones
def impresion():
	global tiempo
	global teles
	global numeroTeles
	global telesGrafo
	global espera
	for i in range(0,numeroTeles):
		if len(teles[i])==0:
			telesGrafo[i]['text']="Desocupada"
		else:
			telesGrafo[i]['text']="Canal: ",teles[i][0],"\nPrgrama: ",teles[i][1],"\nUsuarios: ",teles[i][2]
#Imprime valor de cuadro de texto
def info(a):
	global texto
	global desarrollo
	global mensaje
	mensaje = Text(desarrollo, height=8, width=80, fg="black",font=("Verdana", 10))
	mensaje.grid(row=0, column=0, columnspan=numeroTeles)
	S = Scrollbar(desarrollo,command=mensaje.yview)
	mensaje.config(yscrollcommand=S.set)
	texto+=a
	mensaje.delete('1.0', END)
	mensaje.insert(END,texto)

def fin():
	for i in range(0,numeroTeles):
		telesGrafo[i]['text']="Desocupada"	
	mensaje.delete('1.0', END)
	mensaje.insert(END,"Terminó Ejecución. Adiós")
	time.sleep(3)
	ventana.destroy()

def actTiempo():
	global desarrollo
	global espera
	global tiempo
	espera = Label(desarrollo,text="",font=("Verdana", 15))
	espera.grid(row=2, column=0, columnspan=numeroTeles,sticky="s")
	espera['text']=tiempo

	
#**********Funciones parte logica************
#Funcion que maneja tiempo global, es la encargada de incrementar el tiempo.
def padreTiempo():
	global tiempo
	global tiempoMax
	global ventana
	global espera
	continuar = True
	while continuar:
		queHoraEs.acquire()
		ActualizarTeles()
		if tiempo < tiempoMax+20:
			tiempo += 1
		else:
			continuar = False
		queHoraEs.release()
		actTiempo()
		print(tiempo)
		time.sleep(0.5)
	fin()
	print('Fin simulacion')

#Esta funcion se encarga de verificar que los programas sintonizados en cada televisor no hayan terminado o entrado en bloque comercial
def ActualizarTeles():
	global tiempo
	global programas
	global teles
	global TelesEnUso
	global numeroTeles
	for i in range(0,numeroTeles):
		tomarTele.acquire()
		print(TelesEnUso)
		if TelesEnUso[i] == 1:
			canal = teles[i][0]
			programa = teles[i][1]
			if programas[canal][programa][2] <= tiempo:
				for x in teles[i][2]: #Si el programa termino indica a todos los que veian esa tele que debe desocuparla
					control[i].release()
			else:
				for x in  programas[canal][programa][1]:
					if x == tiempo:
						for j in teles[i][2]:#Si el programa esta en comerciales indica a todos los que veian esa tele que debe desocuparla
							control[i].release()
		tomarTele.release()
	impresion()

def Usuario(who):
	global canales
	global programas
	global tiempo
	global teles
	global TelesEnUso
	time.sleep(0.1)#Con este sleep buscamos concurrencia
	canal = random.randint(0,len(canales)-1) #El usuario elige un canal y programa de la programacion al azar 
	programa = random.randint(0,len(programas[canal])-1)
	otroPrograma = random.random() % 0.1 #Esta es la probabilidad de que un usuario quiera ver otro programa una vez termine el primero
	print('Usuario:', str(who), '; quiero ver:', canal, programa, 'que empieza en', programas[canal][programa][0], 'y termina en', programas[canal][programa][2])
	queHoraEs.acquire()
	tiempoAux = tiempo #El usuario verifica en que tiempo se encuentra
	queHoraEs.release()
	while programas[canal][programa][0] > tiempoAux: #Mientras su programa no haya iniciado el usuario solo ve el tiempo
		queHoraEs.acquire()
		tiempoAux = tiempo
		queHoraEs.release()
	while programas[canal][programa][2] > tiempoAux: #Mientras su programa no termine los usuarios sigue este algoritmo:
		texto='\nSoy usuario:'+ str(who)+ 'estoy en el pasillo esperando'
		info(texto)
		pasillo.acquire() #Primero espera a que una tele se desocupe
		time.sleep(0.1) #antes de entrar dejo salir
		queHoraEs.acquire()
		tiempoAux = tiempo#Debido a que pudo haber esperado varios tiempos vuelve a verificar que el programa no haya terminado
		queHoraEs.release()
		if programas[canal][programa][2] > tiempoAux:
			texto='\nSoy usuario: '+ str(who)+ ' busco una tele'
			info(texto)
			tomarTele.acquire()
			compartiendo = 0
			for x in range(0,len(TelesEnUso)): #Revisa si alguien más esta viendo el mismo programa para utilizar la misma tele
				if TelesEnUso[x] == 1 and teles[x][0] == canal and teles[x][1] == programa:
					teles[x][2].append(who)
					lugar = x
					compartiendo += 1 
			if compartiendo == 0: #Si nadie esta viendo lo mismo toma la tele que se desocupo
				lugar = TelesEnUso.index(0)
				TelesEnUso[lugar] = 1
				if len(teles[lugar]) == 0:
					teles[lugar] = [canal, programa, [who]]
				else:
					teles[lugar][0] = canal
					teles[lugar][1] = programa
					teles[lugar][2].append(who)
			else:
				pasillo.release() #Si va a compartir televisor avisa que hay una tele libre
			tomarTele.release()
			control[lugar].acquire() #Se queda viendo el televisor hasta que el actualizador de Teles le indique que debe liberar la tele
			texto='\nSoy usuario: '+ str(who)+ ' dejé la tele '+str(lugar)
			info(texto)
			tomarTele.acquire()
			TelesEnUso[lugar] = 0
			if len(teles[lugar][2]) == 1: #si soy el unico viendo la tele aviso a quienes esperan que la tele se desocupo
				pasillo.release()
			teles[lugar][2].remove(who)
			tomarTele.release()
		else:
			pasillo.release() #Si el programa termino mientras esperaba indico a quienes esperan que hay una tele libre
		queHoraEs.acquire()
		tiempoAux = tiempo
		queHoraEs.release()
	if random.random() <= otroPrograma: #El usuario podria elegir otro programa
		Usuario(who)
	texto='\n**Usuario '+str(who)+ ' termino**'
	info(texto)
	print(texto)

#Esta funcion sirve para generar la programacion televisiva
def generarProgramacion():
	global canales
	global programas
	global tiempoMax
	for i in range(0,10): #definimos 10 canales distintos
		canales.append([random.randint(1,3), random.randint(4,7)])#para cada canal se define la duracion de un bloque comercial y de un bloque de programacion
		programas.append([])#En el arreglo programa se genera una lista por cada canal, dentro del cual se ponen los distintos programas del mismo
		acumulado = 0
		programa = 0
		while acumulado < tiempoMax:#Para cada canal se genera la programacion hasta el tiempo de simulacion
			programas[i].append([])
			programas[i][programa].append(acumulado)#La primer posicion indica la hora en que el programa inicia
			programas[i][programa].append([])#La segunda es un arreglo que indica en que tiempo inician los distintos bloques comerciales
			duracion = random.randint(1,5)#Al azar se define los bloques televisivos que tendra el programa
			for j in range(0,duracion):
				acumulado += canales[i][1]
				if acumulado > tiempoMax:
					programas[i][programa].append(tiempoMax)
					break
				programas[i][programa][1].append(acumulado)
				acumulado += canales[i][0]#cada bloque de programacion va seguido de un bloque comercial
			acumulado += canales[i][1]
			if acumulado > tiempoMax:
				programas[i][programa].append(tiempoMax)
				break
			programas[i][programa].append(acumulado)
			programa += 1
	print("Canales [tiempo comercial][tiempo visualizacion programa]")
	print("Programas [Canal][Usua]")
	print('Se generarron los canales y programas\ncanales:', canales, '\nprogramas:', programas)


###Declaracion variables globales 
numeroTeles=0
tiempo = 0 #Este contador se utiliza para indicar la hora actual
pasillo = threading.Semaphore(numeroTeles) #Este semaforo sirve para indicar si hay televisiones disponibles, si un integrante desea una television pero todos estan ocupadas el hilo se queda esperando
queHoraEs = threading.Semaphore(1) #Mutex para acceder al contador de tiempo
tomarTele = threading.Semaphore(1)#Mutex para los arreglos de TelesEnUso y teles
canales = [] #Este arreglo sirve para indicar el numero de canales disponibles y el tamaño de sus bloques comerciales y bloques de programacion
programas = [] #Este arreglo idica los programas de cada uno de los canales con sus horarios [[[horaInicio, [bloquesComerciales], horaFin], ...], ...]
teles = [] #En este arreglo se guarda el canal sintonizado en cada tele y los usuarios que la utilizan [[canal, programa, [usuarios]], ...]
control = []#Este sera un arreglo de semaforos que serviara para simular que los usuarios se queda mirando la tele
tiempoMax = 40 #********************************************* 
TelesEnUso = [] #En este arreglo se indicara con un 0 las teles libres y con un 1 las teles ocupadas
telesGrafo=[]
texto=""

#Creacion ventana de interfaz
ventana=Tk()
ventana.geometry("800x800")
ventana.configure(bg="#33D4AE")
ventana.title("EL problema de las televisiones")


#Definicion de etiquetas y objetos de la interfaz

titulo=Label(ventana,text='Horario Familiar',relief=RAISED, fg="white", justify=CENTER, font=("Verdana", 36),bg="#33D4AE")
titulo.pack(padx=1, pady=15)

desarrollo=Frame(ventana, bg="#33D4AE")
mensaje = Text(desarrollo, height=3, width=50, fg="black",font=("Verdana", 15))
espera=Label(desarrollo,text="",font=("Verdana", 15))
espera.pack_forget()
mensaje.pack_forget()
desarrollo.pack_forget()

#Marco de entrada de datos
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

#
adelante = Button(entrada, text="¡ADELANTE!",width=10, justify=CENTER, command=Programa)
adelante.place(relx=0.4,rely=0.7)


ventana.mainloop()
