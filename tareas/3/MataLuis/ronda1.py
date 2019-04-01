import threading
import time

mutex = threading.Semaphore(1)
procesos = [['A', 'B', 'C', 'D', 'E'], [6, 10, 4, 9, 8], [0, 1, 4, 9, 12], [0, 0, 0, 0, 0], [6, 10, 4, 9, 8],]
resultados = [['T', 'E', 'P'], [0, 0, 0], [0, 0, 0]]
cola_ejecucion = []
tiempo_espera = procesos[2][0]
tiempo_total = 0
quantum = 1

def proceso(proc_actual):
    global procesos
    global cola_ejecuacion
    actual = procesos[0][proc_actual]
    print "Ah llegado el proceso %s" %actual
    cola_ejecucion.append(procesos[0][proc_actual])
    while procesos[4][proc_actual] > 0:
        dura_proceso(proc_actual)
        if (len(cola_ejecucion)>1):        
            time.sleep(quantum)
            procesos[3][proc_actual] = procesos[3][proc_actual] + 1
    cola_ejecucion.pop()
    
def dura_proceso(proc_actual):
    global procesos
    actual = procesos[0][proc_actual]
    mutex.acquire()
    print "Inicia ejecucion proceso %s" %actual
    time.sleep(quantum) 
    print "Termina ejecuacion proceso %s" %actual 
    procesos[4][proc_actual] = procesos[4][proc_actual] - 1      
    mutex.release()
     

def lanza_proceso(proc_actual):
    global procesos
    tiempo_actual = procesos[2][proc_actual]
    time.sleep(tiempo_actual)
    threading.Thread(target=proceso, args=[proc_actual]).start()

for i in range(len(procesos[0])):
    threading.Thread(target=lanza_proceso, args=[i]).start()
    
time.sleep(40)
def promedio():
    prom = 0
    num_max = len(procesos[0])
    for i in range (num_max):
        prom = prom + procesos[3][i]
    resultados[1][1] = prom
    prom = (float(prom) / 5.0)
    resultados[2][1] = prom
def tiempo():
    prom = 0
    num_max = len(procesos[0])
    for i in range (num_max):
        prom = prom + procesos[1][i]
    resultados[1][0] = prom + resultados[1][1]
    prom = prom + resultados[1][1]
    prom = (float(prom) / 5.0)
    resultados[2][0] = prom
def penalizacion():
    prom = 0
    num_max = len(procesos[0])
    for i in range (num_max):
        a = procesos[1][i] + procesos[3][i]
        a = (float(a) / procesos[1][i])
        prom = prom + a
    resultados[1][2] = "{0:.2f}".format(prom)
    prom = (float(prom) / 5.0)
    resultados[2][2] = "{0:.2f}".format(prom) 

promedio()
tiempo()
penalizacion()
print (resultados)

