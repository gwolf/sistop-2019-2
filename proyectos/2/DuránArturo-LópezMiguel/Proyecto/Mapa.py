#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle


linea1list = ((-737,240),(-710,240),(-670,240),(-630,240),(-590,240),(-550,240),(-513,240),(-473,240),(-433,240),(-396,240),(-356,240),(-316,240),(-280,240),(-236,240),(-200,240),(-160,240),(-125,240),(-82,240),(-43,240),(-10,240),(30,240),(50,240))
linea5list = ( (-720,-70),(-683,-70),(-633,-70),(-583,-70),(-535, -70 ),(-485,-70),(-435,-70),(-385,-70),(-330,-70),(-286,-70 ),(-236,-70),(-186,-70),(-138,-70),(-75,-70),(-40,-70))
linea9list = ((80,240),(110,240),(160,240),(210,240),(265,240),(318,240),(373,240),(424, 240),(480,240),(533,240),(589,240),(650,240),(700,240),(725,240))
lineaAlist = ((95,-70),(133,-70),(188,-70),(250,-70),(305,-70),(371,-70),(431,-70),(489,-70),(545,-70),(590,-70),(655,-70),(680,-70))

lineas = [linea1list,linea5list,linea9list,lineaAlist]

class Mapa:
    def __init__(self):
        return
    
    def lineaXY(self,estacionid,linea,apuntador):
        apuntador.fillcolor("orange")
        apuntador.shape("square")
        apuntador.penup()
        posx = lineas[linea][estacionid][0]
        posy = lineas[linea][estacionid][1]
        #print(posx)
        #print(posy)
        apuntador.goto(posx,posy)
    def drawText(self):
        return
    def run(self):
        screen = turtle.Screen()
        image = "Resources/MapaMod.gif"
        #apuntador = turtle.Turtle()

        screen.addshape(image)
        fondo = turtle.shape(image)
        turtle.setup(1483,737,0,0)
        turtle.title("Mapa de control")
        turtle.exitonclick()
        return


def lineaXY(estacionid,linea,apuntador):
    apuntador.fillcolor("orange")
    apuntador.shape("square")
    apuntador.penup()
    posx = lineas[linea][estacionid][0]
    posy = lineas[linea][estacionid][1]
    #print(posx)
    #print(posy)
    apuntador.goto(posx,posy)

"""
screen = turtle.Screen()
image = "Resources/MapaMod.gif"
apuntador = turtle.Turtle()

screen.addshape(image)
fondo = turtle.shape(image)
turtle.setup(1483,737,0,0)
turtle.title("Mapa de control")
yo = turtle.Turtle()






def lineaXY(estacionid,linea,apuntador):
    apuntador.fillcolor("orange")
    apuntador.shape("square")
    apuntador.penup()
    posx = lineas[linea][estacionid][0]
    posy = lineas[linea][estacionid][1]
    print(posx)
    print(posy)
    apuntador.goto(posx,posy)

#lineaXY(4,3,apuntador)

"""




