#!/usr/bin/env python
#-*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from FS import *
import tkinter as tk

global FS
#Definición
ventana = Tk()
ventana.geometry('900x400')
#Fondo
img = PhotoImage(file = 'Resources/unam.png')
fondo = Label(ventana,image = img).place(x = 0,y = 0)
#Acciones
def montar():
    global FS
    print ("Se procede a montar")
    file_img = filedialog.askopenfilename()
    FS = FileSystem(file_img)

def copiaraFS():
    global FS
    print ("Se procede a copiar al FS")
    messagebox.showinfo('Seleccione el archivo a copiar','Defina el archivo que desea copiar al FS')
    file_cpFS = filedialog.askopenfilename()
    FS.copyToFS(file_cpFS)


def copiarDesdeFS():
    v_arch = tk.StringVar()
    v_ruta = tk.StringVar()

    def copia(archivo,ruta):
        global FS
        archivo = archivo.get()
        ruta = ruta.get()
        print ("Archivo a copiar: " + str(archivo))
        print ("Ruta: " + str(ruta))
        FS.copytoUser(archivo,ruta)


    print ("Se procede a copiar desde FS")
    lb1 = Label(ventana, text="Escriba el nombre del archivo que desea copiar desde el FS:", font=("Arial Bold", 12)).place(x = 60,y =50)
    E1 = Entry(ventana,width = 20,textvariable = v_arch).place(x = 90,y = 100)

    lbl2 = Label(ventana, text="Escriba la ruta de destino:", font=("Arial Bold", 12)).place(x = 60,y = 200)

    E2 = Entry(ventana,width = 20,textvariable = v_ruta).place(x = 90,y = 230)

    btn1 = Button(ventana,text = "Aceptar", command = lambda : copia(v_arch,v_ruta)).place(x = 150, y = 270)



def eliminarDesdeFS():

    v_archivoE = tk.StringVar()

    def eliminacion(archivo):
        global FS
        archivo = archivo.get()
        print("Archivo a eliminar: " + str(archivo))
        FS.remove(archivo)

    print ("Se procede a eliminar en el FS")
    lbl3 = Label(ventana, text="Escriba el archivo a eliminar en el SF", font=("Arial Bold", 12)).place(x = 600,y = 200)
    E3 = Entry(ventana,width = 20,textvariable = v_archivoE).place(x = 630,y = 230)
    btn2 = Button(ventana,text = "Aceptar", command = lambda : eliminacion(v_archivoE)).place(x = 690, y = 270)


def ls():
    global LS
    print ("Listar")
    FS.ls()

def desfragmentar():
    global LS
    FS.desfragmentacion()

# Creación del titulo
ventana.title("FS-FI UNAM")

#Aviso de montar la imagen
messagebox.showinfo('Seleccione el archivo a montar','Defina el archivo .img en la opción montar')

# Crear el menu principal
menubarra = Menu(ventana)
menubarra.add_command(label="Montar imagen .img", command = montar)
menubarra.add_command(label="Listar", command = ls)
menubarra.add_command(label="Copiar al FS", command = copiaraFS)
menubarra.add_command(label="Copiar desde el FS", command = copiarDesdeFS)
menubarra.add_command(label="Eliminar en el FS", command = eliminarDesdeFS)
menubarra.add_command(label="--Desfragmentar--", command = desfragmentar)
menubarra.add_command(label="Salir", command=ventana.quit)

# Mostrar el menu
ventana.config(menu = menubarra)

# Mostrar la ventana
ventana.mainloop()
