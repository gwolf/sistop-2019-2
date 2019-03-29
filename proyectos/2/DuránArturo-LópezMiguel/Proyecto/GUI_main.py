#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Modulos requeridos para el panel de control
from tkinter import *
from tkinter import ttk
#from tkinter import messagebox

from Sim import *

#################### Panel Control ###############################
# Horas = ['5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']
# Dias = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']


class Ventana:
    #Ventana Principal
    VentanaUI=object()
    #Menu desplegable
    MenuDias = object()
    #ListaDias=['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
    MenuHoras = object()
    #Slider
    Velocidad = object()
    #Labels
    Titulo = object()
    Titulo_Text = "Panel De Control"
    
    Label_Dia = object()
    Label_Dia_Text = "Día:"

    Label_Hora = object()
    Label_Hora_Text = "Hora Inicio:"

    Label_Velocidad = object()
    Label_Velocidad_Text = "Velocidad de ejecucion"
    
    #Variables 
    Tiempo_Simulacion = object()
    Dia = object()
    #Botones
    Start_Buton = object()
    def __init__(self):
        self.VentanaUI = Tk()
        self.VentanaUI.title("Panel de Control")
        self.VentanaUI.configure(background='#EEEEEE')
        self.VentanaUI.geometry('300x300')
        self.VentanaUI.resizable(False, False)
        #Se definen las variables a utilizar
        self.Tiempo_Simulacion = StringVar()
        self.Dia = StringVar()
        #Definicion Labels
        self.Titulo = Label(self.VentanaUI,text=self.Titulo_Text, font=("Helvetica", 16))
        self.Titulo.place(x=20,y=20)

        self.Label_Dia = Label(self.VentanaUI,text=self.Label_Dia_Text, font=("Helvetica", 12))
        self.Label_Dia.place(x=20,y=80)

        self.Label_Hora = Label(self.VentanaUI,text=self.Label_Hora_Text, font=("Helvetica", 12))
        self.Label_Hora.place(x=20,y=120)

        self.Label_Velocidad = Label(self.VentanaUI,text=self.Label_Velocidad_Text, font=("Helvetica", 12))
        self.Label_Velocidad.place(x=20,y=150)
        
        #Definicion de Los elementos
            #Menu (Combobox)
        self.Menu = ttk.Combobox(self.VentanaUI, values = ('Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo'))
        self.Menu.current(0)
        self.Menu.place(x=120,y= 80)

        self.MenuHoras = ttk.Combobox(self.VentanaUI, values = ('5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'))
        self.MenuHoras.current(0)
        self.MenuHoras.place(x=120,y= 120)

        self.Velocidad = Scale(self.VentanaUI,from_= 1,to = 10,resolution=1,orient=HORIZONTAL)
        self.Velocidad.place(x=20,y=170)

        self.Start_Buton = Button(self.VentanaUI,text = 'Iniciar',command = self.Iniciar)
        self.Start_Buton.place(x = 20,y=220)
        return
    
    def Iniciar(self):
        
        Dia  = self.Menu.current()
        Hora = self.MenuHoras.current()
        Vel  = self.Velocidad.get()

        print(Dia)
        print(Hora)
        print(Vel)

        SetVariables(Dia,Hora,Vel)
        run()
        return
    def run(self):
        self.VentanaUI.mainloop()
        return

def main():
    Panel = Ventana()
    Panel.run()    
    return
main()
