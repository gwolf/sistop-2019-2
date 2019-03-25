import tools.consola as consola
from tools.GUI import *
import pkg_resources
import sys

if __name__ == "__main__":
    e = consola.evaluarArgumentos(params=[])
    if "--cli" in sys.argv:
        e.iniciarHilos()
        analisis = e.crearAnalisis()
        print(str(analisis.exitosVSFallos)+" "+str(analisis.tiempo_promedio)+" "+str(analisis.state_codes_dict))
        analisis.dibujar_state_codes()
    else:
        app = MyApp(0)
        app.MainLoop()