
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import threading
import time
import random

num_compradores_por_turno = 10
contador_compradores = 0
contador_compradorOnline = 0
contador_compradorFisico = 0
num_boletos = 10
mutex_compradoresOnline = threading.Semaphore(1)
mutex_compradoresFisico = threading.Semaphore(1)
barrera_Online = threading.Semaphore(0)
barrera_Fisico = threading.Semaphore(0)
sem_compraBoleto = threading.Semaphore(0)
mutex_ctr_compradores = threading.Semaphore(1)

class AplicacionBoleto():
    
    def __init__(self):
        
        # Se utiliza el prefijo 'self' para
        # declarar algunas variables asociadas al objeto 
        # de la clase 'AplicacionBoleto'. Su uso es 
        # imprescindible para que se pueda acceder a sus
        # valores desde otros métodos:
        
        self.raiz = Tk()
        self.raiz.geometry('1800x1000')
        
        # Impide que los bordes puedan desplazarse para
        # ampliar o reducir el tamaño de la ventana 'self.raiz':
        
        self.raiz.resizable(width=False,height=False)
        self.raiz.title('Ver info')
        
        # Define el widget Text 'self.tinfo ' en el que se
        # pueden introducir varias líneas de texto:
        
        self.tinfo = Text(self.raiz, width=180, height=60)
        
        # Sitúa la caja de texto 'self.tinfo' en la parte
        # superior de la ventana 'self.raiz':
        
        self.tinfo.pack(side=TOP)
        
        # Define el widget Button 'self.bingresarDatos' que llamará 
        # al metodo 'self.IngrerarDatos' cuando sea presionado
        
        self.bingresarDatos = ttk.Button(self.raiz, text='Ingresar Datos', 
                                command=self.ingresarDatos)
        
        # Coloca el botón 'self.bingresarDatos' en la parte inferior izquierda
                                
        self.bingresarDatos.pack(side=LEFT)

         # Define el widget Button 'self.bejecutarCompra' que llamará 
        # al metodo 'self.ejecutarCompra' cuando sea presionado
        
        self.bejecutarCompra = ttk.Button(self.raiz, text='Ejecutar Programa', 
                                command=self.ejecutarCompra)
        
        # Coloca el botón 'self.bejecutarCompra' en la parte inferior izquierda
                                
        self.bejecutarCompra.pack(side=BOTTOM)
        
        # Define el botón 'self.bsalir'. En este caso
        # cuando sea presionado, el método destruirá o
        # terminará la aplicación-ventana 'self.raíz' con 
        # 'self.raiz.destroy'
        
        self.bsalir = ttk.Button(self.raiz, text='Salir', 
                                 command=self.raiz.destroy)
                                 
        # Coloca el botón 'self.bsalir' a la derecha del 
        # objeto anterior.
                                 
        self.bsalir.pack(side=RIGHT)
        

        texto_info = "\n\n\n\n\n\n\n\n\n\n\n\n\n"
        texto_info += " \t\t\t\t\t\t\t\t\t**********************************\n\n"
        texto_info += " \t\t\t\t\t\t\t\t\t   SISTEMA DE COMPRA DE BOLETOS\n\n"
        texto_info += " \t\t\t\t\t\t\t\t\t**********************************\n\n"
        self.tinfo.insert("10.0", texto_info)

        # El foco de la aplicación se sitúa en el botón
        # 'self.binfo' resaltando su borde. Si se presiona
        # la barra espaciadora el botón que tiene el foco
        # será pulsado. El foco puede cambiar de un widget
        # a otro con la tecla tabulador [tab]
        self.bingresarDatos.focus_set()
        self.raiz.mainloop()
    
    def ingresarDatos(self):
        
        # Borra el contenido que tenga en un momento dado
        # la caja de texto
        
        self.tinfo.delete("1.0", END)
        texto_info = "\t\t\t\t\t\t\tIngrese los siguientes datos para realizar la ejecucion del programa\n"
        self.tinfo.insert("1.0", texto_info)

      
        self.letiqueta = ttk.Label(self.tinfo, text="Valor")
        self.letiqueta.grid(column=2, row=2, sticky=(W,E))
        

        # Define el Button 'self.bOK' que llamará 
        # al metodo 'self.clickOK' cuando sea presionado
        self.bOK = ttk.Button(self.tinfo, text="Ejecutar OK",command=self.clickOK)
        # Coloca el botón 'self.bejecutarCompra' en la parte inferior izquierda   
      


        valor = ""

        self.entratdaTexto = ttk.Entry(self.tinfo, textvariable=valor)
        self.entradaTexto.grid(column=2, row=1)
       

        def clickOK(self):
            try:
                valor = int(self.entradaTexto.get())
                valor = valor * 5
                self.letiqueta.config(text=valor)
            except ValueError:
                self.letiqueta.config(text="Introduce un numero!")

        
    def ejecutarCompra(self):
        # Borra el contenido que tenga en un momento dado
        # la caja de texto
        self.tinfo.delete("1.0", END)
        texto_info = " \t\t\t\t\t\t\t\t\t\tEJECUTANDO \n"
        self.tinfo.insert("1.0", texto_info)
    

        def compraBoleto():
            global contador_compradores
            global contador_compradorOnline
            global contador_compradorFisico
            global num_compradores_por_turno
            global num_boletos
            texto_info = "\t\tLa compra se esta realizando\n"
            self.tinfo.insert("1.0", texto_info)
            while contador_compradores > 0:
                sem_compraBoleto.acquire()
                mutex_ctr_compradores.acquire()
                if num_boletos==0:
                    texto_info = "\t\tLO SENTIMOS, LOS BOLETOS SE HAN AGOTADO :( \n"
                    self.tinfo.insert("1.0", texto_info)
                    break
                if contador_compradorOnline > 0:
                    texto_info = "\t\tIngresando al sistema el comprador %d \n" % num_compradores_por_turno
                    self.tinfo.insert("1.0", texto_info)
                    contador_compradores = contador_compradores - 1
                    num_boletos = num_boletos -1
                    totalPersonas= totalPersonas-1
                elif contador_compradorFisico > 0:
                    texto_info = "\t\tIngresando al sistema el comprador %d \n" % num_compradores_por_turno
                    self.tinfo.insert("1.0", texto_info)

                    contador_compradores = contador_compradores - 1
                    num_boletos = num_boletos -1
                    totalPersonas = totalPersonas-1
                mutex_ctr_compradores.release()
            texto_info = "\t\tCOMPRA REALIZADA CON EXITO!\n"
            self.tinfo.insert("1.0", texto_info)

        def compradorOnline(nOnline):
            global contador_compradorOnline
            global contador_compradorFisico
            while True:
                #despues de 5 seg aleatoriamente empezaran a entrar al sistema de boletos personas 
                time.sleep(5 + random.random())
                texto_info = "\t\tLa persona %d entra al sistema online\n" % contador_compradorOnline
                #Entra al sistema online una persona
                if num_boletos == 0:
                    break
                contador_compradorOnline +=1
                mutex_compradoresOnline.acquire()
                texto_info = "\t\tUna personna en el sistema online lista para realizar su compra\n"
                self.tinfo.insert("1.0", texto_info)
                #En el primer caso se considera que entraron 10 compradores al sistema online  
                if contador_compradorOnline ==  num_compradores_por_turno:
                    texto_info ="\t\tLa compra esta lista para realizarse desde el sistema online\n"
                    self.tinfo.insert("1.0", texto_info)
                    for i in range(num_compradores_por_turno):
                        barrera_Online.release()
                        compraBoleto()
                    sem_compraBoleto.release()
                    contador_compradorOnline = 0
                #En este segundo caso se considera que al realizar la compra en el sistema online hay n personas comprando en este sistema online
                #pero al mismo tiempo se encuentran n personas comprando el boleto en la tienda fisicamente por lo que si la suma de esas n personas
                #que quieren comprar el boleto es igual al numero de personas admitidas por el sistema se realiza la compra.
                elif contador_compradorOnline + contador_compradorFisico == num_compradores_por_turno:
                    
                    texto_info ="\t\tPersonas en el sistema online y en la tienda listas para realizar su compra\n"
                    self.tinfo.insert("1.0", texto_info)
                    for i in range(contador_compradorOnline):
                        barrera_Fisico.release()
                        compraBoleto()
                    for i in range(contador_compradorFisico):
                        barrera_Online.release()
                        compraBoleto()
                    sem_compraBoleto.release()
                    contador_compradorFisico = 0
                    contador_compradorOnline = 0
                elif num_boletos==0:
                    
                    texto_info = "\t\tBOLETOS AGOTADOS\n"
                    self.tinfo.insert("1.0", texto_info)
                    break
                mutex_compradoresOnline.release()
                barrera_Online.acquire()
                barrera_Fisico.acquire()
    
        def compradorFisico(nPersonaFisico):
            global contador_compradorOnline
            global contador_compradorFisico
            
            while True:
                #despues de 5 seg aleatoriamente empezaran a llegar personas a la tienda fisicamnte a comprar su boleto
                time.sleep(5 + random.random())
                texto_info = "\t\tla persona %d llega a la tienda fisicamnte a comprar su boleto\n" % contador_compradorFisico
                self.tinfo.insert("1.0", texto_info)
                contador_compradorFisico +=1
                mutex_compradoresFisico.acquire()
                texto_info = "\t\tLa persona se ha formado en la tienda fisicamente\n"
                self.tinfo.insert("1.0", texto_info)
                #Este primer caso considera que 10 personas admitidas por el sistema estan en la tienda fisicamente para comprar el boleto
                #por lo que ninguna persona lo esta comprando en el sistema onliene 
                if contador_compradorFisico ==  num_compradores_por_turno:
                    texto_info = "\t\tPersonas en la tienda en fisico listos para comprar su boleto\n"
                    self.tinfo.insert("1.0", texto_info)
                    for i in range(num_compradores_por_turno):
                        barrera_Online.release()
                        compraBoleto()
                    sem_compraBoleto.release()
                    contador_compradorFisico = 0

                #Segundo caso es que hay personas tanto en el sistema online como en la tienda en fisico para comprar sus boletos
                elif contador_compradorFisico + contador_compradorOnline == num_compradores_por_turno:
                    texto_info = "\t\tPersonas en la tienda fisicamente y en el sistema online listas para comrpar su boleto\n"
                    self.tinfo.insert("1.0", texto_info)
                    for i in range(contador_compradorFisico):
                        barrera_Online.release()
                        compraBoleto()
                    for i in range(contador_compradorOnline):
                        barrera_Fisico.release()
                        compraBoleto()
                    sem_compraBoleto.release()
                    contador_compradorOnline = 0
                    contador_compradorFisico = 0
                elif num_boletos==0:
                    texto_info = "\t\tBOLETOS AGOTADOS\n"
                    self.tinfo.insert("1.0", texto_info)
                    
                    break
                mutex_compradoresFisico.release()
                barrera_Fisico.acquire()
                barrera_Online.acquire()
                
        totalPersonas = 5
        print (totalPersonas)
        for i in range(totalPersonas):
            threading.Thread(target = compradorOnline, args = [i]).start()
            threading.Thread(target = compradorFisico, args = [i]).start()

def main():
    mi_app = AplicacionBoleto()
    return 0

if __name__ == '__main__':
    main()