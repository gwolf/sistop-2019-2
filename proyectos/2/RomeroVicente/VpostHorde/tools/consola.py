import sys
import time
import tools.Estres as Estres
def evaluarArgumentos(params):
    if "--cli" in sys.argv:
        params = sys.argv
    if "-u" in params:
        url = str(params[sys.argv.index("-u")+1])
    else:
        url = None
    if "--outfile" in params:
        archivoRespuestas = str(params[sys.argv.index("-outfile")+1])
    else:
        archivoRespuestas = "out"
    if "-d" in params:
        payload = str(params[sys.argv.index("-d")+1])
    else:
        payload = None
    if "-H" in params:
        headers = str(params[sys.argv.index("-H")+1])
    else:
        headers = None
    if "--auth" in params:
        auth = str(params[sys.argv.index("--auth")+1])
    else: 
        auth = None
    if "-X" in params:
        tipo = str(params[sys.argv.index("-X")+1]).upper()
    else:
        tipo = "GET"
    if "--threads" in params:
        hilos = str(params[sys.argv.index("--threads")+1])
    else:
        hilos = 1
    if "--tiempo" in params:
        tiempo = str(params[sys.argv.index("--tiempo")+1])
    else:
        tiempo = None
    if "--file" in params:
        archivo = str(params[sys.argv.index("--auth")+1])
        if(archivo.upper() == "TRUE" or archivo.upper() == "T"):
            archivo = True
        else:
            archivo = False
    else: archivo = False
    e = Estres.Estres(hilos = hilos,tiempo = tiempo,url = url, payload = payload, tipo = tipo,headers = headers,auth = auth, archivo = archivo, archivoRespuestas=archivoRespuestas)
    return e
