class Planificador:
    def __init__(self,log,quantum,procesos):
        self.log = log
        self.quantum = quantum
        self.procesos = procesos
        self.total = 0
    
    def mostrar_procesos(self):
        texto = ""
        suma = 0
        for proceso in self.procesos:
            suma = suma + proceso.t
            texto = texto + " " + proceso.nombre +": " + str(proceso.llegada) + ", t="+ str(proceso.t)+";"
        self.total = suma
        print(texto + "(total:"+str(self.total)+")")