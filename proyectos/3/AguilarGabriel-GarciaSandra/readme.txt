Autores:Aguilar Luna Gabriel Daniel
	García Racilla Sandra
					Sistema de Archivos

Lenguaje de programación: python
Versión: Python 3
Bibliotecas utilizada:
	-OS
	    +path
	-Sys
	-Math
	    +ceil
	    +log10
	-Datetime
	    +time,datetime

Todas las bibliotecas se encuentran instaladas por deafult en la versión 3 de Python

Planteamiento del problema:
	Desarrollar un programa que pueda obtener, crear y modificar información en el 
	micro-sistema-de-archivos de la Facultad de Ingeniería, FiUnamFS. 	


Ejecucion
	Para ejecutar el programa es necesario ubicarse en el ruta donde se encuentra guardado
	el proyecto y ejecutar el siguiente comando:
		--Para el sistema operativo de Windows
			python manejador.py [comando||archivo]
	El comando anterior puede variar dependiendo de el sistema operativo en el que se esté trabajado y la versión de Python con la que se cuente.
		--En distribuciones de linux y con versión de Python3
 			python3 manejador.py [comando||archivo]
NOTA: Es importante verificar este punto por que podría marcar error al tratar de compilar


El programa realiza cinco funciones principales:
	1.Listar los contenidos del directorio
	2.Copiar uno de los archivos de dentro del FiUnamFS hacia tu sistema
	3.Copiar un archivo de tu computadora hacia tu FiUnamFS
	4.Eliminar un archivo del FiUnamFS.
	*5.El programa también realiza desfragmentación cada vez que se elimina un archivo del
	directorio para evitar desperdicios de memoria. Esto lo hace automáticamente por lo que 
	el usuario no decide en qué momento hacer la desfragmentación o no.

Ejecucion
	La primera vez que ejecutemos el programa se creará un archivo de extensión ".img" el cual 
	será nuestro Sistema, es por eso que la primera vez sólo ejecutamos:
		python manejador.py
	Esto nos mostrará las opciones que ponemos hacer

Al ejecutar podemos elegir cuatro opciones o COMANDOS después de indicar el nombre del programa
	1. listar: El comando muestra una lista del nombre de todos los archivos que se encuentran 
	   guardados en el directorio del Sistema de Archivos. No es necesario pasarle el nombre de
	   algun archivo.
	Ejemplo:
		python manejador.py listar

	2. copiar: El comando copia un archivo determinado del Sitema de Archivos a la computadora.
	   El archivo copiado se guardara en la misma carpeta en la que se encuentra el programa. Al
	   ejecutarlo el programa nos pedirá que proporcionemos el nombre con el que queremos que
	   se guarde nuestro archivo, éste debe ser diferente al archivo a copiar.
	Ejemplo:
		python manejador.py copiar prueba.txt
	
	3. añadir: El comando copia un archivo determinado de la computadora al Sitema de Archivos.
	  El archivo a copiar debe encontrarse dentro del mismo directorio que el programa
	Ejemplo:
		python manejador.py añadir prueba.txt
	
	4. eliminar: El comando borra un archivo determinado del Sistema de Archivos. 
	Ejmplo:
		python manejador.py eliminar README.org

NOTAS:
	*NUNCA debes cambiar el nombre del sistema "FiUnamFS", que se encuentra en el archivo ".img"
	 de lo contrario te dirá que existe un error el la ejecución se detendrá de inmediato.
	
