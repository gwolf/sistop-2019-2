#Juarez Agauilar osmar
#Morales Garcia Luis Angel
from random import randint
procesos = ['A','B','C','D']
tLlegada=[randint(1,10), randint(3,10), randint(5,10), randint(7,10)]
def spn(numprocesos, tllegada):
	for i in range(0,len(tLlegada)-1):  
		for j in range(0,len(tLlegada)-i-1):
  			if(tLlegada[j]>tLlegada[j+1]):
			   vartemp=tLlegada[j]
			   tLlegada[j]=tLlegada[j+1]
			   tLlegada[j+1]=vartemp
			   vartemp=procesos[j]
			   procesos[j]=procesos[j+1]
			   procesos[j+1]=vartemp

	tEsperando=[]
	tTotalEspera=0  
	tRespuesta=[]    
	tTotalRespuesta=0  
	tEsperando.insert(0,0)
	tRespuesta.insert(0,tLlegada[0])

	for i in range(1,len(tLlegada)):  
		tEsperando.insert(i,tEsperando[i-1]+tLlegada[i-1])
		tRespuesta.insert(i,tEsperando[i]+tLlegada[i])
		tTotalEspera+=tEsperando[i]
		tTotalRespuesta+=tRespuesta[i]

	tTotalEspera=tTotalEspera/4.0
	tTotalRespuesta=tTotalRespuesta/4.0

	print("\n")
	print("Proceso\t  tiempo de LLegada\t  tiempo de Espera\t ")
	for i in range(0,4):
		imprimir = str(procesos[i])+"\t\t"+str(tLlegada[i])+"\t\t\t"+str(tEsperando[i]) 
		print imprimir
		print("\n")
	print("Promedio del tiempo de espera: "+str(tTotalEspera))


def main():
	global procesos
	numRondas = 0
	while(numRondas < 5):
		print "Ronda "+str(numRondas+1)
		spn(procesos,tLlegada)
		numRondas = numRondas +1

main()