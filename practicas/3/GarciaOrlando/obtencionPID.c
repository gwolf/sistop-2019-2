#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int main (int argc, char *argv[]){
	pid_t pid;

	pid  =fork(); //Crear un hilo extra aparte del que  esta
	if(pid == -1){
		printf("No se pudo realizar el fork\n");
		return -1;
	}else{
	if(!pid){
		printf("Proceso hijo: PID %d\n",getpid());
	}else{
		printf("Proceso padre: PID %d\n",getpid());
		printf("\n\n");
	}
	}
	return 0;
}
