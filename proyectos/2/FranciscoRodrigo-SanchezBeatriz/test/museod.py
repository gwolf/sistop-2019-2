import threading

class Turista(threading.Thread):
    """Esta es una clase Turista"""
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

class Guia(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        print("Soy el guia "+str(self.id))
        for j in range(0,8):
            print("%d : perdiendo eñ tiempo, %d" %(self.id,j))

    def saludar(self):
        print("Ultima prueba, saludando %d" %self.id)
#def generadorTuristas(esp=3,):

def main():
    print("Soy el main")

    for i in range(0,10):
        t =Guia(i)
        t.start()
        #t.saludar()
main()
