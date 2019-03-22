from random import randint,sample

class proceso(object):
 
  def __init__(self,id,CPU,llegada):
    self.id = id
    self.CPU = CPU
    self.CPU2 = CPU
    self.llegada = llegada
    self.finalizacion = 0
    self.espera = 0
    self.retorno = 0
    self.penalizacion = 0

try:
	#numeros: cantidad de procesos a introducir
	numeros = 10
	listallegada = []
	listaCPU = []

	for i in range(numeros):
		listaCPU.append(randint(5, 12))
	listallegada = sample(range(1, 15), numeros)
	#forzando inicio en cero:
	listallegada[0] = 0
	listallegada.sort()

	print("\n\n#########################################################################\nFCFS\n")

####################################################################################################################

	def tiempoRespuestaT(cant_proc, t_fin, t_llegada, t_respuestaT):
		for i in range(cant_proc):
			t_respuestaT[i] = t_fin[i] - t_llegada[i]


	def tiempoEsperaE(cant_proc, t_requerido, t_respuestaT, t_esperaE):
		for i in range(cant_proc):
			t_esperaE[i] = t_respuestaT[i] - t_requerido[i]


	def propPenalizacionP(cant_proc, t_requerido, t_respuestaT, penalizacionP):
		for i in range(cant_proc):
			penalizacionP[i] = t_respuestaT[i] / t_requerido[i]


	def calculosFCFS(procesos, cant_proc, t_requerido, t_llegada):
		t_inicio = [0] * cant_proc
		t_respuestaT = [0] * cant_proc
		t_fin = [0] * cant_proc
		t_esperaE = [0] * cant_proc
		penalizacionP = [0] * cant_proc
		t_espera_total = 0
		t_respuesta_total = 0
		penal_total = 0

		# tiempo de inicio de ejecución del proceso (no es el tiempo de llegada)
		for i in range(1, cant_proc):
			t_inicio[i] = t_inicio[i - 1] + t_requerido[i - 1]
		# tiempo de fin de ejecucion del proceso
		for i in range(cant_proc):
			t_fin[i] = t_requerido[i] + t_inicio[i]

		# Para obtener t_respuestaT para cada proceso
		tiempoRespuestaT(cant_proc, t_fin, t_llegada, t_respuestaT)
		# Para obtener t_esperaE para cada proceso
		tiempoEsperaE(cant_proc, t_requerido, t_respuestaT, t_esperaE)
		# Para obtener penalizacionP para cada proceso
		propPenalizacionP(cant_proc, t_requerido, t_respuestaT, penalizacionP)

		for i in range(cant_proc):
			# totales para obtener despues promedios
			t_respuesta_total = t_respuesta_total + t_respuestaT[i]
			t_espera_total = t_espera_total + t_esperaE[i]
			penal_total = penal_total + penalizacionP[i]

			print("Proceso", procesos[i], "\t\tLlegada:", t_llegada[i], "     Requerido:", t_requerido[i],
				  "\t\tEspera:", t_esperaE[i], "\t\tFinalizo:", t_fin[i],
				  "\t\tRespuesta:", t_respuestaT[i], "\t\tPenalizacion:", penalizacionP[i])

		print("\nPromedio de tiempo de respuesta: " + str(t_respuesta_total / cant_proc),
			  "\nPromedio de tiempo de espera = " + str(t_espera_total / cant_proc),
			  "\nPromedio de penalizacion = " + str(penal_total / cant_proc))


	#def controladora():
	procesos = []
		#tiempo_requerido = []  # t

		#cant_proc = randint(4, 10)
	for i in range(numeros):
		procesos.append(i + 1)
		#tiempo_requerido.append(randint(3, 10))
		#tiempo_llegada = sample(range(0, 12), cant_proc)
		#tiempo_llegada.sort()

	calculosFCFS(procesos, numeros, listaCPU, listallegada)

	####################################################################################################################

	listaprocesos = []
	for i in range(numeros):
		ordenLlegada = -1
		while(ordenLlegada <0):
			ordenLlegada = listallegada[i]
		CPU2 =0
		while(CPU2  <1):
			CPU2 = listaCPU[i]
		listaprocesos.append(proceso((i+1),CPU2,ordenLlegada))
	quantum =0
	control = False
	while(quantum <1):
		quantum = 1
	quantumtmp = quantum

	def ordenaInsersion(lista):
		for i in range(1,len(lista)):
			j = i
			while j > 0 and lista[j].llegada < lista[j-1].llegada:
				lista[j], lista[j-1] = lista[j-1], lista[j]
				j=j-1
		return lista

	listaprocesos = ordenaInsersion(listaprocesos)

	procesosControl = len(listaprocesos)
	tiempo = 0
	Cola=[]
	proceso2 = None
	siguiente = 0
	control = True

	print("\n\n###################################################\nRound Robin\n")
	while(procesosControl>0):
		if(len(listaprocesos) > siguiente and tiempo >= listaprocesos[siguiente].llegada):
			Cola.append(listaprocesos[siguiente])
			siguiente = siguiente +1
		else:
			if (siguiente>0 or len(Cola) > 0):
				if(proceso2 == None):
					proceso2 = Cola.pop(0)
					control = True
				else:
					if(control):
						if(proceso2.CPU2 >=quantum):
							proceso2.CPU2 = proceso2.CPU2 - quantum
							print("Tiempo "+str(tiempo))
							print("Se atendió al proceso "+str(proceso2.id))
							tiempo = tiempo + quantum
						else:
							tiempo = tiempo + proceso2.CPU2
							print("Tiempo "+str(tiempo))
							print("[Se atendió al proceso  "+str(proceso2.id))
							proceso2.CPU2 = 0
						if(proceso2.CPU2 <1 ):
							print("Tiempo "+str(tiempo))
							print("El Proceso "+str(proceso2.id)+ " finalizó.")
							proceso2.finalizacion = tiempo
							proceso2.retorno = proceso2.finalizacion - proceso2.llegada # retorno = tiempo de respuesta
							proceso2.espera = proceso2.retorno - proceso2.CPU
							procesosControl = procesosControl-1
							proceso2.penalizacion = proceso2.retorno / proceso2.CPU
							proceso2 = None
						else:
							control= False
					else:
						Cola.append(proceso2)
						proceso2 = None
			else:
				tiempo = tiempo +1

	print("\nResultados")
	TotalFinal=0
	Totalespera=0
	TotalPenalizacion = 0

	for proceso in listaprocesos:
		#print("Proceso "+ str(proceso.id) + "\t\tFinalizo: "+str(proceso.finalizacion) + "\t\tEspera: "+str(proceso.espera)+ "\t\tRetorno: "+str(proceso.retorno))
		print("Proceso " + str(proceso.id) + "\t\tLlegada: " + str(proceso.llegada) + "\t\tRequerido: " + str(proceso.CPU)
			+ "\t\tEspera: " + str(proceso.espera) + "\t\tFinalizo: " + str(proceso.finalizacion)
			+ "\t\tRespuesta: " + str(proceso.retorno) + "\t\tPenalizacion: " + str(proceso.penalizacion))

		TotalFinal = TotalFinal + proceso.retorno
		Totalespera = Totalespera + proceso.espera
		TotalPenalizacion = TotalPenalizacion + proceso.penalizacion

	print("\nPromedio de tiempo de respuesta: " +str(TotalFinal/len(listaprocesos)))
	print("Promedio de tiempo de espera: " +str(Totalespera/len(listaprocesos)))
	print("Promedio de penalizacion: " + str(TotalPenalizacion / len(listaprocesos)))



	print("\n\n#########################################################################\nSPN\n")

	mini=9999999999
	mini2=999999999
	listaprocesos = []
	listatotal = []
	glo = 0
	final = 0
	
	for i in range(numeros):
	    ordenLlegada = listallegada[i]
	    if ordenLlegada < mini:
	        temp = ordenLlegada
	        mini = temp
	    CPU = listaCPU[i]
	    listaprocesos.append(((i+1),CPU,ordenLlegada))
	    listatotal.append(((i+1),CPU,ordenLlegada))
	print(listaprocesos)
	print("\n")
	#print("\n")
	t=0
	total=0
	o = 0
	for o in range(numeros):
	    total = total + int(listatotal[o][1])

	TrabajarCola = []
	cola=[]
	listafinalizacion = []
	x = 0

	for i in range(numeros):
	    if listaprocesos[i][2]==temp:
	        TrabajarCola.append(listaprocesos[i])
	        if listaprocesos[i][1] < mini2:
	            temp2 = listaprocesos[i][1]
	            mini2 = temp2
	            x=i
	            cola=[]
	            cola.append(listaprocesos[x])
	            final = listaprocesos[x][1]
	            listafinalizacion.append(final)

		#print(cola)
	glob = 0
	f=0
	esptotal=0
	fptotal=0
	totalresp = 0
	print("Se trabajó el proceso "+str(x+1)+"\nCon un tiempo de respuesta (T) de "+str(listafinalizacion[f])+"\nUn tiempo de espera (E) de 0\nUna penalización (P) de 0")
	listaprocesos.pop(x)
	print("\n")
	#print(listaprocesos)
	comp = cola[0][1]
	while len(listaprocesos)>0:
	    mini3 = 9999999
	    glob = cola[0][1]
	    for i in range(len(listaprocesos)):
	        if listaprocesos[i][2] <= comp:
	            TrabajarCola.append(listaprocesos[i])
	            if listaprocesos[i][1] < mini3:
	                temp3 = listaprocesos[i][1]
	                mini3 = temp3
	                x=i
	                cola=[]
	                cola.append(listaprocesos[x])
#   print(cola)
	    final = final + listaprocesos[x][1]

	    listafinalizacion.append(final)
	    f+=1
	    esptotal= esptotal+(listafinalizacion[f]-listaprocesos[i][2])
		#fp=((int(listafinalizacion[f])-int(listaprocesos[i][2]))*(1))/total
	    fp=((int(listafinalizacion[f]))*(1))/CPU
	    fptotal = fp + fptotal
	    print("Se trabajó el proceso "+str(listaprocesos[x][0])+"\nCon un tiempo de respuesta (T) de "+str(listafinalizacion[f])+"\nUn tiempo de espera (E) de "+str(listafinalizacion[f]-listaprocesos[i][2])+"\nUna penalización (P) de "+str(fp))
	    totalresp = totalresp + listafinalizacion[f]
	    listaprocesos.pop(x)
	    #print(listaprocesos)
	    print("\n")
	    comp = cola[0][1] + glob
		#print(listafinalizacion)
	#print(total)
	promesp = esptotal/numeros
	prompen = fptotal/numeros
	promresp = totalresp/numeros
	print("Promedio de tiempo de respuesta: " + str(promresp))
	print("Promedio de tiempo de espera: "+str(promesp))
	print("Promedio de penalización: "+str(prompen))


except Exception as e:
  print("ERROR")