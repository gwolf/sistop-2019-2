from random import randint
from core.Planificador import Planificador
class Round_robin(Planificador):
    def __init__(self,log,quantum,procesos):
        Planificador.__init__(self,log,quantum,procesos)
    
    def iniciar_planificador(self):
        self.mostrar_procesos()
        self.planificar()
    
    def planificar(self):
        pass