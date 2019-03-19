print('''
#___________                      __      __.__            .___                   
#\\__    ___/___ _____    _____   /  \\    /  \\__| ____    __| _/______  _  ________
#  |    |_/ __ \\__   \\  /     \\  \\   \\/\\/   /  |/    \\  / __ |/  _ \\ \\/ \\/ /  ___/
#  |    |\\  ___/ / __ \\|  Y Y  \\  \\        /|  |   |  \\/ /_/ (  <_> )     /\\___ \\ 
#  |____| \\___  >____  /__|_|  /   \\__/\\  / |__|___|  /\\____ |\\____/ \\/\\_//____  >
#             \\/     \\/      \\/         \\/          \\/      \\/                 \\/ 
#                                                                                 
#___  ________                                                                    
#\\  \\/ /  ___/                                                                    
# \\   /\\___ \\                                                                     
#  \\_//____  >                                                                    
#          \\/                                                                     
#___________                     .____    .__                                     
#\\__    ___/___ _____    _____   |    |   |__| ____  __ _____  ___                
#  |    |_/ __ \\__   \\  /     \\  |    |   |  |/    \\|  |  \\  \\/  /                
#  |    |\\  ___/ / __ \\|  Y Y  \\ |    |___|  |   |  \\  |  />    <                 
#  |____| \\___  >____  /__|_|  / |_______ \\__|___|  /____//__/\\_ \\                
#             \\/     \\/      \\/          \\/       \\/            \\/                
@autor: 
González Pacheco Leonardo
Pérez Ruiz Miguel Ángel
''')



import threading
from random import random
from time import sleep

# Contadores para developeres de Linux (hackers) y Microsoft (serfs)
global hackers
global serfs
global persona_balsa, nHackers, nSerfs      #Contadores de personas

entidad = threading.Semaphore(1) 			# entidad's - semáforo inicializado en 1
shieldBalsa = threading.Semaphore(1)
rowSerfs = threading.Semaphore(0)			#semaforo para el numero maximo de hackers y Serfs
rowHackers = threading.Semaphore(0)
safeProcessThread = threading.Barrier(4)   	#asegura que solo puedan correr 4 hilos
#Variables contadoras	
hackers = 0
serfs = 0
persona_balsa = 0
nHackers = 0
nSerfs = 0



#Funcion Cruzar rio(tipoDesarrollador,id_desarrollador)
def crossRiver(developer,id):
	global persona_balsa, nHackers, nSerfs
	print("Aborda un {} con ID: {}".format(developer,id))
	persona_balsa += 1
	if developer == "hacker":  #si es hacker
		nHackers += 1
		#debug
		#print("ha subido un hacker")
	elif developer == "serf":  #si es serf
		nSerfs += 1
		#debug
		#print("ha subido un serf")

	if persona_balsa == 4: 	   #si la balsa esta llena
		print("=====================================================================")
		print("La balsa ha partido con {} Hackers y {} Serfs".format(nHackers,nSerfs))
		print("=====================================================================")
		persona_balsa = 0
		nSerfs = 0
		nHackers = 0


#llegado un hacker a la balsa
def arryvedHacker(idHacker):
	global hackers
	global serfs

	entidad.acquire()    		#entidad para comprar
	hackers += 1
	print("El Hacker con ID: {}".format(idHacker))
	if hackers >= 4: 			#si hay 4 hackers
		for i in range(4):
			rowHackers.release()
		hackers -= 4
		entidad.release()   	# Liberamos entidad
	#si hay 2 hackers y 2 serfs
	elif hackers >= 2 and serfs >= 2:
		rowSerfs.release()       # Se liberan 2 hackers y 2 serfs de la fila 
		rowSerfs.release()
		rowHackers.release()
		rowHackers.release()
		hackers -= 2
		serfs -= 2
		entidad.release()        # Liberamos entidad
	else:
		entidad.release() 		 # Si no entra en niguna opcio, solo se libera entidad
	
	rowHackers.acquire()
	if safeProcessThread.broken: # Si la safeProcessThread "estado roto" se reinicia
		safeProcessThread.reset()#reseteamos el proceso de seguridad

	safeProcessThread.wait()     # Se queda esperando hasta que 4 hilos terminan "wait"
	shieldBalsa.acquire()        # se captura laentidad
	crossRiver("hacker",idHacker)
	shieldBalsa.release()


# llegado un serf
def arryvedSerf(idSerf):
	global hackers
	global serfs

	entidad.acquire()
	serfs += 1
	print("Serf",idSerf,"llegó")
	if serfs >= 4:                     #Si hay 4 Serfs
		for i in range(4):
			rowSerfs.release()   	   #Suben a la balsa 4 Serfs

		serfs -= 4
		entidad.release()  		 	   #Liberamos entidad
	
	elif hackers >= 2 and serfs >= 2:  #si hay 2 hackers y 2 serfs
		rowSerfs.release()             # Abordan 2 hackers y 2 serfs
		rowSerfs.release()
		rowHackers.release()
		rowHackers.release()
		hackers -= 2
		serfs -= 2
		entidad.release()			# Liberamos el entidad
	else:
		entidad.release()           # en otro caso, solo se libera entidad

	rowSerfs.acquire()              # Serf se queda esperando a abordar
	
	if safeProcessThread.broken:    # Si la safeProcessThread entra en "estado roto" se reinicia
		safeProcessThread.reset()
	safeProcessThread.wait()		# Se queda esperando hasta que los 4 hilos terminen
	
	shieldBalsa.acquire()     		#entidad para proteger la función crossRiver
	crossRiver("serf",idSerf)
	shieldBalsa.release()



def main():
	idHacker = 0    #ids
	idSerf = 0
	try:
		while (True):
			#los numeros random estan generados del 0 al 1 con decimales
			#otorgando una probabilidad del 50% a cada uno de los dos tipos de personas
			if random() < 0.5:
				idHacker += 1
				threading.Thread(target=arryvedHacker, args = ["H4KR#"+str(idHacker)]).start()
				sleep(1) # Cada segundo se generará un hilo
			else:
				idSerf += 1
				threading.Thread(target=arryvedSerf, args = ["Win32#"+str(idSerf)]).start()
				sleep(1)
	except KeyboardInterrupt:
		print("Se ha detenedo la ejecución mediante el teclado")
			#KeyboardInterrupt

main()
