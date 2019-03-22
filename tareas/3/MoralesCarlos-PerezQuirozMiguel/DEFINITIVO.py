import random

def gen_list():
    procesos = []
    diccionario = {0:'A',1:'B',2:'C',3:'D',4:'E'}
    num_procesos = 5
    llegada = 0
    for i in range(num_procesos):
        duracion = random.randint(1,8)
        procesos.append([diccionario[i],llegada,duracion])
        llegada += random.randint(0,duracion-1)
    return procesos

def FCFS(process_queue):
    n = len(process_queue)
    salida = ""
    Fin = [ 0 for i in range(n) ]
    T = [ 0 for i in range(n) ]
    E = [ 0 for i in range(n) ]
    P = [ 0 for i in range(n) ]
    t = [ process_queue[i][2] for i in range(n) ]
    #print 'Proceso\t\tInicio\t\tt\t\tFin\t\tT\t\tE\t\tP'
    for i in range(n):

        if i == 0:
            Fin[i] = process_queue[i][2]
        else:
            if process_queue[i][1] <= Fin[i-1]:
                Fin[i] = process_queue[i][2] + Fin[i-1]
            else:
                Fin[i] = process_queue[i][1] + process_queue[i][2]
        T[i] = Fin[i] - process_queue[i][1]
        E[i] = T[i] - process_queue[i][2]
        P[i] = float(T[i])/float(process_queue[i][2])
    #    print process_queue[i][0],'\t\t',process_queue[i][1],'\t\t',process_queue[i][2],'\t\t',Fin[i],'\t\t',T[i],'\t\t',E[i],'\t\t',P[i],'\t\t'

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

    print 'FCFS:   T = %.2f' % promedioT,'\t', 'E = %.2f' % promedioE,'\t', 'P = %.2f' % promedioP
    
    for i in range(n):
        for j in range(t[i]):
            salida += process_queue[i][0]
            
    print salida   

def RR1(process_queue):
    n = len(process_queue)
    #print n
    cola_procesos = []

    #process_queue.sort(key = lambda process_queue:process_queue[1]) #Se ordena la lista

    Fin = [ 0 for i in range(n) ]
    T = [ 0 for i in range(n) ]
    E = [ 0 for i in range(n) ]
    P = [ 0 for i in range(n) ]
    t = [ process_queue[i][2] for i in range(n) ]
    inicio = [ process_queue[i][1] for i in range(n) ]
    salida = ""
    tiempo_actual = 0 #Se utiliza para que los procesos entren en el tiempo que les toca.

    #print 'Proceso\t\tInicio\t\tt\t\tFin\t\tT\t\tE\t\tP'
    while any(tiempo != 0 for tiempo in t):
        for i in range(len(t)):
            if t[i] >= 1 and tiempo_actual >= inicio[i]:
                cola_procesos.append(process_queue[i][0])
                salida += process_queue[i][0]
                t[i] -= 1
                tiempo_actual += 1
            
    #for i in range(len(cola_procesos)):
    #    print cola_procesos[i]


    # Calculando Fin

    for i in range(n):
        aux = [ j for j in range(len(cola_procesos)) if cola_procesos[j] == process_queue[i][0] ]
        Fin[i] = aux[::-1][0] + 1 #Se voltea la lista y se obtiene el primer elemento que es el mayor, es decir, la ultima vez que aparece
        T[i] = Fin[i] - process_queue[i][1]
        E[i] = T[i] - process_queue[i][2]
        P[i] = float(T[i])/float(process_queue[i][2])

    #    print process_queue[i][0],'\t\t',process_queue[i][1],'\t\t',process_queue[i][2],'\t\t',Fin[i],'\t\t',T[i],'\t\t',E[i],'\t\t',P[i],'\t\t'

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
    print 'RR1:    T = %.2f' % promedioT,'\t', 'E = %.2f' % promedioE,'\t', 'P = %.2f' % promedioP
    print salida

def RR4(process_queue):
    n = len(process_queue)
    #print n
    cola_procesos = []

    #process_queue.sort(key = lambda process_queue:process_queue[1]) #Se ordena la lista

    Fin = [ 0 for i in range(n) ]
    T = [ 0 for i in range(n) ]
    E = [ 0 for i in range(n) ]
    P = [ 0 for i in range(n) ]
    t = [ process_queue[i][2] for i in range(n) ] #[0,5,2,5,5]
    inicio = [ process_queue[i][1] for i in range(n) ] #[0,1,3,9,12]
    salida = ''
    tiempo_actual = 0 #Se utiliza para que los procesos entren en el tiempo que les toca. 

    #print ('Proceso\t\tInicio\t\tt\t\tFin\t\tT\t\tE\t\tP')
    while any(tiempo != 0 for tiempo in t):
        for i in range(len(t)):
            if t[i] >= 4 and tiempo_actual >= inicio[i]:
                for j in range(4):
                    cola_procesos.append(process_queue[i][0])
                    salida += process_queue[i][0]
                tiempo_actual += 4
                t[i] -= 4
            elif t[i] < 4 and t[i] > 0 and tiempo_actual >= inicio[i]:
                for j in range(t[i]):
                    cola_procesos.append(process_queue[i][0])
                    salida += process_queue[i][0]
                tiempo_actual += t[i]
                t[i] = 0

    #for i in range(n):
    #    print t[i]

    # Calculando Fin

    for i in range(n):
        aux = [ j for j in range(len(cola_procesos)) if cola_procesos[j] == process_queue[i][0] ]
        Fin[i] = aux[::-1][0] + 1 #Se voltea la lista y se obtiene el primer elemento que es el mayor, es decir, la ultima vez que aparece
        T[i] = Fin[i] - process_queue[i][1]
        E[i] = T[i] - process_queue[i][2]
        P[i] = float(T[i])/float(process_queue[i][2])

        #print (process_queue[i][0],'\t\t',process_queue[i][1],'\t\t',process_queue[i][2],'\t\t',Fin[i],'\t\t',T[i],'\t\t',E[i],'\t\t',P[i],'\t\t')

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

    print 'RR4:    T = %.2f' % promedioT,'\t', 'E = %.2f' % promedioE,'\t', 'P = %.2f' % promedioP
    print salida
    #for i in range(len(cola_procesos)):
    #    print (cola_procesos[i])

def SPN(process_queue):
    sala_espera = []        #Aqui se guardan los procesos que llegan antes de que sea su turno

    arrival_time = 0
    time_requiered = 0
    start_time = 0
    finish_time = 0

    T = 0   #Tiempo Total actual
    E = 0   #Tiempo Espera actual
    P = 0   #Razon de Penaliacion actual

    Tsum = 0    #Tiempo Total promedio
    Esum = 0    #Tiempo Espera promedio
    Psum = 0    #Razon de Penalizacion promedio

    salida = ""     #Aqui se guarda el orden en que se ejecutaron los procesos

    for i in range (len(process_queue)):
        arrival_time = process_queue[i][1]      #Se registra tiempo de llegada
        time_requiered = process_queue[i][2]    #Se registra tiempo requerido
        if (arrival_time < finish_time):        #Se verifica si llega antes de que sea su turno
            sala_espera.append(process_queue[i])    #Se agrega a la sala de espera
            sala_espera.sort(key = lambda sala_espera:sala_espera[2])   #Se ponen los mas cortos al principio
        else:
            if (sala_espera):       #Se verifica si hay algun proceso esperando
                sala_espera.append(process_queue[i])    #Se agrega el proceso actual a la espera
                sala_espera.sort(key = lambda sala_espera:sala_espera[2])   #Se ponen el mas corto al principio
                arrival_time = sala_espera[0][1]        #Se registra tiempo de llegada
                time_requiered = sala_espera[0][2]      #Se registra el tiempo requerido
                for j in range (time_requiered):        #Se guarda el orden de ejecucion
                    salida+=(sala_espera[0][0])
                start_time = finish_time                #Se programa su tiempo de inicio
                E = start_time - arrival_time           #Se calcula tiempo perdido
                Esum = Esum + E
                T = time_requiered + E                  #Se calcula tiempo total
                Tsum = Tsum + T
                P = T/time_requiered                    #Se calcula razon de respuesta
                Psum = Psum + P
                finish_time = start_time + time_requiered   #Se calcula tiempo de fin
                sala_espera.pop(0)
                #print (sala_espera)
                #print ('S: %d' %start_time, 'F: %d' %finish_time, 'T: %d' % T, 'M: %d' % E, 'P: %.2f' % P)
            else:
                for j in range (time_requiered):        #Se guarda el orden de ejecucion
                    salida+=(process_queue[i][0])
                start_time = finish_time                #Se programa su tiempo de inicio
                E = start_time - arrival_time           #Se calcula tiempo perdido
                Esum = Esum + E
                T = time_requiered + E                  #Se calcula tiempo total
                Tsum = Tsum + T
                P = T/time_requiered                    #Se calcula razon de respuesta
                Psum = Psum + P
                finish_time = start_time + time_requiered   #Se calcula tiempo de fin
                #print ('S: %d' %start_time, 'F: %d' %finish_time, 'T: %d' % T, 'M: %d' % E, 'P: %.2f' % P)
#Se vacia la sala de espera
    for i in range (len(sala_espera)):          
        arrival_time = sala_espera[i][1]        #Se registra tiempo de llegada
        time_requiered = sala_espera[i][2]
        for j in range (time_requiered):        #Se guarda el orden de ejecucion
            salida+=(sala_espera[i][0])
        start_time = finish_time                #Se programa su tiempo de inicio
        E = start_time - arrival_time           #Se calcula tiempo perdido
        Esum = Esum + E
        T = time_requiered + E                  #Se calcula tiempo total
        Tsum = Tsum + T
        P = T/time_requiered                    #Se calcula razon de respuesta
        Psum = Psum + P
        finish_time = start_time + time_requiered   #Se calcula tiempo de fin
        #print ('S: %d' %start_time, 'F: %d' %finish_time, 'T: %d' % T, 'M: %d' % E, 'P: %.2f' % P)

    promedioT = float(Tsum) / float(len(process_queue))

    promedioE = float(Esum) / float(len(process_queue))

    promedioP = float(Psum) / float(len(process_queue))

    print 'SPN:    T = %.2f' % promedioT,'\t', 'E = %.2f' % promedioE,'\t', 'P = %.2f' % promedioP
    print salida

pasadas = 20    #Indica el numero de ejecuciones deseadas
for i in range (pasadas):
    print 'Ronda %d' %i
    process_queue = gen_list()
    print 'Lista de procesos llegados:', process_queue
    FCFS(process_queue)
    RR1(process_queue)
    RR4(process_queue)
    SPN(process_queue)