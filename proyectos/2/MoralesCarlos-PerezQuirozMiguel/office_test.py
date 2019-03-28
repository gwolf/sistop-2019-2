from threading import Semaphore, Thread
from time import sleep
from random import random, randint

workers_queue = []
workers_count = 0
workers_dictionary = {
            0:"Roberto",
            1:"Carolina",
            2:"Miguel",
            3:"Carlos",
            4:"Jehosua",
            5:"Beatriz",
            6:"Luis",    
            7:"Jorge",
            8:"Armando",
            9:"Max"
        }
quantum = 2

cubicles = Semaphore(8)
def lets_work():
        ## Simula dos horas de trabajo en el cubículo
        aux = workers_queue.pop(0)
        cubicles.release()
        time = aux[1]
        worker_id = aux[0]
        if (time > 0):
                time -= quantum
                sleep(random())
                Thread(target = worker_wait, args = [worker_id,time]).start()
    
def worker_wait(num, tiempo):
        ## Se agregan a una lista de procesos listos
        # workers_count += 1
        cubicles.acquire()
        workers_queue.append([num, tiempo])
        print ("Trabajador %s listo." %workers_dictionary[num], "Me faltan %d horas" %tiempo)
        ## Un trabajador adquiere un cubículo
        #print (workers_queue)


#Horas que trabajan los distintos tipos de trabajadores.

times = [6,8,12]
def get_time():
    global times
    aux = randint(0,2)
    return times[aux]

def gen_workers():
        for i in range(10):
                total = get_time()
                sleep(random())
                Thread(target = worker_wait, args = [i,total]).start()

def office():
        gen_workers()
        while (workers_queue):
                #print(workers_queue)
                lets_work()
                

office()
