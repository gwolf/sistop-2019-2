# Tarea 2 Ejercicio de sincronización

En esta tarea se pondra la solucion a un problema de sincronización

### ¿Que se necesita para poder correr la solucion?

En la raiz de la carpeta del proyecto se encuentra un archivo llamado main.py
este se trata de un ejecutable de python, para la implementacion del programa
se uso python en su version 3.7.2.

## El servidor web

Este problema sigue las siguientes reglas:

* Al inicializar, el proceso jefe lanza k hilos trabajadores

* Los trabajadores que no tienen nada que hacer se van a dormir.

* El proceso jefe recibe una conexión de red, y elige a cualquiera de los trabajadores para que la atienda

* Se la asigna a un trabajador y lo despierta

* El jefe va a buscar mantener siempre a k hilos disponibles y listos para atender las solicitudes que van llegando.
