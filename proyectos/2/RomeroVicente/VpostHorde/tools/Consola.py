import tools.Estres as Estres
import argparse
import threading
from tools.GUI import *
class Consola:
    def __init__(self):
        self.parser = parser = argparse.ArgumentParser()
        self.parser.add_argument('--cli', default=False, action="store_true", help='si esta activado se iniciara en modo consola usando los parametros')
        self.parser.add_argument('-u','--url',nargs='?', default=None,type=str, help='Define la url objetivo')
        self.parser.add_argument('-o','--out-file', nargs='?', default="out", type=str,help='Se define el archivo de salida de la prueba')
        self.parser.add_argument('-d','--payload',nargs='?',default=None,required=False,type=str,help="Define el payload para cada peticion (formato Curl)")
        self.parser.add_argument('-H','--headers',nargs='?',default=None,type=str,help="Define las cabeceras de cada peticion")
        self.parser.add_argument('--auth',nargs='?',default=None,type=str,help="Define la cabecera de autenticacion (bearer o diggest o basic)")
        self.parser.add_argument('-X','--type',nargs='?',default='GET',type=str,help="Se define el tipo de la peticion [GET|POST|PUT|DELETE]")
        self.parser.add_argument('-t','--threads',nargs='?',default=1,type=int,help="Se la cantidad de peticiones simultaneas activas")
        self.parser.add_argument('-s','--seconds',nargs='?',default=None,type=int,help="Se define la cantidad de segundos que durara la prueba si se deja en 0 la prueba durara lo que tarden los hilos especificados en ejecutares")
        self.parser.add_argument('-f','--file',nargs='?',default=False,type=str,help="Se añade la ruta del archivo que va a ser enviado por multipart en cada peticion")
        self.args = parser.parse_args()
        self.estres = None

    def evaluarArgumentos(self):
        if self.args.cli == True:
            params = self.args
            url = params.url
            if url != None:
                archivoRespuestas = params.out_file
                payload = params.payload
                headers = params.headers
                auth = params.auth
                tipo = params.type
                hilos = params.threads
                tiempo = params.seconds
                archivo = params.file
                self.estres = Estres.Estres(hilos = hilos,tiempo = tiempo,url = url, payload = payload, tipo = tipo,headers = headers,auth = auth, archivo = archivo, archivoRespuestas=archivoRespuestas)
            else:
                print("tienes que introducir una URL valida")
                self.estres = False

    def iniciar_consola(self):
        if self.estres != None and self.estres != False:
            self.estres.iniciarHilos()
            analisis = self.estres.crearAnalisis()
            print("["+str(analisis.exitosVSFallos)+",'tiempo_promedio':"+str(analisis.tiempo_promedio)+", "+str(analisis.state_codes_dict)+"]")
            analisis.dibujar_state_codes()
        elif self.estres == None:
            app = MyApp(0)
            app.MainLoop()