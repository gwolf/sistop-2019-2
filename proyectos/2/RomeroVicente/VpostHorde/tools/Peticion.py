import requests
import threading
from multiprocessing import Queue
import time
import sys
import json
import tools.Analisis as Analisis
import time
import mimetypes

class Peticion(object):
    def __init__(self,url,payload,tipo,headers, auth):
        self.payload = payload
        if(payload != None):
            self.payloadCurlADict()
        self.tipo = tipo.upper()
        self.headers = headers
        if headers != None:
            self.headerCurlADict()
        self.tiposValidos = ("POST","GET","PUT","DELETE","HEAD","OPTIONS")
        self.url = url
        self.auth = auth
        
    def setHeader(self,header):
        self.headers = header
        try:
            self.headerCurlADict()
        except IndexError as e:
            pass
        except Exception as e:
            print(e)
    
    def setPayload(self, payload):
        self.payload = payload
        try:
            self.payloadCurlADict()
        except IndexError as ie:
            pass
        except Exception as e:
            print(e)

    def payloadCurlADict(self):#Parsea la entrada de texto al formato interno de requests
        payload = {}
        datos = self.payload.split("&")
        for dato in datos:
            dato = dato.split("=")
            payload[dato[0]] = dato[1]
        self.payload = payload

    def headerCurlADict(self):#Parsea la entrada de texto al formato para el requests
        headers = {}
        datos = self.headers.split(",")
        for dato in datos:
            dato = dato.split(":")
            headers[dato[0]] = dato[1]
        self.headers = headers

    def istipoValido(self, tipo):#revisa en el diccionario de tipos si se paso un metodo valido o no
        if tipo in self.tiposValidos:
            return True
        return False
    
    def get(self, resultados):#Envia la peticion GET
        respuesta = {} # inicia el diccionario para la respuesta que se va a guardar
        try:
            tiempoInicio = time.time() 
            r = requests.get(self.url,params = self.payload, headers = self.headers, auth = self.auth)# Se crea y se la peticion con los atributos del objeto usando requests
            respuesta["code"] = r.status_code #Guarda el codigo status que regresa el servidor
            respuesta["estado"] = "exito" #Retorna si hubo exito o no
        except Exception as e:
            respuesta["code"] = str(type(e)) #Guarda la excepcion en caso de que fallase la peticion
            respuesta["estado"] = "fallo"            
        finally:
            respuesta["fecha"] = time.strftime("%c") #Guarda la fecha actual
            respuesta["timeDate"] = time.time() #Guarda el tiempo UNIX actual
            respuesta["tiempoPeticion"] = time.time() - tiempoInicio #Guarda el tiempo que duro la peticion en completarse hasta este punto
            resultados.append(respuesta) #Añade la respuesta a la lista de resultados
            return respuesta
    
    def post(self,resultados):
        respuesta = {}
        try:
            tiempoInicio = time.time()
            r = requests.post(self.url,data = self.payload, headers = self.headers, auth = self.auth) 
            respuesta["code"] = r.status_code
            respuesta["estado"] = "exito"
        except Exception as e:
            respuesta["code"] = str(type(e))
            respuesta["estado"] = "fallo" 
        finally:
            respuesta["fecha"] = time.strftime("%c")
            respuesta["timeDate"] = time.time()
            respuesta["tiempoPeticion"] = time.time() - tiempoInicio
            resultados.append(respuesta)
            return respuesta
    
    def postFile(self,resultados):
        respuesta = {}
        try:
            tiempoInicio = time.time()
            files = {'file':open(self.payload,'rb')}
            r = requests.post(self.url,files = files, headers = self.headers, auth = self.auth)
            respuesta["code"] = r.status_code
            respuesta["estado"] = "exito"
        except Exception as e:
            respuesta["code"] = str(type(e))
            respuesta["estado"] = "fallo" 
        finally:
            respuesta["fecha"] = time.strftime("%c")
            respuesta["timeDate"] = time.time()
            respuesta["tiempoPeticion"] = time.time() - tiempoInicio
            resultados.append(respuesta)
            return respuesta

    def put(self,resultados):
        respuesta = {}
        try:
            tiempoInicio = time.time()
            r = requests.put(self.url,data = self.payload, headers = self.headers, auth = self.auth)
            respuesta["code"] = r.status_code
            respuesta["estado"] = "exito"
        except Exception as e:
            respuesta["code"] = str(type(e))
            respuesta["estado"] = "fallo" 
        finally:
            respuesta["fecha"] = time.strftime("%c")
            respuesta["timeDate"] = time.time()
            respuesta["tiempoPeticion"] = time.time() - tiempoInicio
            resultados.append(respuesta)
            return respuesta

    def delete(self,resultados):
        respuesta = {}
        try:
            tiempoInicio = time.time()
            r = requests.delete(self.url, auth = self.auth)
            respuesta["code"] = r.status_code
            respuesta["estado"] = "exito"
        except Exception as e:
            respuesta["code"] = str(type(e))
            respuesta["estado"] = "fallo" 
        finally:
            respuesta["fecha"] = time.strftime("%c")
            respuesta["timeDate"] = time.time()
            respuesta["tiempoPeticion"] = time.time() - tiempoInicio
            resultados.append(respuesta)
            return respuesta
    
    def head(self,resultados):
        respuesta = {}
        try:
            tiempoInicio = time.time()
            r = requests.head(self.url,headers = self.headers, auth = self.auth)
            respuesta["code"] = r.status_code
            respuesta["estado"] = "exito"
        except Exception as e:
            respuesta["code"] = str(type(e))
            respuesta["estado"] = "fallo" 
        finally:
            respuesta["fecha"] = time.strftime("%c")
            respuesta["timeDate"] = time.time()
            respuesta["tiempoPeticion"] = time.time() - tiempoInicio
            resultados.append(respuesta)
            return respuesta
    
    def options(self,resultados):
        respuesta = {}
        try:
            tiempoInicio = time.time()
            r = requests.options(self.url, params = self.payload, headers = self.headers, auth = self.auth)
            respuesta["code"] = r.status_code
            respuesta["estado"] = "exito"
        except Exception as e:
            respuesta["code"] = str(type(e))
            respuesta["estado"] = "fallo" 
        finally:
            respuesta["fecha"] = time.strftime("%c")
            respuesta["timeDate"] = time.time()
            respuesta["tiempoPeticion"] = time.time() - tiempoInicio
            resultados.append(respuesta)
            return respuesta