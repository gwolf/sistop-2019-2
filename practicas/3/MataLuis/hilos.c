#include  <stdio.h>
#include  <stdlib.h>
#include  <string.h>
#include  <unistd.h>
#include  <pthread.h>

void *hola() {
	char *msg = "Hola";
	int i;

	for ( i = 0; i < strlen (msg); i++ ) {
		printf (" %c", msg[i]);
		fflush (stdout );
		usleep (1000000) ;
	}
}
void *mundo() {
	char *msg = " mundo ";
	int i;

	for ( i = 0 ; i < strlen (msg) ; i++ ) {
		printf (" %c", msg[i]);
		fflush (stdout );
		usleep (1000000) ;
	}
}

int  main(){
	pthread_t  h1;
	pthread_t  h2;
	pthread_create(&h1, NULL, hola , NULL);
	pthread_create(&h2, NULL, mundo , NULL);
	printf ("Fin\n");
return 0;
}
