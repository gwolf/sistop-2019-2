#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void *procesoSeparado(void *data)
{
	char *texto = (char *) data;
	struct timespec tiempo = {1, 0};
	while (1) {
		printf("%s\n",texto);
		pthread_delay_np(&tiempo);
	}
	}


int main(void)
{
	pthread_t proceso1;
	pthread_t proceso2;
	pthread_create(&proceso1, NULL, &procesoSeparado, "hola");
	pthread_create(&proceso2, NULL, &procesoSeparado, "adios");
    pthread_join(proceso1, NULL);
    pthread_join(proceso2, NULL);
    return 0;
}
