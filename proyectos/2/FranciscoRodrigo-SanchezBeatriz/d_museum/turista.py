import threading
import random
from d_museum.lenguajes import language
import d_museum.var_glob

class Turista(threading.Thread):
    """Esta es una clase Turista"""
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id = id
        self.idioma = random.choice(language)
    def run(self):
        #print("Soy el turista %d y hablo %s" %(self.id,self.idioma))

    	global turista_esp,turista_ing,esCap
    	#print("esp %d esperando ..." %num)
    	mutex_guia.acquire()
    	turista_esp+=1
    	print("Turista que habla español %d formado para recorrido" %num)
    	if (turista_ing + turista_esp) >=4:
    		for i in range(turista_ing):
    			lista_turista_ing.release()
    		for i in range(turista_esp):
    			lista_turista_esp.release()
    		turista_ing=0
    		turista_esp=0
    		print("*** Inicia recorrido")

    	mutex_guia.release()

    	lista_turista_esp.acquire()
