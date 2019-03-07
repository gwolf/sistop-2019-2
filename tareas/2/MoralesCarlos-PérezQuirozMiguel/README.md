# El cruce del río
    Morales Tellez Carlos Gamaliel
    Pérez Quiroz Miguel Ángel

## Planteamiento
Para llegar a un encuentro de desarrolladores de sistemas operativos, hace falta cruzar un río en balsa.
Los desarrolladores podrían pelearse entre sí, hay que cuidar que vayan con un balance adecuado
En la balsa caben cuatro (y sólo cuatro) personas
La balsa es demasiado ligera, y con menos de cuatro puede volcar.
Al encuentro están invitados hackers (desarrolladores de Linux) y serfs (desarrolladores de Microsoft).
Para evitar peleas, debe mantenerse un buen balance: No debes permitir que aborden tres hackers y un serf, o tres serfs y un hacker. Pueden subir cuatro del mismo bando, o dos y dos.
Hay sólo una balsa.
No se preocupen por devolver la balsa (está programada para volver sola)

## Lenguaje y entorno utilizado.
La solución está implementada en Python versión Python 3.6.4 :: Anaconda, Inc.

## ¿Cómo ejecutar el programa?
Ejercutar el siguiente comando en una terminal
```
python3 /path/RiverCrossing.py
```
donde "path" es la ubicación del archivo RiverCrossing.py

## Estrategias de sincronización utilizados
Utilizamos una barrera, un mutex y dos semáforos cerrados
    
**Nota:** No se utilizaron refinamientos porque no se pedía nunguno