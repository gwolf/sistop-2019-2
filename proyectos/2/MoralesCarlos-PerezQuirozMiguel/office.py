from threading import Semaphore, Thread
from time import sleep
from random import random, randint
import colorama

#Diccionario para generar los nombres de trabajadores
workers_dictionary = {
                0:"Roberto",
                1:"Kenny\t",
                2:"Miguel\t",
                3:"Carlos\t",
                4:"Jehosua",
                5:"Beatriz",
                6:"Luis\t",    
                7:"George\t",
                8:"Armando",
                9:"Max\t"
        }

#Diccionario de simbolos para generar la linea de control de trabajo de la oficina
symbols_dictionary = {
                0:"R",
                1:"K",
                2:"M",
                3:"C",
                4:"J",
                5:"B",
                6:"L",    
                7:"G",
                8:"A",
                9:"M"
        }

#Lista de colores para que se vea bonito
colors_dictionary = [
        colorama.Fore.CYAN,
        colorama.Fore.RED,
        colorama.Fore.LIGHTBLUE_EX,
        colorama.Fore.GREEN,
        colorama.Fore.BLUE,
        colorama.Fore.LIGHTRED_EX,
        colorama.Fore.YELLOW,
        colorama.Fore.MAGENTA,
        colorama.Fore.LIGHTGREEN_EX,
        colorama.Fore.LIGHTCYAN_EX
]

times = [6,8,12] #Horas que trabajan los distintos tipos de trabajadores.

#Se utiliza para mostrar el progrso de ejecución
progress_bar = [ '' for i in range (11) ]
workers_queue = []      #Lista de procesos listos
quantum = 2             #Parte del RoundRobin
cubicles = Semaphore(8) #Multiplex para cuando no hay cubiculos

def lets_work():
        # Simula dos horas de trabajo en el cubículo
        aux = workers_queue.pop(0)      #Guarda el siguiente proceso listo
        cubicles.release()              #Se libera un cubículo
        time = aux[1]                   
        worker_id = aux[0]
        if (time > 0):          #Si el trabajador aún no cumple sus horas
                time -= quantum #Se disminuyen las horas restantes del trabajador
                sleep(.1)
                progress_bar[worker_id] = progress_bar[worker_id] + '****' #Se agregan por cada horas de trabajo
                progress_bar[10] = progress_bar[10] + symbols_dictionary[worker_id] + symbols_dictionary[worker_id]
                #Se imprime salida
                print(colorama.ansi.clear_screen())
                print(colorama.Style.RESET_ALL)
                print ("Linea de control de trabajo de la oficina\n" +  progress_bar[10] + "\n")
                for i in range (10):
                        print(colors_dictionary[i] + "%s \t" %workers_dictionary[i] + "%s" %progress_bar[i])
                        print(colorama.Style.RESET_ALL)
                #Se agrega el trabajador a la lista de procesos listas
                Thread(target = worker_wait, args = [worker_id,time]).start()

def worker_wait(worker_id, time):
        #Agrega un trabajador a la lista de procesos listos
        cubicles.acquire()
        workers_queue.append([worker_id, time])

def get_time():
        #Genera las duracion de las jornadas de trabajo
        global times
        aux = randint(0,2)
        return times[aux]

def gen_workers():
        #Se generan 10 trabajadores
        for i in range(10):
                total = get_time()
                Thread(target = worker_wait, args = [i,total]).start()

def office():
        #Programa principal
        gen_workers()
        while (workers_queue):
                #print(workers_queue)
                lets_work()

#Se lanza programa principal        
office()
