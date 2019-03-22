from random import randint
from core.Planificador import Planificador
from math import ceil
class FCFS(Planificador):
    def __init__(self,log,quantum,procesos):
        Planificador.__init__(self,log,quantum,procesos)
 
    def iniciar_planificador(self):
        self.mostrar_procesos()
        self.planificar()

    def planificar(self):
        texto = ""
        total = 0
        inicio = 0
        for proceso in self.procesos:
            while(proceso.llegada > total):
                total = total + 1
                texto = texto + "[  ]"
            inicio = total
            fin = inicio + ceil(proceso.t/self.quantum)
            T = (fin - proceso.llegada)
            quantum_tick = proceso.t/self.quantum
            self.T_list.append(T)
            P = T/quantum_tick
            self.P_list.append(P)
            R = quantum_tick/T
            self.R_list.append(R)
            E = T - quantum_tick
            self.E_list.append(E)
            for i in range(ceil(quantum_tick)):
                texto = texto + proceso.nombre
            total = total + ceil(proceso.t/self.quantum)
        promedios = self.get_promedios()
        print("FCFS: T={0}, E={1}, P={2}".format(promedios['T'],promedios['E'],promedios['P']))
        print(texto)