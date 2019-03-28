import threading
import time

mutex = threading.Semaphore(1)
procesos = [['A', 'B', 'C', 'D', 'E'], [3, 5, 2, 5, 5], [0, 1, 3, 9, 12], [0, 0, 0, 0, 0]]
resultados = [['T', 'E', 'P'], [0, 0, 0], [0, 0, 0]]
tiempo_espera = procesos[2][0]
tiempo_total = 0

def proceso(proc_actual):
    global procesos
    actual = procesos[0][proc_actual]
    print "Ah llegado el proceso %s" %actual
    dura_proceso(proc_actual)
    
def dura_proceso(proc_actual):
    global procesos
    actual = procesos[0][proc_actual]
    tiempo_eje = procesos[1][proc_actual]
    mutex.acquire()
    tiempo_de_espera(proc_actual)
    print "Inicia ejecucion proceso %s" %actual
    time.sleep(tiempo_eje) 
    print "Termina ejecuacion proceso %s" %actual 
    mutex.release()

def lanza_proceso(proc_actual):
    global procesos
    tiempo_actual = procesos[2][proc_actual]
    time.sleep(tiempo_actual)
    threading.Thread(target=proceso, args=[proc_actual]).start()

def tiempo_de_espera(proc_actual):
    global tiempo_espera
    global tiempo_total
    tiempo_espera = tiempo_espera - procesos[2][proc_actual]
    print "El proceso %s espero %d segundos" %(procesos[0][proc_actual], tiempo_espera) 
    procesos[3][proc_actual] = tiempo_espera
    tiempo_espera = tiempo_espera + procesos[2][proc_actual]
    tiempo_espera = tiempo_espera + procesos[1][proc_actual]
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
