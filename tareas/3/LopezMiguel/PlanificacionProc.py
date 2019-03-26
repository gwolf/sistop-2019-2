import random

class Process:
    PID=str()
    t=0
    t_A=0
    def __init__(self,PID,tiempo_req):
        self.PID=PID
        self.t=tiempo_req
    def getPID(self):
        return self.PID
    def getT(self):
        return self.t
    def tpp(self):
        self.t_A+=1
    def isComplete(self):
        return self.t_A == self.t -1
    def getTA(self):
        return self.t_A
    def setTA(self):
        self.t_A=0
        

def Format(llegada,t,proc,Ini,Fin,T,E,P):
    print('{:<10}|{:<12}|{:10}|{:<10}|{:<10}|{:<10}|{:<10}|{:<10.2f}'.format(llegada,t,proc,Ini,Fin,T,E,P))
def FCFS_Tabla(Procesos):
    Inicio=0
    Fin=0
    T=0
    E=0
    P=0
    k=0
    PromT=0
    PromE=0
    PromP=0
    print('FCFS')
    print('{:10}|{:12}|{:10}|{:10}|{:10}|{:10}|{:10}|{:10}'.format('Llegada','Tiempo_Req','Proceso','Inicio','Fin','T','E','P'))
    
    for i in Procesos:
        #i[1] =  i[0].getT()
        #i[0]= i[1]
        Fin=Inicio+i[0].getT()
        
        T=Fin-i[1]
        PromT+=T

        E=T-i[0].getT()
        PromE+=E
        
        P=T/i[0].getT()
        PromP+=P
        Format(i[1],i[0].getT(),chr(k+65),Inicio,Fin,T,E,P)
        Inicio+=i[0].getT()
        k+=1
    print('-'*88)
    n=len(Procesos)
    print('{:10} {:12} {:10} {:10} {:10}|{:<10.2f}|{:<10.2f}|{:<10.2f}'.format('Promedio','','','','',PromT/n,PromE/n,PromP/n))
    return
def FCFS(Procesos):
    print("FCFS")
    while(len(Procesos)>0):
        Actual=Procesos[0][0]
        if Actual.isComplete():
            Procesos.pop(0)     
        print(Actual.getPID(),end='')
        Actual.tpp()
    print()
    return
#Funcion Auxiliar par SPN
#Identifica el proceso para realizar operaciones (promedios)
def IndexProces(Proceso,Procesos):
    k=0
    for i in Procesos:
        if Proceso is i[0]:
            return k
        k+=1
    return
def RoundRobin(Procesos,Q):
    print("Round Robin ",Q)
    t=0
    L=list()
    i=1
    L.append(Procesos[0][0])
    CC=True
    #Medidas
    T=0
    E=0
    P=0
    while(len(L)>0):
        
   
        if i<len(Procesos) and Procesos[i][1] == t:
            L.append(Procesos[i][0])
            i+=1
            
        Actual=L[0]
        
        if Actual.getTA()% Q == 0 and CC:
            Aux=L.pop(0)
            L.append(Aux)  

        Actual=L[0]
        CC=True
        if Actual.isComplete():
            #Calculo de las metricas
            indice=IndexProces(Actual,Procesos)
            TA=((t+1)- Procesos[indice][1] )
            T+=TA
            E+=TA-Actual.getT()
            P+=TA/Actual.getT()
            L.pop(0)
            CC=False

        print(Actual.getPID(),end='')
        Actual.tpp()
        t+=1
    
    #Impresion de las metricas
    print()
    print("T: ",T/len(Procesos),end="")
    print("\tE: ",E/len(Procesos),end="")
    print("\tP: {:.2f}".format(P/len(Procesos)),end="")
    print()
    return
#Funcion Auxiliar para establecer en zeros las copias de las listas de objetos de procesos
def setZeros(P):
    for i in P:
        i[0].setTA()
    return

#Calcula el proceso mas corto para SPN
"""
A diferencia de lo que vimos en clase, lo que hice aqui fue ver, de la lista de procesos cual es el que requiere menos tiempo y ese
asignarlo a el proceso "Actual" que se esta ejecutando. Se que el despachador en este caso estima la duracion del proceso
pero en este caso por simplicidad, el algoritmo sabe cuanto dura un proceso y le da preferencia.
"""
def CalcMinSPN(Procesos):
    Tiempos=list()
    for i in Procesos:
        Tiempos.append((i.getT()) - (i.getTA()))
    minimo=min(Tiempos)
    indice=Tiempos.index(minimo)

    Preferente = Procesos.pop(indice)
    Procesos.insert(0,Preferente)
    
    return Procesos[0]
def SPN(Procesos):
    print("SPN")
    t=0
    L=list()
    i=1
    L.append(Procesos[0][0])
    #Medidas
    T=0
    E=0
    P=0  
    while(len(L)>0):
        if i<len(Procesos) and Procesos[i][1] == t:
            L.append(Procesos[i][0])
            i+=1

        Actual=CalcMinSPN(L)
    
        if Actual.isComplete():
            #Calculo de las metricas
            indice=IndexProces(Actual,Procesos)
            TA=((t+1)- Procesos[indice][1] )
            T+=TA
            E+=TA-Actual.getT()
            P+=TA/Actual.getT()
            
            L.pop(0)

        print(Actual.getPID(),end='')
        Actual.tpp()
        t+=1
    #Impresion de las metricas
    print()
    print("T:",T/len(Procesos),end="")
    print("\tE:",E/len(Procesos),end="")
    print("\tP:{:.2f}".format(P/len(Procesos)),end="")
    print()
    return
#Funcion que genera las listas aleatorias 
def RandomP(max_proc,max_duracion):
    Procesos=list()

    duracion = random.randrange(2,max_duracion)
    llegada = 0

    Procesos.append( (Process('A',duracion),llegada) )
    llegada_ant=llegada
    for i in range(1,max_proc):
        
        llegada = random.randrange(llegada,llegada+duracion)
        if llegada==llegada_ant:
            llegada+=1
        duracion = random.randrange(1,max_duracion)      
        Procesos.append( (Process(chr(i+65),duracion),llegada) )
        llegada_ant=llegada
    return Procesos

def Print_List(Procesos):
    for i in Procesos:
        print(" {}: {}, t={};".format(i[0].getPID(),i[1],i[0].getT() ),end='' )
    print()
    return

def main():
    print("Carga Ejemplo")
    P=[(Process('A',3),0),(Process('B',5),1),(Process('C',2),3),(Process('D',5),9),(Process('E',5),12)]
    Print_List(P)
    P2=P.copy()
    P3=P.copy()
    P4=P.copy()
    
    FCFS_Tabla(P)
    FCFS(P)
    
    setZeros(P2)
    RoundRobin(P2,1)
    
    setZeros(P3)
    RoundRobin(P2,4)
    
    setZeros(P4)
    SPN(P4)

    ##RANDOM
    max_duracion=10
    max_procesos=10
    rondas=5
    for i in range(rondas):
        print('#'*50+" Carga " + str(i)+'#'*50)
        PR=RandomP(max_procesos,max_duracion)
        Print_List(PR)
        
        PR2=PR.copy()
        PR3=PR.copy()
        PR4=PR.copy()        
        FCFS_Tabla(PR)
        FCFS(PR)
        
        setZeros(PR2)
        RoundRobin(PR2,1)
        
        setZeros(PR3)
        RoundRobin(PR2,4)
        
        setZeros(PR4)
        SPN(PR4)        

    return

main()


