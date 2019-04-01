#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
void main(int argc, char **argv){
	
	system("clear");
		
	pid_t pid;
	int a;
 
  	if  ((pid=fork())==0) {
      		printf ("El hijo, ID = %ld\n", (long)getpid());
      		// El codigo del hijo va aqui
		sleep(3);
		system("gnome-terminal -- ./omar_ibarra.proyecto_sistemas.sh");
	} else if (pid>0) {
      		printf ("El padre, ID = %ld\n", (long)getpid());
      		// El codigo del padre va aqui 
		system("gnome-terminal -- htop ");
  	}

}

