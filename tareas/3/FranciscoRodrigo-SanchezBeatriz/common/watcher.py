def buscarId(id, procesos):
    for i in range(len(procesos)):
        if id == procesos[i][0]:
            return i
    return -1

def aumentEspera_deOtros(pos_inqueue,espera,queue_preexec,procesos):
    for j in range(len (queue_preexec)):
        if pos_inqueue != j: # y ademas asegurar que ya no esta
            real_pos = buscarId(queue_preexec[j][0],procesos)
            espera[real_pos] +=1

def proc_finalizado(procesos):
    finalizado = 0
    for i in procesos:
        if i[2] == 0:
            finalizado += 1
    if finalizado == len(procesos):
        return True
    return False

def elmenor(queue):
    menor = queue[0][2]
    pos = 0
    for j in range(0,len(queue)):
        if queue[j][2] < menor:
            menor = queue[j][2]
            pos = j
    return pos
