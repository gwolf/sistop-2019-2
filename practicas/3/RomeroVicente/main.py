import time
import signal
import sys

salida = 0
def salir(signum, frame):
    global salida
    salida = 1
    print("\nsaliendo del programa")
    sys.exit()
 
signal.signal(signal.SIGINT, salir)

if __name__ == "__main__":
    while salida == 0:
        timer = time.time()
        print(timer)
        with open("log.txt","a") as outfile:
            outfile.write("hora actual:"+str(timer)+"\n")