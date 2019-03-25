from tools.Peticion import Peticion
from tools.analisis import Analisis
from operator import itemgetter
import threading
import time
import json

class Singleton(type):
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
        self.__instance = None
        self.hilos = hilos
        self.tiempo = tiempo
        if(self.tiempo != None):
            self.horaFinal = time.time() + int(self.tiempo)
        self.horaFinal = None
        self.file = archivo
        self.archivoRespuestas = archivoRespuestas
        Peticion.__init__(self,url,payload,tipo,headers,auth)
        self.respuestas = []
        self.finished = False

    def crearAnalisis(self):
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

    def iniciarHilos(self):
        if(self.tiempo != None):
            self.horaFinal = time.time() + int(self.tiempo)
        print("guardado:"+self.archivoRespuestas)
        output = open(self.archivoRespuestas+".txt","w")
        if(self.tipo == "POST"):
            if(self.file == None):
                while(self.esperarTiempo()):
                    for i in range(int(self.hilos)):
                        thread = threading.Thread(target = self.post, args = (self.respuestas,),name=str(i+1)+" peticion")
                        thread.start()
                    thread.join()
                    self.esperarCompletos()
                    if (self.tiempo == None):
                        break
                self.escribirRespuestas(output)
            else:
                while(self.esperarTiempo()):
                    for i in range(int(self.hilos)):
                        thread = threading.Thread(target = self.postFile, args = (self.respuestas,),name=str(i+1)+" peticion")
                        thread.start()
                    thread.join()
                    self.esperarCompletos()
                    if (self.tiempo == None):
                        break
            self.escribirRespuestas(output)
        elif(self.tipo == "GET"):
            while(self.esperarTiempo()):
                for i in range(int(self.hilos)):
                    thread = threading.Thread(target = self.get, args = (self.respuestas,),name=str(i+1)+" peticion")
                    thread.start()
                thread.join()
                self.esperarCompletos()
                if (self.tiempo==None):
                    break
            self.escribirRespuestas(output)
        elif(self.tipo == "PUT"):
            while(self.esperarTiempo()):
                for i in range(int(self.hilos)):
                    thread = threading.Thread(target = self.put, args = (self.respuestas,),name=str(i+1)+" peticion")
                    thread.start()
                thread.join()
                self.esperarCompletos()
                if (self.tiempo == None):
                    break
            self.escribirRespuestas(output)
        elif(self.tipo == "DELETE"):
            while(self.esperarTiempo()):
                for i in range(int(self.hilos)):
                    thread = threading.Thread(target = self.delete, args = (self.respuestas,),name=str(i+1)+" peticion")
                    thread.start()
                thread.join()
                self.esperarCompletos()
                if (self.tiempo == None):
                    break
            self.escribirRespuestas(output)
        elif(self.tipo == "HEAD"):
            while(self.esperarTiempo()):
                for i in range(int(self.hilos)):
                    thread = threading.Thread(target = self.head, args = (self.respuestas,),name=str(i+1)+" peticion")
                    thread.start()
                thread.join()
                self.esperarCompletos()
                if (self.tiempo == None):
                    break
            self.escribirRespuestas(output)
        elif(self.tipo == "OPTIONS"):
            while(self.esperarTiempo()):
                for i in range(int(self.hilos)):
                    thread = threading.Thread(target = self.options, args = (self.respuestas,),name = str(i+1)+" peticion")
                    thread.start()
                thread.join()
                self.esperarCompletos()
                if (self.tiempo == None):
                    break
            self.escribirRespuestas(output)
        else:
            pass
        output.close()
        return True

    def esperarCompletos(self):
        while(len(self.respuestas) < int(self.hilos)):
            pass

    def esperarTiempo(self): 
        if(self.tiempo == None or time.time() <= self.horaFinal):
            return True
        return False
    
    def escribirRespuestas(self,archivo):
        self.respuestas = sorted(self.respuestas, key=itemgetter('timeDate'), reverse=True)
        for respuesta in self.respuestas:
            archivo.write(str(respuesta)+"\n")
