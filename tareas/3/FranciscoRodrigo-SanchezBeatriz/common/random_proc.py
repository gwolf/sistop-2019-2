import random

def rand_proc(num_proc):
    procesos = []
    for j  in range(0,num_proc):
        t_0 = random.randint(1,10+1)
        t =random.randint(1,10+1)
        procesos.append([j,t_0,t])

    return procesos
