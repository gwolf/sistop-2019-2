from fcfs import fcfs
from rr import round_robin
from rr4 import round_robin4
from spn import spn
from common.random_proc import rand_proc

import sys

def main():

    proc_num = 4
    rondas = 2

    # Si el usuario pasa mal los parametros ponemos unos por defecto
    if len(sys.argv) == 3:
        proc_num = int(sys.argv[1])
        rondas = int(sys.argv[2])
    else :
        print("Algo salió mal con los param. así que usaremos unos por defecto")

    print("Número de procesos : %d" %proc_num)
    print("Número de rondas : %d" %rondas)

    for ronda in range(0,rondas):
        print("----------------------------------------------\n")
        print("RONDA %d \n" %(ronda+1))

        print("Los procesos generados aleatoriamente son :")

        procesos = rand_proc(proc_num)
        for j in procesos:
            print("id: %d, t_arrived = %d, t = %d" %(j[0],j[1],j[2]))

        print("Realizando fcfs...")
        # Pasando una copia de procesos a fcfs...
        fcfs([sublista[:] for sublista in procesos[:]])

        print("Realizando Round Robin...")
        # Pasando una copia de procesos a spn...
        round_robin([sublista[:] for sublista in procesos[:]])

        print("Realizando Round Robin 4...")
        # Pasando una copia de procesos a spn...
        round_robin4([sublista[:] for sublista in procesos[:]],4)

        print("Realizando spn...")
        # Pasando una copia de procesos a spn...
        spn([sublista[:] for sublista in procesos[:]])

if __name__ == '__main__':
    main()
