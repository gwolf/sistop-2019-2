

class Tren:
    Modelo = 'NM-16'
    Capacidad_Max = 1530
    Capacidad_Actual = 0
    Linea=str()
    Numero=int()
    Direccion=int()
    Velocidad_prom = 50 #km/h
    def __init__(self,linea,numero,direccion):
        self.Linea     = linea
        self.Numero    = numero
        self.Direccion = direccion
        print("Tren Creado")
        return
    def setDireccion(self,direccion):
        self.Direccion = direccion
        return
    
    def addUsuarios(self,numero_personas_abordando):
        self.Capacidad_Actual += numero_personas_abordando
        return
    def restUsuarios(self,numero_personas_descenso):
        if self.Capacidad_Actual > numero_personas_descenso:
            self.Capacidad_Actual-=numero_personas_descenso
        else:
            self.Capacidad_Actual = 0
        return
    def getCapacidadRestante(self):
        return self.Capacidad_Max - self.Capacidad_Actual

    def getCapacidadActual(self):
        return self.Capacidad_Actual
    
    def getCapacidadMaxima(self):
        return self.Capacidad_Max
    def getvelocidad(self):
        return float(self.Velocidad_prom/60)
    def __str__(self):
        return self.Modelo + " " + str(self.numero)
    def vaciarTren(self):
        self.Capacidad_Actual = 0
        return
    def getNumero(self):
        return self.Numero
    def isEmpty(self):
        return self.Capacidad_Actual == 0
    
    
