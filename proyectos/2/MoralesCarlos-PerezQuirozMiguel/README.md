# La oficina de los locos
Una situación cotidiana paralelizable
```
Morales Tellez Carlos Gamaliel
Pérez Quiroz Miguel Ángel
```
## Descripción del problema
Una empresa de desarrollo de software cuenta 10 trabajadores contratados y todos acuden a la misma oficina para realizar sus actividades.

Existen tres tipos de trabajadores: 
* Los trabajadores de tiempo completo que trabajan un total de 8 horas
* Los trabajadores de medio tiempo que trabajan 6 horas
* Los suicidas que trabajan 12 horas.

La oficina cuenta con ocho cubículos y cada uno de estos puede ser ocupado por un solo trabajador a la vez.

Los trabajadores son muy puntuales y todos llegan a las 7:00 am. Si todos los cubículos están ocupados deberán esperar a que alguno quede libre para poder trabajar.

Sería injusto que un trabajador conserve un cubículo por 12 horas seguidas y por esta razón los trabajadores solo podrán utilizarlos en periodos de dos horas máximo. 

Si un trabajador desocupa un cubículo y no hay nadie esperando, podrá volver a ocuparlo si así lo requiere.

**NOTA:** No interesa el trabajo realizado por cubículo, interesa el trabajo general en la oficina

## Primitivas de sincronización empleadas
### Multiplex
Se utilizó un multiplex ya que permite la entrada de no más de n procesos a la región crítica, en este restringe el acceso a los cubículos. Se implementó con un semáforo incializado en 8 (número de cubículos dentro de la oficina).

## Algoritmos de planificación empleados
### Round Robin (con q=2)
Se agregaron los trabajadores a una la lista de procesos listos que pueden ejecutarse por un sólo quantum (q). Si un proceso no ha terminado de ejecutar al final de su quantum, será interrumpido y puesto al final de la lista de procesos listos, para que espere a su turno nuevamente. 

## Lógica de operación
### Sección crítica
En este caso un cubículo es considerado una variable que puede generar accesos concurrentes por una condición de carrera entre varios procesos (los trabajadores).
### Ejecución de los hilos
Se implementó un RoundRobin para alternar el cambio de cubículos y permitir que todos los trabajadores puedan realizar sus actividades.

## Entorno de desarrollo
1. Lenguaje de programación: **python 3.6.4**
2. Bibliotecas no estándar: **colorama**
3. Desarrollado y probado en: **macOS 10.14.3** 
**NOTA:** Debería en entornos UNIX con python 3.6.4 y colorama instalados

## Ejecuciones exitosas
### Primera ejecución
<img src= "https://media.giphy.com/media/88iY5aZ1ktni8MBQPX/giphy.gif">
### Segunda ejecución
<img src= "https://media.giphy.com/media/dn0w2v0MCYHJWjHn4B/giphy.gif">
### Tercera ejecución
<img src= "https://media.giphy.com/media/d2Sud63AhjOpIp8AEC/giphy.gif">
