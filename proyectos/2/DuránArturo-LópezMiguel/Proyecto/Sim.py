from threading import Semaphore,Thread
from time import sleep
import turtle


#from Linea import *
from Tren import *
from Estacion import *
from Carga import *

import queue 
from Mapa import *

################ MAPA #######################################
"""
Esta funcion fue pirateada de StackOverflow al tratar de resolver un problema descrito en:
https://stackoverflow.com/questions/19498447/multithreading-with-python-turtle
"""
def process_queue():
    while not graphics.empty():
        (graphics.get())(1)

    if threading.active_count() > 1:
        turtle.ontimer(process_queue, 100)

MapaCola = queue.Queue(106)

TurtleLinea=[turtle.Turtle(),turtle.Turtle(),turtle.Turtle(),turtle.Turtle()]
for i in range(40):
    TurtleLinea.append(turtle.Turtle())
"""
def process_queue():
    while not actions.empty():
        turtle, action, argument = actions.get()
        action(turtle, argument)

    if active_count() > 1:
        screen.ontimer(process_queue, 100)


screen = turtle.Screen()

image = "Resources/mapa_macabro_gif.gif"

screen.addshape(image)
fondo = turtle.shape(image)

turtle.setup(1483,737,0,0)
turtle.title("Mapa de control")
turtle.showturtle()
UI_LA = turtle.Turtle()

"""


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

NLineas = ['L1','L5','L9','LA']

#Trenes disponibles segun las lineas
#          1  5  9  A
Trenes = [40,16,20,30]

#Control del tiempo en la simulacion

IncrementoTiempo = 1
InicioSim = 5*60*60
Es_Fin = False


#Listas ( Lineas ) Con Estaciones ##################################
linea1 = []
linea5 = []
linea9 = []
lineaA = []

linea1 = cargarObject("Data/L1",linea1)
linea5 = cargarObject("Data/L5",linea5)
linea9 = cargarObject("Data/L9",linea9)
lineaA = cargarObject("Data/LA",lineaA)

LineasObj=[linea1,linea5,linea9,lineaA]

### Listas de Mutex ################################################
MutexL1P=[]
MutexL1N=[]

MutexL5P=[]
MutexL5N=[]

MutexL9P=[]
MutexL9N=[]

MutexLAP=[]
MutexLAN=[]

MutexLinea1=[MutexL1P,MutexL1N]
MutexLinea5=[MutexL5P,MutexL5N]
MutexLinea9=[MutexL9P,MutexL9N]
MutexLineaA=[MutexLAP,MutexLAN]

Mutexs=[MutexLinea1,MutexLinea5,MutexLinea9,MutexLineaA]

#Señalizaciones
SenializacionInicio=[Semaphore(0),Semaphore(0),Semaphore(0),Semaphore(0)]
#Variable tiempo
t=0
Hora = 5
Minuto = 0
#Variable de control de tiempos:
tiempo_salida=[5,5,5,5]
tiempo_minimo_restante = 3.3
def IniciadorLinea(linea):
    k=0
    while len(Mutexs[linea][0])>0 and  len(Mutexs[linea][1]) > 0:
        SenializacionInicio[linea].acquire()
        ## Inicia un tren (hilo)
        Mutexs[linea][0][k].start()
        Mutexs[linea][1][k].start()
        k+=1
        
        
    return
def createMutex(linea):
    print("Creando mutexs ",NLineas[linea])
    tam_linea = len(LineasObj[linea])
    num_mutex = (tam_linea * 2) - 4 
    for i in range(num_mutex):
        Mutexs[linea][0].append(Semaphore(1))
        Mutexs[linea][1].append(Semaphore(1))
    return


M = Semaphore(1)
O = Semaphore(1)

def TrenF(num_linea,i,Direccion):

    print("Funcion Tren ",i)
    print("Direccion ",Direccion)
    
    TrenAs = Tren(NLineas[num_linea],i,Direccion)
    
    longitud = len(Mutexs[num_linea][Direccion%2])
    
    longitud_E = len(LineasObj[num_linea])
    
    estacionid = (Direccion % longitud_E )

    #Variables Ascenso y Descenso
    Ascenso = 0
    Descenso = 0
    
    if Direccion < 0:
        estacionid -=1
    
    DepositoInicial = 0
    DepositoFinal = 0        
    if Direccion < 0 :
        DepositoInicial = 0
        DepositoFinal = 1
    else:
        DepositoInicial = 1
        DepositoFinal = 0
    
    for j in range(1,longitud):
        O.acquire()
        Mutexs[num_linea][Direccion%2][j].acquire()
        Mutexs[num_linea][Direccion%2][j-1].acquire()
        print("Agarró mutex ",j," ",j-1)
        if j%2==0:
            estacionid += Direccion*1
        #print("Estacion Id ",estacionid)
        EstacionActual = LineasObj[num_linea][estacionid]
        #printLineaA(estacionid,UI_LA,0)
        print("Estoy en la estacion ", EstacionActual.getNombreE() )
        print("Es la hora ",Hora,":",Minuto)
        
        #################### Ascenso Descenso #########################
        if j%2==0:
            tasa = EstacionActual.getNumPersonas(Hora+Minuto/60,Direccion,tiempo_salida[num_linea])
            print("Llegan ",tasa," personas")
            #Ascenso
            #Nuevas personas que llegan + Personas en la estacion que no abordaron
            Ascenso = int(random.uniform(tasa*0.7,tasa)) + EstacionActual.personasEnEstacion()
            print("Van a Subirse ",Ascenso," Personas")       
            #Descenso
            if TrenAs.isEmpty():
                Descenso = 0
            else:
                Descenso = int(random.uniform(0,0.7*TrenAs.getCapacidadActual()))
            print("Van a Descender ",Descenso," Personas")

            #Turu ru ¡¡¡Antes de entrar permita salir !!!!
            TrenAs.restUsuarios(Descenso)
            
            if Ascenso > TrenAs.getCapacidadRestante():
                TrenAs.addUsuarios(TrenAs.getCapacidadRestante())
                EstacionActual.addPersonasEstacion( TrenAs.getCapacidadRestante() - Ascenso )
            else:
                TrenAs.addUsuarios(Ascenso)
            print("Personas en tren ", TrenAs.getCapacidadActual())
        Mutexs[num_linea][Direccion%2][j-1].release()
        Mutexs[num_linea][Direccion%2][j].release()
        #El tren espera el tiempo de traslado y el tiempo que tarda en la estacion
        tiempo_en_estacion = random.uniform(0.2,1) #[minutos]
        tiempo_traslado = TrenAs.getvelocidad()/EstacionActual.getDistancia(Direccion)
        tiempo_traslado = random.uniform(0.7*tiempo_traslado,tiempo_traslado)
        tiempo_espera = tiempo_traslado + tiempo_en_estacion
        print("Tiempo total de espera ",tiempo_espera)
        MapaCola.put(lineaXY(estacionid,num_linea,turtle.Turtle()))
        sleep(tiempo_espera / IncrementoTiempo)
        O.release()
    ############ Destruye y crea un tren como en un campo de cuantico y sus fluctuaciones xD #############
    TrenNuevo = Tren(num_linea,i,Direccion*-1)
    Depositos[num_linea][DepositoFinal].append(TrenNuevo)    
    return

def CreacionTrenes(num_linea):
    print(num_linea)
    #### CREACION DE TRENES #########
    M = Semaphore(1)
    Total_trenes = Trenes[num_linea]
    lugar = 0
    direccion = -1
    for i in range(1,Total_trenes+1):
        if i == int(Total_trenes/2):
            lugar = 1
            direccion = 1
        #Guardamos los trenes en sus respectivos depositos pero sin iniciar los hilos.
        nombreThread = NLineas[num_linea]+'-'+str(i)
        #print(num_linea,i,direccion)
        Depositos[num_linea][lugar].append( Thread(target=TrenF,args=[num_linea,i,direccion],name=nombreThread ))
    return

#Gestiona  las salidas de la linea
MutexPrint = Semaphore(1)
def GestorDeLinea(num_linea):
    createMutex(num_linea)
    CreacionTrenes(num_linea)
    while not (len(Depositos[num_linea][0])==0 and len(Depositos[num_linea][1]) == 0):
        ActualD1 = Depositos[num_linea][0].pop(0)
        ActualD2 = Depositos[num_linea][1].pop(0)
        #print("len ",len(Depositos[num_linea][0]))
        ActualD1.start()
        ActualD2.start()
        #Calcula el tiempo de salida de cada tren
        
        ############### TASA GLOBAL DE LLEGADAS
        desviacion = random.uniform(3.5,6)
        tiempo_actual = Hora+ Minuto/60
        tasa_global = st.norm.pdf(tiempo_actual, 7.5, desviacion ) + st.norm.pdf(tiempo_actual, 18, desviacion)
        tasa_global = tasa_global*20*60
        ########################################
        
        tiempo_salida[num_linea] = 5 -  tasa_global*(tiempo_minimo_restante/800)
        
        #input()
        sleep(tiempo_salida[num_linea]/IncrementoTiempo)
    #MutexPrint.release()

    return
def run():
    
    global Hora
    global Minuto
    
    t=InicioSim

    #Crea Trenes
    
    #CreacionTrenes()
    
    Fin = 24*60*60
    
    L1=Thread(target=GestorDeLinea,args=[0],name='L1').start()
    L5=Thread(target=GestorDeLinea,args=[1],name='L5').start()
    L9=Thread(target=GestorDeLinea,args=[2],name='L9').start()
    LA=Thread(target=GestorDeLinea,args=[3],name='LA').start()
    
    Ventana = Mapa()
    Ventana.run() 
    
    while not (t == Fin):

        Hora = int(t/3600)
        Minuto = int((t % 3600)/60 )

        sleep(IncrementoTiempo/60)
        t+=IncrementoTiempo

        #print(Hora,":",Minuto)
    
    return

def SetVariables(Dia,Hora,Vel):
    IncrementoTiempo = Vel
    InicioSim = Hora*60*60
    if Dia >5:
        Es_Fin = True
    else:
        Es_Fin = True
    
    return
    

run()

#for i in linea5:
#    print(i.getNombreE())

#createMutex(1)
#screen.mainloop()

#turtle.exitonclick()

















