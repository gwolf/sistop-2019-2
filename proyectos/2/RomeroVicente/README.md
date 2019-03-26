# Proyecto 2. Simulacion y aplicacion real para pruebas de estres a paginas web con varios usuarios simultaneos
## Introduccion
Este programa hace una simulacion real de usuarios simultaneos a cualquier url que se le indique.
Se simularan N numero de usuarios haciendo click simultaneamente a la url y se guardara un registro del comportamiento
de las respuestas del servidor
Tiene las siguientes caracteristicas
* Soporte para url http y https
* Soporte de metodos GET POST PUT DELETE HEAD OPTIONS
* Soporte para el envio de archivos por multipart
* Soporte para la inclusion de cabeceras Headers personalizadas
* Uso de peticiones simultaneas por medio de hilos
* Creacion de grafico en el tiempo que dura la prueba
* Creacion de log con los datos y resultados de cada peticion

### ¿Dónde pueden verse las consecuencias nocivas de la concurrencia? ¿Qué eventos pueden ocurrir que queramos controlar?
El mayor evento nocivo que puede ocurrir es al momento de guardar las respuestas ya que estas habitaran en un mismo espacio
de memoria, tambien puede ocurrir que al enviar 2 peticiones simultaneas se bloqueen mutuamente, la finalidad es poder simular
fielmente el numero exacto de usuarios simultaneos "haciendo click" a la pagina por lo que una barrera es lo mas idoneo.

## Lógica de operación
### Identificación del estado compartido e interaccion
Las variables compartidas en este programa son las siguientes
#### Clase Estres
* respuestas => Esta variable es del tipo lista y en el se almacenan las respuestas por cada peticion que concluye su ejecucion
* output => Esta variable es el apuntador al archivo persistente el cual sera escrito con los resultados, este solo puede ser escrito al finalizar todas las peticion
* barrier => Esta variable permite la implementacion de la barrera
* mutex => Esta variable sirve para asegurar la ejecucion completa de cada peticion antes de aumentar el contador
* num => Esta variable es el contador para la barrera
#### Clase Peticion
* requests => Esta no sera una variable en el estricto sentido pero es la interfaz de conexion que se comparte principalmente con todos los procesos
* mutex => esta variable viene de la clase estres y se libera al finalizar cada peticion
#### Consola
* mutex => este semaforo sirve para esperar a que termine la prueba antes de escribir el analisis de los datos
#### GUI
* mutex => Es el mismo caso que en el de la consola
## Descripcion del entorno de desarrollo
### Lenguaje utilizado
* Python 3.7 puede utilizarse en su version 3.*
### Bibliotecas y dependencias
* wxPython: `` pip install wxPython ``
* numpy: ``pip install numpy``
### Sistema operativo
* GNU/linux con entorno grafico gtk compatible
#### Se uso y probo en las siguientes distribuciones
* ArchLinux
* CentOS 7

