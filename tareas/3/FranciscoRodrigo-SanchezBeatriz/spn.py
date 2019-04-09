from common.watcher import *
from common.mystats import *

def spn(procesos):
    tiempo = 1
    espera = [0]*len(procesos)
    tiempo_exe = []
    queue_preexec = []

    pos_inqueue = 0
    real_pos = 0

    for j in procesos:
        tiempo_exe.append(j[2])

    while proc_finalizado(procesos) != True:
        # vemos quien se puede agregara la cola de pre-ejecucion
        # de acuerdo a la variable tiempo
        for j in procesos:
            if j[1] == tiempo-1:
                queue_preexec.append(j)

        if len(queue_preexec) != 0:
            #sacar el menor
            pos_inqueue = elmenor(queue_preexec)

            #disminuir su tiempo
            queue_preexec[pos_inqueue][2] -= 1

            #aumentar espera de los otros procesos en la cola
            aumentEspera_deOtros(pos_inqueue,espera,queue_preexec,procesos)

            # si su tiempo es cero, sacamos de la cola
            if queue_preexec[pos_inqueue][2] <= 0:
                del queue_preexec[pos_inqueue]
        tiempo += 1

    estadisticas(tiempo_exe,espera,procesos)

if __name__ == '__main__':
    main()
