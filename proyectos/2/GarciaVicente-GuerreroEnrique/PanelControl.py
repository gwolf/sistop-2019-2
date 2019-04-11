# -*- Encoding: utf-8 -*-
from tkinter import *
import time
import os

raiz=Tk()
raiz.title("Menú")
raiz.resizable(0,0)
raiz.geometry("800x500")
raiz.config(bg="yellow green")
#bit = raiz.iconbitmap("bus.ico")

def iniciar():
	lbl2 = Label(raiz,text="Programa finalizado",font=("Arial Bold",35),background = "yellow green")
	lbl2.place(x=190, y=350)
	time.sleep(2)
	comienza()

def comienza():
	os.system("python3 prog2.py")

def finalizar():
	exit()

def variables():
	numeropasajeros = (txt.get())
	numeroparadas = (txt2.get())
	lbl3 = Label(raiz,text="Variables Asignadas",font=("Arial Bold",20),background = "yellow green")
	lbl3.place(x=190, y=350)
	f = open ("variables.py",'w')
	f.write("numeropasajeros ="+numeropasajeros+"\nnumeroparadas ="+numeroparadas)
	f.close()

lbl = Label(raiz,text="Panel de configuración",font=("Arial Bold",30),background = "yellow green")
lbl.place(x=180, y=25)

btn = Button(raiz,text = "Iniciar programa",font=("Arial Bond",15),command=iniciar)
btn.place(x=400, y=200)

btn2 = Button(raiz,text = "Cerrar programa",font=("Arial Bond",15),command=finalizar)
btn2.place(x=400, y=250)

btn2 = Button(raiz,text = "Asignar variables",font=("Arial Bond",15),command=variables)
btn2.place(x=400, y=300)


lbl_pasajeros = Label(raiz,text="Número mínimo de pasajeros: ",font=("Arial Bold",10),background = "yellow green")
lbl_pasajeros.place(x=200, y=100)
txt = Entry(raiz,width=10)
txt.place(x=400, y=100)

lbl_paradas = Label(raiz,text="Número de paradas: ",font=("Arial Bold",10),background = "yellow green")
lbl_paradas.place(x=260, y=130)
txt2 = Entry(raiz,width=10)
txt2.place(x=400, y=130)

raiz.mainloop()
