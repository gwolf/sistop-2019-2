class Planificador:
    def __init__(self,log,quantum,procesos):
        self.log = log
        self.quantum = quantum
        self.procesos = procesos
        self.procesos.sort(key=lambda x:x.llegada,reverse=False) #ordena por el orden de llegada
        self.total = 0
        self.T_list = []
        self.P_list = []
        self.R_list = []
        self.E_list = []
    
    def mostrar_procesos(self):
        texto = ""
        suma = 0
        for proceso in self.procesos:
            suma = suma + proceso.t
            texto = texto + " " + proceso.nombre +": " + str(proceso.llegada) + ", t="+ str(proceso.t/self.quantum)+"[quantum];"
        self.total = suma
        print(texto + "(total:"+str(self.total/1000)+"[s])")

    def get_promedios(self):
        P_promedio = 0
        R_promedio = 0
        T_promedio = 0
        E_promedio = 0
        cantidad_procesos = len(self.procesos)
        for P in self.P_list:
            P_promedio = P_promedio + P
        P_promedio = P_promedio/cantidad_procesos
        for T in self.T_list:
            T_promedio = T_promedio + T
        T_promedio = T_promedio/cantidad_procesos
        for R in self.R_list:
            R_promedio = R_promedio + R
        for E in self.E_list:
            E_promedio = E_promedio + E
        R_promedio = R_promedio/cantidad_procesos
        return {"P":P_promedio,"R":R_promedio,"T":T_promedio,"E":E_promedio}