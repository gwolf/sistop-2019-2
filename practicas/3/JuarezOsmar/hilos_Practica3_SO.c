/*JuarezAguilarOsmar
 Se crean dos hilos y se ejecutan al mismo tiempo 
 El hilo uno incrementa en dos una varible global
 El hilo dos incrementa en uno la misma variable global
 Este ejemplo hace el uso de semaforos(implementando un mutex) para tener una sincronizacion
 de los dos hilos y que la suma total sea consistente*/

#include <stdio.h>
#include <stdlib.h> 
#include <pthread.h>
int count=5;
int sumaTotal=0;
pthread_mutex_t mutex;

void accionHilos(void *args){ 
	char * hiloID = (char *) args;
	pthread_mutex_lock(&mutex);
	if(hiloID=="1"){
		printf("Hola soy el hilo %c  (*.*)/  y tengo el control\n", *hiloID);
		sumaTotal = sumaTotal + 2; 	
	} else{

		printf("Hola soy el hilo %c  (-.-)/  y tengo el control\n", *hiloID);
		sumaTotal = sumaTotal + 1; 	
	}
	printf("La suma es: %d \n", sumaTotal);
	pthread_mutex_unlock(&mutex);
	printf("EL Hilo %c se va\n", *hiloID);
}

int main(void){
	int i;
	char *hiloU="1";
	char *hiloD="2";

	pthread_mutex_init(&mutex, NULL); 
	pthread_t hiloUno;
	pthread_t hiloDos;

	for(i=0; i<=count; i++){
		
		pthread_create(&hiloUno, NULL, (void*) accionHilos, (void*) hiloU);
	}

	for(i=0; i<=count; i++){

		pthread_create(&hiloDos, NULL, (void*) accionHilos, (void*) hiloD);
	}
	pthread_join (hiloUno, NULL);
	pthread_join (hiloDos, NULL);
	
	printf("La suma total es: %d \n", sumaTotal);
	return 0;
}