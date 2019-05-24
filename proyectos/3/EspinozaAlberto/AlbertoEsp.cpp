#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
# define MAX 25

char * main_menu_items[32] =
{
	"Salir",
	"Nuevo archivo",
	"Ver todos los archivos",
	"",
};

/**
 * @brief Lee una cadena desde el teclado.
 *
 * Esta función debe ser utilizada cada vez que se requiera leer una cadena
 * desde el teclaco, usándose en lugar de fgets(), gets(), scanf(), etc.
 *
 * @param str Arreglo donde se guardará la cadena leída.
 *
 * @return El número de carácteres leídos
 */
int GetString(char * str)
{
	int n = 0;
	char c;
	char * p = str;

	while (getchar() != '\n') { ; }
	// se come los '\n' previos

	while ((c = getchar()) != '\n') {
		*p = c;
		++p;

		++n;
	}

	*p = '\0';

	return n;
}

void myfflush()
{
	int c;
//	while ((c = getchar()) != '\n' && c != EOF) {
//		;
//	}
	while (getchar () != '\n') {
		;
	}
}

int main_menu()
{
	int option;
	int i;

	while (1)
	{
		printf("\n");

		for (i = 0; strcmp(main_menu_items[i], "") != 0; ++i) {
			printf("%d -- %s\n", i, main_menu_items[i]);
		}

		printf("Su opcion: ");
		scanf("%d", &option);

		if (option < i && option >= 0) {
			return option;
		}
		else {
			printf("Opcion invalida\n");
		}
	}
}

/**
 * @brief Estructura que representa a cada ítem que se guardará en el archivo.
 */
struct Cluster
{

	char name[20];
	char cont[50];
	int tam;
	int valido;
	int tBin[12];

};

/**
 * @brief Estructura que representa la cabecera del archivo
 */
struct Header_C
{
	char nombre[10]="FiUnamFs ";
	char ver[10]="0.3";
	char etiqueta[20]="Sistemas oparat    ";
	char tamCl[7]="1024";
	char numCl[6]="04   ";
	char totCl[8]="0001440";
	int registros;
	// es el número de registros en el archivo
	char RestMem[959];
};

/**
 * @brief Verifica que el archivo sea del tipo "FiUnamFs"
 *
 * @param fileName Nombre del archivo de la base de datos
 *
 * @return	>= 0: El número de registros actualmente en la base de datos
 *			  -1: En casode que se haya presentado algún error
 */
 
int Verificar(char * fileName)
{
	FILE * fd = NULL;

	struct Header_C h;

	fd = fopen(fileName, "rb+");
	// intentamos abrir al archivo en modo lectura

	// Si el archivo no existe en la ruta, entonces tenemos que crear uno nuevo.
	// En caso de que sí exista, entonces leemos los metadatos
	if (fd == NULL ){
		// Nota:
		// En este punto no es necesario cerrar al archivo apuntado por fd dado
		// que no existe. Ahora simplemente creamos uno:
		fd = fopen(fileName, "wb");
		// creamos un archivo nuevo
		if (fd == NULL) {
			printf("Error creando el archivo\n");
			exit(1);
		}	
		h.registros = 0;
		strcpy(h.nombre,"FiUnamFs ");

		fwrite(&h, sizeof(struct Header_C), 1, fd);
		fclose(fd);
		// cerramos al archivo nuevo
		return 0;

	}
	else {

		rewind(fd);
		// regresamos el cursor a la posición inicial del archivo
		fread(&h, sizeof(struct Header_C), 1, fd);
		// leemos los metadatos

		fclose(fd);
		// cerramos al archivo porque en este momento ya no lo necesitamos más.
		// Los datos importante ahora están en 'h'

		if (strcmp(h.nombre,"FiUnamFs ") != 0 ) {
			// printf("Error: El archivo no es del tipo FiUnamFs\n");
			return -1;
		}
		else {
			return h.registros;
		}
	}
}


static int actualizar(char * fileName)
{
	FILE * fd = NULL;

	fd = fopen(fileName, "rb+");
	// vamos a leer y escribir los metadatos; en principio lo abrimos como de
	// lectura para que no lo vaya a borrar

	if (fd == NULL) { return -1; }

	struct Header_C h;

	rewind(fd);
	// nos colocamos al principio del archivo para leer los metadatos

	fread(&h, sizeof(struct Header_C), 1, fd);
	// leemos los datos actuales. Básicamente lo que nos importa es el contador
	// de registros

	h.registros++;
	// incrementamos al contador de registros

	rewind(fd);
	// nos colocamos al principio del archivo para escribir los metadatos (la
	// llamada anterior a fread() nos movió el cursor)

	fwrite(&h, sizeof(struct Header_C), 1, fd);
	// devolvemos el valor actualizado al archivo

	fclose(fd);

	return 0;
}

/**
 * @brief Inserta al final del archivo, y actualiza al contador 
 *
 * @param fileName Nombre del archivo de la base de datos
 * @param a Búfer de datos donde está la información del registro que se va a
 * insertar
 *
 * @return	-1: Si hubo algún error
 *			0: Si no hubo errores
 */
int Insertar(char * fileName, struct Cluster * a)
{
	FILE * fd = NULL;

	fd = fopen(fileName, "ab");
	// abrimos al archivo para escritura a partir del final de éste

	if (fd == NULL) { return -1; }

	fwrite(a, sizeof(struct Cluster), 1, fd);
	// escribimos la información del alumno a partir del final del
	// archivo

	fclose(fd);


	if (actualizar(fileName) < 0) { return -1; }
	// actualizamos al contador  en el bloque de metadatos

	return 0;
}

int Cerrar(char *fileName){
	FILE * fd ;
	fd = fopen(fileName, "rb+");
	printf("Cerrando\n");
	fseek(fd, 1440000, 0);
	printf("estoy en %d",ftell(fd));
	fputs("k", fd);
	rewind(fd);
	fclose(fd);
}


/**
 * @brief Devuelve la cantidad de registros en el archivo de base de datos
 *
 * @param fileName Nombre del archivo de la base de datos
 *
 * @return El número de registros en la base de datos. -1 si hubo algún error.
 */
int Registros(char * fileName)
{
	FILE * fd = NULL;

	fd = fopen(fileName, "rb");
	// vamos a leer los metadatos

	if (fd == NULL) { return -1; }

	struct Header_C h;

	fread(&h, sizeof(struct Header_C), 1, fd);
	// leemos los datos actuales. Básicamente lo que nos importa es el contador
	// de registros. No hemos utilizado a la función rewind() porque al abrir al
	// archivo como de lectura el cursor ya se encuentra al principio de éste.

	fclose(fd);

	return h.registros;
}

/**
 * @brief Lee uno o varios registros de la base de datos
 *
 * @param fileName Nombre del archivo de la base de datos
 * @param buffer Arreglo donde se guardarán los registros leídos
 * @param tam La cantidad de registros que se van a leer
 * @param nreg Registro a partir del cual se hará la lectura
 *
 * @return -1 si hubo algún error; 0 en cualquier otro caso
 */
int Leer(char * fileName, struct Cluster * buffer, int tam, int nreg)
{
	FILE * fd = NULL;

	int offset = sizeof(struct Header_C) + sizeof(struct Cluster) * nreg;
	// calculamos el registro a partir del cual queremos leer

	fd = fopen(fileName, "rb");
	// únicamente vamos a leer los datos

	if (fd == NULL) { return -1; }

	fseek(fd, offset, SEEK_SET);
	// colocamos al cursor en el registro a partir del cual queremos leer

	fread(buffer, sizeof(struct Cluster), tam, fd);
	// leemos el o los registros
	fclose(fd);
	return 0;
}


/*-----------------------------------------------------------------------------
 *  Driver program
 *-----------------------------------------------------------------------------*/
int main(int argc, const char *argv[])
{
	char Directorio[] = "./disk.img";

	int n;
	struct Cluster temp;
	struct Cluster buf[300];
	struct Cluster lista;
    int numreg=0;

	n = Verificar(Directorio);
	if (n < 0)
    {
		printf("Hubo un error abriendo la unidad\n");
		exit(1);
	}
	else if (n == 0)
	{
		printf("esta vacio.\n");
	}
	else { printf("Se encontraron (%d) archivos en la unidad.\n", n); }
	
	while (1)
	{
		int option = main_menu();

		switch (option)
		 {
			case 0:
				Cerrar(Directorio);
				printf("Fin.\n");
				return 0;
			case 1:
			{
                printf ("Nombre delarchivos:");
				GetString(temp.name);
				printf ("Contenido: ");
				gets(temp.cont);
				printf ("Tamano: ");
				scanf ("%d", &temp.tam);
				
				int numero;
				numero=temp.tam;	
				for (int x=0;x<12;x++) { 
				temp.tBin[x]=numero%2; 
				printf("%d",temp.tBin[x]); 
				numero=numero/2; 
				if(numero==0) 
				break; 
				} 
				
                printf ("\n");
                temp.valido =1;

				if (Insertar (Directorio, &temp) < 0) {
					printf ("Error creando al archivo.\n");
				}
				else {
					printf ("archivos insertado correctamente\n");
				}
				break;
			}

			case 2:
			    {
		int opt;
		printf ("\n");

 				  int num_regs = Registros (Directorio);
				  // es la cantidad de registros que se quiere leer
				  int offset = 0;
				  // es el registro a partir del cual se desea comenzar la lectura
				  if (Leer(Directorio, buf, num_regs, offset) < 0)
                      {
					  printf("Error leyendo de la unidad\n");
				      }
				  else
                   {
                    printf ("\n");
                    int i;
					for (i = 0; i < num_regs; ++i)
                     {
                      printf(" ..%d %s, Previsualizacion: %s ,: %d bytes ",i,buf[i].name, buf[i].cont, buf[i].tam);
                      
                      	for(int j=0;j<12;j++){
                     	printf("%d",buf[i].tBin[j]);
					 	}
						printf ("bytes \n");
                     }
                     
                   }
				  printf("Se encontraron %d archivos en la unidad\n",
						num_regs);
			break;
                }
                
        
         }
    }
}


