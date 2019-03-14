# Tarea 2: Ejercicios de sincronización

## Problema : Cruce de Río

### Integrantes

Francisco Pablo RODRIGO

Sánchez Díaz BEATRIZ

### ¿Qué necesito para ejecutar el programa?

* Debe tener instalado interprete de Python en la versión 3.5 y la instrucción de ejecución es `python3 cruce-rio.py` para el caso de Ubuntu 16.04 y para el resto de los Linux y Windows solo se debe poner `python cruce-rio.py`
* Si desea aumentar el número de hackers o de serfs debe tener algo de conocimiento del lenguaje `python`.
  * Para modificar la cantidad de hackers o serfs deberá ir a las últimas 4 líneas de código y en el `for` debe cambiar el rango (número de hackers o serfs respectivamente).

### Estrategias de sincronización

Para resolver el problema ocupamos **mutex** (para la parte de proteger el acceso a la balsa), **semaforos** (para la señalización del numero de nuestros hackers o serfs),. La pieza clave en la resolución de este problema para nosotros fue el conteo de nuestros hackers y serfs, es decir la parte del envió de señales ya que en este punto intentamos condicionar de que cuando ya se cumpliera el número requerido la balsa zarpara.



### Conflictos

* Al ejecutar el programa el flujo para muchos hackers y serfs (100 cada uno) era el siguiente:
  * Muchos hackers accedian de 4 en 4 a la balsa y se iban.
  * Muy pocos hackers coexistian en la balsa con los serfs (2 hackers y 2 serfs). 
  * Y finalmente accedian el resto de serfs de 4 en 4.
* Rara vez el programa llego a enviar 5 desarrolladores (hackers y serfs) pero no sabemos por qué :(