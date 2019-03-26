#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
import copy

def lista():
    procesos = []
    procesos1 = []
    procesos2 = []
    for i in range (5):
        procesos.append(["P"+str(i),randint(0,10),randint(2,6)])
    procesos.sort(key = lambda proceso : proceso[1])
    print(procesos)
    procesos1 = procesos[:]
    procesos2 = list(procesos)
    return procesos,procesos1,procesos2
