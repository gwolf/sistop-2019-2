import random
def FCFS(procesos):
	tiempo=0
	ejecucion = ''
	t=[] #acumulador tiempo que toma el trabajo
	e=[] #acumulador tiempo de espera
	p=[] #acumulador T/t
	for pro in procesos:
		espera = tiempo - pro[0]
		ejecucion += ''
		if espera >= 0:
			e.append(espera)
		else:
			tiempo = pro[0]
			e.append(0)
			for j in range(0,espera,-1):
				ejecucion += '_'
		tiempoPro = espera + pro[1]
		t.append(tiempoPro)
		p.append(t[-1]/pro[1])
		for i in range(0,pro[1]):
			ejecucion += pro[2]
		tiempo += pro[1]
	mostrar('FCFS:', t, e, p, ejecucion)

def RR1(procesos):
	aux = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14}
	contador=0 #Si no existe ningun proceso esto no funciona
	tiempo=0
	cola=[]
	ejecucion=''
	t=[0]*len(procesos) #acumulador tiempo que toma el trabajo
	e=[0]*len(procesos) #acumulador tiempo de espera
	p=[0]*len(procesos) #acumulador T/t
	i=0
	x=0
	eT=[]#Respaldo de tiempos de ejecucion
	for s in procesos:
		eT.append(s[1])
	while contador < len(procesos) or len(cola) > 0:
		contador += queu(procesos, tiempo, cola, contador)
		if len(cola) > 0:
			while i < len(cola):
				ejecucion += cola[i][2]
				eT[aux[cola[i][2]]] -= 1
				while x < len(cola):
					indice = aux[cola[x][2]]
					if x != i:
						e[indice] += 1
					t[indice] += 1
					x += 1
				x=0
				if eT[aux[cola[i][2]]] == 0:
					cola.pop(i)
					if i >= len(cola):
						i=0
				else:
					i+=1
				tiempo += 1
				contador += queu(procesos, tiempo, cola, contador)
			i=0
		else:
			ejecucion += '_'
			tiempo += 1
	for k in range(0,len(p)):
		p[k]= t[k]/procesos[k][1]
	mostrar('RR1:', t, e, p, ejecucion)



def RR4(procesos):
	aux = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14}
	contador=0 #Si no existe ningu proceso esto no funciona
	tiempo=0
	cola=[]
	ejecucion=''
	t=[0]*len(procesos) #acumulador tiempo que toma el trabajo
	e=[0]*len(procesos) #acumulador tiempo de espera
	p=[0]*len(procesos) #acumulador T/t
	i=0
	x=0
	tam=0
	eT=[]
	for s in procesos:
		eT.append(s[1])
	while contador < len(procesos) or len(cola) > 0:
		contador += queu(procesos, tiempo, cola, contador)
		if len(cola) > 0:
			while i < len(cola):
				ejecucion += cola[i][2]
				eT[aux[cola[i][2]]] -= 1
				while x < len(cola):
					indice = aux[cola[x][2]]
					if x != i:
						e[indice] += 1
					t[indice] += 1
					x += 1
				x=0
				tiempo += 1
				if eT[aux[cola[i][2]]] == 0:
					cola.pop(i)
					if i >= len(cola):
						i = 0
					tam = 0
				else:
					tam += 1
					if tam == 4:	
						i += 1
						tam = 0
				contador += queu(procesos, tiempo, cola, contador)
			i=0
		else:
			ejecucion += '_'
			tiempo += 1
	for k in range(0,len(p)):
		p[k]= t[k]/procesos[k][1]
	mostrar('RR4:', t, e, p, ejecucion)



def queu(procesos, tiempo, cola, contador):
	aux = 0
	for y in range(contador, len(procesos)):
		if procesos[y][0] <= tiempo:
			cola.append(procesos[y])
			aux += 1
	return aux

def mostrar(w, t, e, p, ex):
	T=0
	E=0
	P=0
	lon=len(t)
	for x in range(0,lon):
		T += t[x]
		E += e[x]
		P += p[x]
	print( w + ' T=' + str(T/lon) + ', E=' + str(E/lon)  + ', P=' + str(P/lon))
	print(ex)

    
def SPN(A):
	global numProcesos
	tiempo=A[0][0]	#Inicializamos el tiempo
	t=[] #acumulador tiempo que toma el trabajo
	e=[] #acumulador tiempo de espera
	p=[] #acumulador T/t
	E=[]*len(A) #lista de los procesos que tienen que esperar
	ejecucion="" #Cadena con nombre orden ejecucion
	espera=0
	cont=0
	Basura=[]
	for j in range(0,tiempo):
		ejecucion += '_ '

	for i in range(numProcesos):
		
		if A[i][0]	<= tiempo:
			for k in range (i,numProcesos):
				if A[k][0]<= tiempo:
					
					
					if (A[k] not in Basura): 
						
						E.append(A[k])
						
						cont+=1
					else:
						print("YA ESTA")
						i+=1
			E.sort(key=lambda x:x[1])
			espera=tiempo-E[0][0]
			tiempo=tiempo+E[0][1]
		else:
			E.append(A[i])
			libre=E[0][0]-tiempo
			for m in range (libre):
				ejecucion += '_ '
			E.sort(key=lambda x:x[1])
			espera=0
			tiempo+=libre
			tiempo=tiempo+E[0][1]

		for l in range (E[0][1]):
			ejecucion += E[0][2]
		tiempoPro=espera+E[0][1]
		e.append(espera)
		t.append(tiempoPro)
		p.append(t[-1]/E[0][1])
		Basura.append(E[0])
		E.pop(0)
    
    
def prueba(ronda):
	numProcesos=3
	cad=''
	j=0
	#Nombre de los procesos
	diccionario={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',
		7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O'}
	procesos=[]#random
	#Lista de Procesos
	for i in range (numProcesos):
		procesos.append([random.randint(0,10),random.randint(1,10)])
	#ordenarla por orden de llegada
	ordenProcesos=sorted(procesos)
	#Agregamos nombre a los procesos
	for i in ordenProcesos:
		i.append(diccionario[j])
		cad += diccionario[j] + ': ' + str(i[0]) + ', t=' + str(i[1]) + ';'
		j+=1
	print('-Ronda', ronda, ':')
	print(cad)
	FCFS(ordenProcesos)
	RR1(ordenProcesos)
	RR4(ordenProcesos)
    SPN(ordenProcesos
#A=[[0,3,'A'],[1,5,'B'],[3,2,'C'],[9,5,'D'],[12,5,'E']]
#FCFS(A)
#RR1(A)
#RR4(A)
for x in range(1,6):
	prueba(x)