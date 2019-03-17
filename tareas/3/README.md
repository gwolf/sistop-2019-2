# Algoritmos de planificación

	Tarea creada: 2019.03.14
	Entrega: 2019.03.21

Para el tema de *Planificación de procesos* abordamos distintos
algoritmos. Si bien los más divertidos son los últimos, los primeros
son más sencillos de implementar — Y, por tanto, son aptos para un
bonito ejercicio.

## Implementar algoritmos

El planteamiento de esta tarea es bastante sencillo: Implementar y
comparar los algoritmos más sencillos (FCFS/FIFO, Round Robin,
SPN). Pueden realizar el ejercicio en su lenguaje favorito.

Si adicionalmente a estos tres algoritmos *simplotes* quieren
divertirse, jueguen con los siguientes que revisamos en clase (Round
Robin con distintas duraciones de quantum, Retroalimentación
Multinivel, Ronda Egoísta...)

A diferencia de lo que vimos en clase, sin embargo, les voy a pedir
que *no* lo hagan sobre una misma *carga ejemplo* (un sólo conjunto de
procesos evaluado bajo los distintos algoritmos), sino que sobre
conjuntos de procesos generados con cierta aleatoriedad (¿cómo? Como
ustedes lo quieran presentar).

Ojo, ¡no olviden verificar manualmente algunos de los resultados! :-)

## Ejemplo de ejecución

La salida básica mínima que espero es algo equivalente a la siguiente:
Primero, generan e imprimen la lista de procesos, y presentan el
resultado del análisis de ejecución de cada algoritmo (el renglón de
*promedios*):

    $ compara_planif
    - Primera ronda:
      A: 0, t=3; B: 1, t=5; C: 3, t=2; D: 9, t=5; E: 12, t=5 (tot:20)
      FCFS: T=6.2, E=2.2, P=1.74
      RR1:  T=7.6, E=3.6, P=1.98
      RR4:  T=7.2, E=3.2, P=1.88
      SPN:  T=5.6, E=1.6, P=1.32
    - Segunda ronda
      A: 0, t=5; B: 3, t=3; C: 3, t=7; D: 7, t=4; E:8, t=4 (tot:23)
      (...)

Pueden esforzarse un poquito más, y regalarme una representación del
orden resultante:

    $ compara_planif
    - Primera ronda:
      A: 0, t=3; B: 1, t=5; C: 3, t=2; D: 9, t=5; E: 12, t=5 (tot:20)
      FCFS: T=6.2, E=2.2, P=1.74
      AAABBBBBCCDDDDDEEEEE
	  RR1:  T=7.6, E=3.6, P=1.98
	  ABABCABCBDBDEDEDEDEE
      RR4:  T=7.2, E=3.2, P=1.88
	  AAABBBBCCBDDDDEEEEDE
      SPN:  T=5.6, E=1.6, P=1.32
	  AAACCBBBBBDDDDDEEEEE
    - Segunda ronda
      A: 0, t=5; B: 3, t=3; C: 3, t=7; D: 7, t=4; E:8, t=4 (tot:23)
      (...)

¿Quieren divertirse? Implementen algún algoritmo más
divertido. Retroalimentación multinivel, ronda egoísta, algún esquema
híbrido...

## La entrega

Esta tarea puede realizarse de forma individual o por equipos. Como
siempre, la entrega se realizará mediante el repositorio Git, dentro
del directorio correspondiente (tareas/3/MiNombre-ElDelCompañero).

Les recomiendo, como siempre, hacer su entrega a partir de
sincronizar con `gwolf/master`, y sobre una rama dedicada.
