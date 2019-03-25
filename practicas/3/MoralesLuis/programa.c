#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

void *pedirRecurso(void *id);
pthread_mutex_t mutexHilo;

int main(){
	pthread_t idHilo;
	pthread_mutex_init (&mutexHilo, NULL);
	int i;
	for (i=0;i<5;i++){
		pthread_mutex_lock (&mutexHilo);
		
		pthread_create (&idHilo, NULL, pedirRecurso, (void *)&idHilo);
		
		pthread_mutex_unlock (&mutexHilo);

	}
	pthread_exit(NULL);
	return 0;
}

void *pedirRecurso(void *id){
	int *identificador=(int *)id;
	
	printf("soy el hilo %d y estoy pidiendo un recurso al sistema\n",*identificador);
	usleep(3000);
}
