#ImplementandoFIFO en python


from random import randint

#creadno conjunto de procesos
procesos = []

cantproc = 5;
quantum  = 3;
tiempo_llegada = 0;


for i in range(1,cantproc):
	proc = []
	tiempo_requerido = randint(3,15);
	proc.append([i,tiempo_llegada,tiempo_requerido])
	procesos.append(proc)
	tiempo_llegada  = tiempo_llegada +1;

for l in range(0,cantproc-1):
	p = procesos[l]
	tiempo_ejecucion  = p[0][2]
	while p[0][2] >0 :
		
