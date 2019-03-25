import requests
import threading
from multiprocessing import Queue
import time
import sys
from analisis import analisis
import time

def getj(n,e):
    inicio = time.time()
    try:
        r = requests.get('http://localhost:5000/ranking/314144799')
        fin = time.time()
        tiempo = fin - inicio
        n.append(tiempo)
        e.append("exito")
        #print(str(n) + str(r.json()))
    except Exception as inst:
        print(inst)
        print(type(inst))
        fin = time.time()
        tiempo = fin - inicio
        n.append(tiempo)
        e.append("fallo")

    if __name__ == "__main__":
    tiempo= []
    estatus = []
    intentos = sys.argv[1]
    global exito, fallo
    exito, fallo  = 0, 0
    for i in range (int(intentos)):
        thread = threading.Thread(target = getj, args=(tiempo,estatus))
        thread.start()
    thread.join()
    fallo = 0
    exito = 0
    suma = 0
    intentos = len(estatus)
    for i in range (int(intentos)):
        if(estatus[i] == "fallo"):
            fallo = fallo + 1
        else:
            exito = exito + 1
        suma = suma + tiempo[i]
    promedio = suma/int(intentos)
    f = open ("log","a")
    f.write("\n{4} {3} exitos: {0} fallo: {1} promedio: {2}".format(exito,fallo,promedio,sys.argv[2],time.strftime("%c")))
    f.close()
    print(tiempo)
    print(promedio)
main()
