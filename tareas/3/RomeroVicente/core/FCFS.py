from random import randint
from core.Planificador import Planificador
class FCFS(Planificador):
    def __init__(self,log,quantum,procesos):
        Planificador.__init__(self,log,quantum,procesos)
 
    
    def iniciar_planificador(self):
        self.mostrar_procesos()
        self.planificar()

    
    
    def planificar(self):
        self.procesos.sort(key=lambda x:x.llegada,reverse=False) #ordena por el orden de llegada
        texto = ""
        total = 0
        for proceso in self.procesos:
            if(proceso.llegada > total):
                inicio = proceso.llegada
                total = total + inicio
            else:
                inicio = total
            fin = inicio + proceso.t
            T = fin - proceso.llegada
            self.T_list.append(T)
            P = T/proceso.t
            self.P_list.append(P)
            R = proceso.t/T
            self.R_list.append(R)
            E = T - proceso.t
            self.E_list.append(E)
            for i in range(proceso.t):
                texto = texto + proceso.nombre
            total = total + proceso.t
        promedios = self.get_promedios()
        print("FCFS: T={0}, E={1}, P={2}".format(promedios['T'],promedios['E'],promedios['P']))
        print(texto)
    

