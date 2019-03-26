from random import randint
procesos=[]

def llenarProcesos():
	procesos.append(['A',0,randint(4,10)])
	procesos.append(['B',randint(1,3),randint(1,10)])
	procesos.append(['C',randint(4,7),randint(1,10)])
	procesos.append(['D',randint(8,10),randint(1,10)])
	procesos.append(['E',randint(11,13),randint(1,10)])

def imprimirDatosProcesos():
	for elemento in procesos:
		datos= elemento[0]+": "+str(elemento[1])+", t="+str(elemento[2])
		print datos

def calculoPromedios(tTotal,tEspera,penalizacion):
	promedioTiempoTotal=0
	promedioTiempoEspera=0
	promedioPenalizacion=0
	tmpT=0
	tmpE=0
	tmpP=0

	for i in tTotal:
		tmpT = tmpT + i

	for i in tEspera:
		tmpE = tmpE + i

	for i in penalizacion:
		tmpP = tmpP + i

	promedioTiempoTotal = tmpT/5.0
	promedioTiempoEspera = tmpE/5.0
	promedioPenalizacion = tmpP/5.0
	promedios="T="+str(promedioTiempoTotal)+", E="+str(promedioTiempoEspera)+", P="+str(promedioPenalizacion)
	print promedios

def fifo(procesos):
	ordenProcesamiento=[]
	fin=[]
	tiempoTotal=[]
	tiempoEspera=[]
	penalizacion=[]
	procesoActual=0
	tiempoIndividual=procesos[procesoActual][2]
	while(procesoActual<5):
		if tiempoIndividual > 0:
			ordenProcesamiento.append(procesos[procesoActual][0])
			tiempoIndividual = tiempoIndividual - 1
		else:
			if procesoActual != 4:
				if procesoActual == 0:
					fin.append(procesos[procesoActual][2])
					tiempoTotal.append(procesos[procesoActual][2])
					tiempoEspera.append(0)
					penalizacion.append(tiempoTotal[procesoActual]/procesos[procesoActual][2])
				else:
					tiempoEspera.append(fin[procesoActual-1] - procesos[procesoActual][1])
					tiempoTotal.append(tiempoEspera[procesoActual]+procesos[procesoActual][2])
					penalizacion.append(tiempoTotal[procesoActual]/procesos[procesoActual][2])
					fin.append(fin[procesoActual-1]+procesos[procesoActual][2])
				procesoActual = procesoActual + 1
				tiempoIndividual = procesos[procesoActual][2]
			else:
				procesoActual = procesoActual + 1
	print "FIFO"
	print " "
	calculoPromedios(tiempoTotal,tiempoEspera,penalizacion)
	print ordenProcesamiento

"""def roundRobin(procesos,quantum):
	quantumTmp=quantum
	fin=[]
	tiempoTotal=[]
	tiempoEspera=[]
	penalizacion=[]
	colaProcesos=[]
	ordenProcesamiento=[]
	numProcesos=0
	tiempoIndividual=procesos[numProcesos][2]
	tiempoTranscurrido=0
	while(numProcesos<5):
		if tiempoTranscurrido == procesos[numProcesos][1]:
			colaProcesos.append(procesos[numProcesos])
		else:
			if (colaProcesos[numProcesos][2] > 0) and (quantumTmp >0):
				ordenProcesamiento.append(colaProcesos[numProcesos][0])
				colaProcesos[numProcesos][2] = colaProcesos[numProcesos][2] - 1
				quantumTmp = quantumTmp -1
				tiempoTranscurrido = tiempoTranscurrido + 1
			else:			
				if quantumTmp == 0:
					colaProcesos.popleft()
					colaProcesos.append(procesos[numProcesos])
				else:
					colaProcesos.popleft()
					numProcesos = numProcesos -1

	nombreAlgoritmo= "RR"+str(quantum)	
	print nombreAlgoritmo
	#calculoPromedios(tiempoTotal,tiempoEspera,penalizacion)
	print ordenProcesamiento"""

def main():
	global procesos
	numRondas = 0
	while(numRondas < 5):
		print "Ronda "+str(numRondas+1)
		llenarProcesos()
		imprimirDatosProcesos()
		fifo(procesos)
		numRondas = numRondas +1
		procesos[:]=[]

main()





