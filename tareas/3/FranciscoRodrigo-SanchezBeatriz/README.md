# Algoritmos de planificación

En esta tarea implementamos algoritmos básicos en la planificación de procesos.

En primera instancia los procesos se generan de manera aleatoria mediante la función
`rand_proc()`. Los procesos los almacenamos en una lista de `python` y cada proceso es una
lista que tiene tres elementos.
  * El primer elemento de la lista es el id del proceso
  * El segundo elemento es el tiempo de llegada de los procesos
  * Finalmente, el tercer parámetro es el tiempo de ejecución (t)

Si imprimimos la lista procesos obtenemos algo similar a esto.

```python
Número de procesos : 4
Los procesos generados aleatoriamente son :
[[0, 2, 4], [1, 3, 2], [2, 9, 3], [3, 2, 8]]

```

Usted básicamente va tener 2 variables con las que puede jugar, las cuales son:

* El número de procesos a generar
* El número de rondas

Entonces si corremos nuestro programa en la línea de comandos

```shell
$ python3 main.py 5 2
```

Es decir, el número de procesos es 5 y el número de rondas será 2

Si los se meten mal los parametros o no se meten, se tomarán parametros por defecto.

* El número de procesos por defecto es 4
* El número de rondas por defecto es 2

```shell
$ python3 main.py
```

