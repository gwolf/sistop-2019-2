from tools.Peticion import Peticion
from tools.Analisis import Analisis
from operator import itemgetter
import threading
import time
import json

class Singleton(type): #Evita que en algun caso extremo exista otra instancia de la clase en ejecucion
    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)

    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args,**kw)
        return cls.__instance

class Estres(Peticion):
    __metaclass__ = Singleton
    def __init__(self,hilos,tiempo,url,payload,tipo,headers,auth,archivo,archivoRespuestas):
        self.__instance = None #Parte de la implementacion del Singleton
        self.hilos = int(hilos)
        self.tiempo = tiempo
        if(self.tiempo != None):
            self.horaFinal = time.time() + int(self.tiempo) # Si se especifica el tiempo se le suma a la hora del sistema el tiempo especificado
        self.horaFinal = None
        self.file = archivo
        self.archivoRespuestas = archivoRespuestas
        Peticion.__init__(self,url,payload,tipo,headers,auth) # Se pasan los parametros que corresponden a la clase padre
        self.respuestas = [] 
        self.finished = threading.Semaphore(1)
        self.mutex_cont = threading.Semaphore(1)
        self.barrier = threading.Semaphore(0) # se crean los semaforos correspondientes 

    def crearAnalisis(self): # Este metodo retorna el analisis final de las respuestas del servidor
        analizador = Analisis() 
        respuestas = sorted(self.respuestas, key=itemgetter('timeDate'), reverse=True)
        self.respuestas = []
        for respuesta in respuestas:
            analizador.times.append(respuesta["tiempoPeticion"])
            analizador.state_codes.append(respuesta["code"])
            analizador.estados.append(respuesta["estado"])
            analizador.fechas.append(respuesta["timeDate"])
        analizador.analizar_tiempo()
        analizador.analizar_estados()
        analizador.analizar_state_codes()
        return analizador

    def iniciarHilos(self, mutex): # Este metodo crea e inicializa los procesos
        if(self.tiempo != None):
            self.horaFinal = time.time() + int(self.tiempo)
        print("guardado:"+self.archivoRespuestas)
        output = open(self.archivoRespuestas+".txt","w") # Toma la variable del archivo y la abre
        if(self.tipo == "POST"): # si se usa el metodo POST
            self.finished.acquire() # Se inicia un mutex que impide la escritura antes de la finalizacion de los procesos
            if(self.file == None): #Si no se definio un archivo a enviar se envia con metodo post normal
                num_respuestas = 0 # Se inicializa una variable que acumula el numero de respuestas esperadas
                while(self.esperarTiempo()):
                    num = 0 # se inicializa en 0 el contador para la barrera 
                    num_respuestas = num_respuestas + self.hilos # en cada iteracion se aumenta por el numero de hilos concurrentes
                    for i in range(self.hilos):
                        thread = threading.Thread(target = self.post, args = (self.respuestas,),name=str(i+1)+" peticion")
                        thread.start() #adentro se libera el mutex
                        self.mutex_cont.acquire()
                        num = num + 1 #se proteje el contador con este mutex
                        self.mutex_cont.release()
                    if num == self.hilos:
                        for i in range(self.hilos):
                            self.barrier.release() #Se libera la barrear
                        num = 0 #Se reinicializa el contador para otra barrera
                    self.barrier.acquire()
                    if (self.tiempo==None): # Si no se define tiempo se terminara el while inmediatamente
                        break
                while len(self.respuestas) < num_respuestas and self.esperarTiempo():
                    pass
                self.escribirRespuestas(output)
                self.finished.release()
            else:
                num_respuestas = 0
                while(self.esperarTiempo()):
                    num = 0
                    num_respuestas = num_respuestas + self.hilos
                    for i in range(self.hilos):
                        thread = threading.Thread(target = self.postFile, args = (self.respuestas,),name=str(i+1)+" peticion")
                        thread.start()
                        self.mutex_cont.acquire()
                        num = num + 1 #se proteje el contador con este mutex
                        self.mutex_cont.release()
                    if num == self.hilos:
                        for i in range(self.hilos):
                            self.barrier.release()
                        num = 0
                    self.barrier.acquire()
                    if (self.tiempo==None):
                        break
                while len(self.respuestas) < num_respuestas and self.esperarTiempo():
                    pass
                self.escribirRespuestas(output)
                self.finished.release()
        elif(self.tipo == "GET"): # apartir de aqui el proceso es igual solo que con metodos diferentes
            self.finished.acquire()
            num_respuestas = 0
            while(self.esperarTiempo()):
                num = 0
                num_respuestas = num_respuestas + self.hilos
                for i in range(self.hilos):
                    thread = threading.Thread(target = self.get, args = (self.respuestas,),name=str(i+1)+" peticion")
                    thread.start()
                    self.mutex_cont.acquire()
                    num = num + 1 #se proteje el contador con este mutex
                    self.mutex_cont.release()
                if num == self.hilos:
                    for i in range(self.hilos):
                        self.barrier.release()
                    num = 0
                self.barrier.acquire()
                if (self.tiempo==None):
                    break
            while len(self.respuestas) < num_respuestas and self.esperarTiempo():
                pass
            self.escribirRespuestas(output)
            self.finished.release()
        elif(self.tipo == "PUT"):
            self.finished.acquire()
            num_respuestas = 0
            while(self.esperarTiempo()):
                num = 0
                num_respuestas = num_respuestas + self.hilos
                for i in range(int(self.hilos)):
                    thread = threading.Thread(target = self.put, args = (self.respuestas,),name=str(i+1)+" peticion")
                    thread.start()
                    self.mutex_cont.acquire()
                    num = num + 1 #se proteje el contador con este mutex
                    self.mutex_cont.release()
                if num == self.hilos:
                    for i in range(self.hilos):
                        self.barrier.release()
                    num = 0
                self.barrier.acquire()
                if (self.tiempo==None):
                    break
            while len(self.respuestas) < num_respuestas and self.esperarTiempo():
                pass
            self.escribirRespuestas(output)
            self.finished.release()
        elif(self.tipo == "DELETE"):
            self.finished.acquire()
            num_respuestas = 0
            while(self.esperarTiempo()):
                num = 0
                num_respuestas = num_respuestas + self.hilos
                for i in range(int(self.hilos)):
                    thread = threading.Thread(target = self.delete, args = (self.respuestas,),name=str(i+1)+" peticion")
                    thread.start()
                    self.mutex_cont.acquire()
                    num = num + 1 #se proteje el contador con este mutex
                    self.mutex_cont.release()
                if num == self.hilos:
                    for i in range(self.hilos):
                        self.barrier.release()
                    num = 0
                self.barrier.acquire()
                if (self.tiempo==None):
                    break
            while len(self.respuestas) < num_respuestas and self.esperarTiempo():
                pass
            self.escribirRespuestas(output)
            self.finished.release()
        elif(self.tipo == "HEAD"):
            self.finished.acquire()
            num_respuestas = 0
            while(self.esperarTiempo()):
                num = 0
                num_respuestas = num_respuestas + self.hilos
                for i in range(int(self.hilos)):
                    thread = threading.Thread(target = self.head, args = (self.respuestas,),name=str(i+1)+" peticion")
                    thread.start()
                    self.mutex_cont.acquire()
                    num = num + 1 #se proteje el contador con este mutex
                    self.mutex_cont.release()
                if num == self.hilos:
                    for i in range(self.hilos):
                        self.barrier.release()
                    num = 0
                self.barrier.acquire()
                if (self.tiempo==None):
                    break
                while len(self.respuestas) < num_respuestas and self.esperarTiempo():
                    pass
            self.escribirRespuestas(output)
            self.finished.release()
        elif(self.tipo == "OPTIONS"):
            self.finished.acquire()
            num_respuestas = 0
            while(self.esperarTiempo()):
                num = 0
                num_respuestas = num_respuestas + self.hilos
                for i in range(int(self.hilos)):
                    thread = threading.Thread(target = self.options, args = (self.respuestas,),name = str(i+1)+" peticion")
                    thread.start()
                    self.mutex_cont.acquire()
                    num = num + 1 #se proteje el contador con este mutex
                    self.mutex_cont.release()
                if num == self.hilos:
                    for i in range(self.hilos):
                        self.barrier.release()
                    num = 0
                self.barrier.acquire()
                if (self.tiempo==None):
                    break
                while len(self.respuestas) < num_respuestas and self.esperarTiempo():
                    pass
            self.escribirRespuestas(output)
            self.finished.release()
        else:
            pass
        output.close()
        mutex.release() #Libera el semaforo //SOLO UTIL EN MODO GUI
        return True

    def esperarTiempo(self):  # Este metodo da el valor al loop del tiempo que debe durar la prueba
        if(self.tiempo == None or time.time() <= self.horaFinal):
            return True
        return False
    
    def escribirRespuestas(self,archivo): # Este metodo escribe en el archivo las respuestas de la prueba
        self.respuestas = sorted(self.respuestas, key=itemgetter('timeDate'), reverse=True) #Acomoda la lista por orden de ejecucion
        with archivo as in_archivo:
            for respuesta in self.respuestas:
                in_archivo.write(str(respuesta)+"\n")
