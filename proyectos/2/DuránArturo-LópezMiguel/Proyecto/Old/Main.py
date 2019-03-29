from threading import Semaphore,Thread
from time import sleep

from Linea import *
from Tren import *
from Estacion import *

#Se crean las listas donde se almacenan los trenes (depósitos)

DepositoObservatorioL1=[]
DepositoPantitlanL1=[]

DepositoPolitecnicoL5=[]
DepositoPantitlanL5=[]

DepositoTacubayaL9=[]
DepositoPantitlanL9=[]

DepositoLaPazLA=[]
DepositoPantitlanLA=[]

Linea1 = [DepositoObservatorioL1, DepositoPantitlanL1 ]
Linea5 = [DepositoPolitecnicoL5,DepositoPantitlanL5 ]
Linea9 = [DepositoTacubayaL9, DepositoPantitlanL9 ]
LineaA = [DepositoLaPazLA, DepositoPantitlanLA]

Depositos=[Linea1, Linea5, Linea9, LineaA]

Lineas = ['L1','L5','L9','LA']


#Trenes disponibles segun las lineas
#          1  5  9  A
Trenes = [40,16,20,30]
def ControladorEstacion():
    return
def createMutex():
    return

def Avance(linea,deposito):
    return

def simulacion(dia_completo):
    bandera = True
    x=17900
    dia_semana=0
    dias=0
    hora_servicio_inicio = 5
    hora_servicio_fin = 24

    fin_semana = 0
    entre_semana = 0

    #Controla los avisos acerca del estado el metro
    aviso_inicio = True
    aviso_fin = True
    
    #### CREACION DE TRENES #########
    k=0  
    for i in Trenes:
        Lugar = 0
        for j in range(i):
            if j == int(i/2):
                Lugar = 1
            #Guardamos los trenes en sus respectivos depositos pero sin iniciar los hilos.
            nombreThread = Lineas[k]+'-'+str(j)
            Depositos[k][Lugar].append( Thread(target=Avance,args=(0,0),name=nombreThread ))
            print("Hilo ",nombreThread," creado")
        k+=1
    

    while bandera == True:
        t = x % dia_completo
        #Incrementa dia
        if x % dia_completo == 0:
            dia_semana = (dias+1)%7
            dias+=1
    
        hora_actual = int(t/3600)
        
        ####### ESTADO DEL METRO ######
        if hora_actual ==  hora_servicio_inicio and aviso_inicio :
            print("Abre el metro")
            aviso_inicio =  False
            #### Inicia labores de apertura ###############
            
        if  hora_actual ==  hora_servicio_fin and aviso_fin:
            print("Cierra el metro")
            aviso_fin = False
            #### Inicia labores de cierre ################
    
            
        print(t,"[s]")
        x+=1
        

    return

def main():
    dia_completo = 60*60*24 #[s]
    simulacion(dia_completo)
    return

main()
