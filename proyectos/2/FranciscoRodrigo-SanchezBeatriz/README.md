# El Museo de Djisktra
En la vida cotidiana se presentan situaciones de concurrencia para los cuales serían buena idea poder aplicar los métodos de sincronización vistos en clase. Para el caso del museo de Djisktra se tiene la siguiente problemática.

El museo Djisktra se exhiben muchas máquinas de la era pasada que resultan muy curiosas a las nuevas generaciones, además de que hay actividades lúdicas en las cuales los `millenials` aprenden cómo funcionan alguno de los componentes de la computadora.
El museo está dividido en secciones.

1.  Sección de sistemas operativos.
2.  Las primeras generaciones de computadoras.
3.  Sección de Vulnerabilidades
4.  Personajes más importantes de la computación.
5.  La sala Turing
6.  La sala Larry Page & Sergey Brin
7.  La sala  Neumann 

Y además el museo cuenta con guías que solo pueden atender a turistas que hablan ciertos idiomas, dado que el guía no maneja todos los idiomas. En el museo se tienen 5 guías que tienen las siguientes características.

* El guía 1 solo atiende turistas estadounidenses, ingleses y franceses dado que solo habla **inglés y francés**.
* El guía 2 solo atiende a turistas japoneses y coreanos dado que solo habla **japonés y coreano**.

* El tercer guía habla **inglés y español**
* El cuarto guía solo habla **portugués e italiano**
* Y finalmente, el último guía solo habla **alemán y holandés**

A lo largo del día llegan muchos turistas de distintas nacionalidades y la mécanica del museo es la siguiente.

1. Un turista llega y paga su boleto de acuerdo a las siguientes categorías
   1. Estudiante
   2. Persona de mayor a 65 años
   3. Público en general
2. Antes de finalizar el pago debe escoger si quiere realizar el recorrido por el museo con algún guía o solo. En caso de escoger al guía se le cobrarán un monto adicional.

## Primer problema de sincronización

Por ordenes del museo el guía no puede iniciar su recorrido si

* No hay por lo menos 6 turistas a su cargo
* Además, si por ejemplo el guía habla inglés y francés debe de tener el mismo número de turistas franceses que ingleses. Esto porque en el recorrido tiene que dar su charla en ambos idiomas y no le conviene dar su discurso para 5 ingleses y para un solo francés, por ejemplo.

### Caso base

```shell
Para el guía 1
Llegan 4 ingleses y 2 franceses
	Ya son 6 turistas, sin embargo aún no se puede ir el guía dado que necesita que el 		número de turistas ingleses sea el mismo que el de franceses.
	Entonces lo que debe hacer en este caso es evitar que sigan pasando turistas ingleses 	  y dejar pasar a 2 franceses 
	De manera que con esto tendría 4 turistas ingleses y 4 franceses y entes momento ¡Puede inciar el viaje!!
```

### Segundo problema de sincronización

En algún momento que desconocemos los guías se pelearon y no pueden estar en la misma sala al mismo tiempo con sus respectivos turistas. Si la sala se encuentra ocupado por algún guía y otro guía quiere pasar  no podrá hacerlo y solo le queda esperar a que se desocupe o *asomarse* a la sala de al lado para ver si esta desocupada y entrar allí mientras se desocupa la otra. 

Se considera que las salas se recorren en el orden que fueron elistadas al principio.

Los guías deben de recorrer todas las salas con todo sus turistas a cargo.

Los que eligieron recorrer el museo solos pueden recorrer el museo en desorden.

### Tercer problema de sincronización

¡El museo de Djiskstra es genial! Sin embargo, es un museo no muy famoso y por lo tanto sus recursos son limitados. Para una de las tantas actividades lúdicas que ofrecen los turistas se deben compartir los recursos. Sin embargo un turistas no puede realizar la actividad recreativa sino tiene el recurso A y el recurso B. [Se quiere llegar al caso de espera por...]

