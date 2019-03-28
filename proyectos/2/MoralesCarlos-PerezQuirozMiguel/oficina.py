import threading, random

cuantum_cubiculo = 2
cubiculos_ocupados = 0
llave_cubiculo = threading.Semaphore(1) #Se crea un mutex como llave del cubiculo
 


# 'A' - Trabajador de medio tiempo
# 'B' - Trabajador de tiempo completo
# 'C' - Trabajador suicida

tipos = ( 'A', 'B','C' )

def usar_cubiculo():
    llave_cubiculo.acquire()


def oficina(lista_trabajadores):
    pass
 
def trabajador(id,tipo):
    hora_llegada = random.randint(0,24)
    if tipo == 'A':
        tiempo = 6
    elif tipo == 'B':
        tiempo = 8
    elif tipo == 'C':
        tiempo = 12
    else:
        print("Tipo de trabajador no considerado")
    trabajador = [ id,hora_llegada,tiempo ]
    print(trabajador)
    return trabajador

def tipo_trabajador():
    aux = random.randint(0,2)
    tipo = tipos[aux] 
    print (tipo)
    return tipo

#print(trabajador(tipo_trabajador()))
lista_trabajadores = [] 
for i in range(0,10):
    lista_trabajadores.append(trabajador(i,tipo_trabajador()))

lista_trabajadores.sort(key = lambda lista_trabajadores:lista_trabajadores[1]) #Se ordena la lista
print(lista_trabajadores)



##############################################################
#  ROUND ROBIN 4, pero se tiene que adaptar a ROUND ROBIN 5 # 
##############################################################








#Round Robin con q = 4

#process_queue = [['A',0,3],['B',1,5],['C',3,2],['D',9,5],['E',12,5]]
#process_queue = [['p1',0,4],['p2',1,5],['p3',2,2],['p4',3,1],['p5',4,6],['p6',6,3]]
process_queue = lista_trabajadores
n = len(process_queue)
cola_procesos = []

process_queue.sort(key = lambda process_queue:process_queue[1]) #Se ordena la lista

Fin = [ 0 for i in range(n) ]
T = [ 0 for i in range(n) ]
E = [ 0 for i in range(n) ]
P = [ 0 for i in range(n) ]
t = [ process_queue[i][2] for i in range(n) ] #[0,5,2,5,5]
inicio = [ process_queue[i][1] for i in range(n) ] #[0,1,3,9,12]

tiempo_actual = 0 #Se utiliza para que los procesos entren en el tiempo que les toca. 

print ( 'Proceso\t\tInicio\t\tt\t\tFin\t\tT\t\tE\t\tP' )
while any(tiempo != 0 for tiempo in t):
    for i in range(len(t)):
        if t[i] >= 4 and tiempo_actual > inicio[i]:
            for j in range(4):
                cola_procesos.append(process_queue[i][0])
            tiempo_actual += 4
            t[i] -= 4
        elif t[i] < 4 and t[i] > 0 and tiempo_actual >= inicio[i]:
            for j in range(t[i]):
                cola_procesos.append(process_queue[i][0])
            tiempo_actual += t[i]
            t[i] = 0
        else:
            t[i] = 0
            tiempo_actual += t[i]


#for i in range(n):
#    print t[i]

for i in range(len(cola_procesos)):
    print ( cola_procesos[i] )


# Calculando Fin

for i in range(n):
    aux = [ j for j in range(len(cola_procesos)) if cola_procesos[j] == process_queue[i][0] ]
    Fin[i] = aux[::-1][0] + 1 #Se voltea la lista y se obtiene el primer elemento que es el mayor, es decir, la ultima vez que aparece
    T[i] = Fin[i] - process_queue[i][1]
    E[i] = T[i] - process_queue[i][2]
    P[i] = float(T[i])/float(process_queue[i][2])

    print ( process_queue[i][0],'\t\t',process_queue[i][1],'\t\t',process_queue[i][2],'\t\t',Fin[i],'\t\t',T[i],'\t\t',E[i],'\t\t',P[i],'\t\t' )

suma = 0
for i in range(n):
    suma += T[i]
promedioT = float(suma) / float(n)
suma = 0
for i in range(n):
    suma += E[i]
promedioE = float(suma) / float(n)
suma = 0 
for i in range(n):
    suma += P[i]
promedioP = float(suma) / float(n)

print ('RR1:    T = %.2f' % promedioT,'\t', 'E = %.2f' % promedioE,'\t', 'P = %.2f' % promedioP ) 

