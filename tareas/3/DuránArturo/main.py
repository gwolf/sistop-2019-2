#!/usr/bin/env python
# -*- coding: utf-8 -*-

from FIFO import*
from lista import*
from RR4 import*
from RR1 import*
from random import randint
import copy

#lista1,lista2,lista3 = lista()
#lista4 = list(lista1)

#No se empleó la funcion lista para hacer las listas aleatorias debido
#a que eran modificadas en cada método, se trató sin éxito copiar con [:], copy, list()... etc
print("RONDA NÚMERO: 1")
lista = [["P1",0,3],["P2",1,5],["P3",3,2],["P4",9,5],["P5",12,5]]
FIFO(lista)
lista1 = [["P1",0,3],["P2",1,5],["P3",3,2],["P4",9,5],["P5",12,5]]
RR4(lista1,4)
lista2 = [["P1",0,3],["P2",1,5],["P3",3,2],["P4",9,5],["P5",12,5]]
RR1(lista2,1)

print("RONDA NÚMERO: 2")
lista3 = [["P1",2,6],["P2",3,5],["P3",5,1],["P4",8,6],["P5",12,5]]
FIFO(lista3)
lista4 = [["P1",2,6],["P2",3,5],["P3",5,1],["P4",8,6],["P5",12,5]]
RR4(lista4,4)
lista5 = [["P1",2,6],["P2",3,5],["P3",5,1],["P4",8,6],["P5",12,5]]
RR1(lista5,1)
