#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#define BUFSIZE 1024
//long int Ubicacion;
int Conta = 1024 , Recorre = 0;
int fd,fd1, fd2, cerrar,Lugar[64];
char buf[BUFSIZE];
char Nombre_archivo[64][16], T_archivo[64][9];
char Version_FS[4],Cluster_inicial[64][6],Aqui_no_va_nada[64];
char Fecha_creacion[15], Fecha_modificacion[15];
char Nombre_FS[9];

void lista(){
	while (Conta < 5120)
	{
   		lseek(fd,Conta,SEEK_SET);	//Recorre al bit 1024, al nombre del archi
		read(fd,&Nombre_archivo[Recorre],15);   //lee los 15 carcateres que mide el archivo
		Nombre_archivo[Recorre][15]='\0';
	   	lseek(fd,Conta+16,SEEK_SET);	
		read(fd,&T_archivo[Recorre],8);	
	        T_archivo[Recorre][8]='\0';
	   	lseek(fd,Conta+25,SEEK_SET);
		read(fd,&Cluster_inicial[Recorre],5);	
		Cluster_inicial[Recorre][5]='\0';
		if (strcmp(Nombre_archivo[Recorre], "AQUI_NO_VA_NADA") != 0){
		   	lseek(fd,Conta+31,SEEK_SET);
			read(fd,&Fecha_creacion,14);	
			Fecha_creacion[14]='\0';
	   		lseek(fd,Conta+46,SEEK_SET);
			read(fd,&Fecha_modificacion,14);	
			Fecha_modificacion[14]='\0';
		
		  	printf("Nombre del archivo: %s\n",Nombre_archivo[Recorre]);
			printf("EL tamano del archivo: %s\n",T_archivo[Recorre]);
	  		printf("El cluster inicial es: %s\n",Cluster_inicial[Recorre]);
	  		printf("La fecha de creacion es: %s\n",Fecha_creacion);
 		 	printf("La fecha de modificacion es: %s\n",Fecha_modificacion);
			printf("\n\n"); 
			Aqui_no_va_nada[Recorre]=0; //hay algo
			Lugar[Recorre]= -1;
		}else{
		Aqui_no_va_nada[Recorre]=1; //no hay nada
		Lugar[Recorre]=Conta;
		}
		Recorre++;
		Conta = Conta + 64;
   	}
}

void Copiar_a_mi_sistema(){
	char Archivo_a_copiar[16];
	int i,j,cuenta1[64],cuenta2=0, Ubicacion[64],n,aux=0,coin=0;
	for(j = 0; j < 64; j++){
		Ubicacion[j]=-1;
		cuenta1[j]=0;
	}
	
	printf("Ingresa el nombre del archivo que deseas copiar a tu maquina:  ");
	scanf("%s",Archivo_a_copiar);
	/*for(int i = 0; i < 64;i++){
		printf("El archivo %d es: %s\n",i,Nombre_archivo[i]);
		printf("El archivo %d pesa: %s\n",i,T_archivo[i]);
		printf("El archivo %d esta en el bloque: %s\n",i,Cluster_inicial[i]);
	}*/
	
	cuenta2=strlen(Archivo_a_copiar)+1; //Se agraga uno por el final de lina (\0)
	
	for(i = 0; i < 64; i++){
		for(j = 0; j < 16; j++){
			if (strcmp(Nombre_archivo[i], "AQUI_NO_VA_NADA") != 0)
				if(Nombre_archivo[i][j] != ' ')
					cuenta1[i]=cuenta1[i]+1;		
		}
	}
	
	for(j = 0; j < 64; j++)
		if(cuenta1[j] == cuenta2){
			Ubicacion[j]=j;
		}
	
	char coinsidencia1[cuenta2+1], coinsidencia2[cuenta2+1];
	
	int espacios = 16 - cuenta2, ubi=0;
	for(i = 0; i < 64; i++){
		if (Ubicacion[i] != -1){
			for( j = 0; j < cuenta2; j++){
				coinsidencia1[j]=Nombre_archivo[i][espacios+j];
				coinsidencia2[j]=Archivo_a_copiar[j];
				ubi=i;
			}
		}
	}	
	
	int new = atoi(Cluster_inicial[ubi]) * BUFSIZE;//cluster en el que inicia * 1024
	if (strcmp(coinsidencia1, coinsidencia2) == 0 ) {
		//printf("Cluster: %s", Cluster_inicial[ubi]);
		fd1=creat(Archivo_a_copiar,0644);
		lseek(fd,new,SEEK_SET);
		char buf[atoi(T_archivo[ubi])];
		n = read(fd, buf, atoi(T_archivo[ubi]));
	  	write(fd1, buf, n);
	}else{
		printf("No se encontro el archivo");}
		
	
}

void Copiar_de_mi_sistema(){
	char Archivo_a_pegar[16];
	struct stat bufe;
	int ok,n,m = 0,valor=0;
	long int posicion;
	printf("Ingresa el nombre del archivo que deseas copiar de tu maquina:  ");
        scanf("%s",Archivo_a_pegar);
	fd2=open(Archivo_a_pegar,O_APPEND);
	ok = stat(Archivo_a_pegar,&bufe);
	//printf (" %ld\t", buf.st_size);
	while (Aqui_no_va_nada[m] == 0){
		m++;
	}
        posicion=lseek(fd,0L,SEEK_END);
	//printf("Posicion: %ld",posicion);
	if (posicion % 1024 != 0){
		valor=(posicion / 1024);
		valor= posicion- (valor*(1024));
		valor=1024 - valor;
		posicion=posicion +valor;	
	}
	//printf("Posicion: %ld",posicion);
	int c = posicion / 1024;
	lseek(fd,posicion,SEEK_SET);
        char buf[bufe.st_size];
        n = read(fd2, buf, bufe.st_size);
        write(fd, buf, n);
	lseek(fd,Lugar[m],SEEK_SET);//Archivo_a_pegar[m]
	lseek(fd,Lugar[m]+16,SEEK_SET);//bufe.st_size[m]
	lseek(fd,Lugar[m]+25,SEEK_SET);//c
	char fecha[14];
        struct tm *tmPtr;
        tmPtr = localtime(&bufe.st_ctime);
        strftime( fecha, 14, "%Y%m%d%H%M%S", tmPtr );
	lseek(fd,Lugar[m]+31,SEEK_SET);//fecha
        tmPtr = localtime(&bufe.st_mtime);
        strftime( fecha, 14, "%Y%m%d%H%M%S", tmPtr );
	lseek(fd,Lugar[m]+46,SEEK_SET);//fecha
	}


void Eliminar(){
	int i,j,cuenta1[64],cuenta2=0, Ubicacion[64],n,aux=0,coin=0;
	char Archivo_a_eliminar[16];

	printf("Ingresa el nombre del archivo que deseas eliminar de tu maquina:  ");
        scanf("%s",Archivo_a_eliminar);
	cuenta2=strlen(Archivo_a_eliminar)+1; //Se agraga uno por el final de lina (\0)

        for(i = 0; i < 64; i++){
                for(j = 0; j < 16; j++){
                        if (strcmp(Nombre_archivo[i], "AQUI_NO_VA_NADA") != 0)
                                if(Nombre_archivo[i][j] != ' ')
                                        cuenta1[i]=cuenta1[i]+1;
                }
        }

        for(j = 0; j < 64; j++)
                if(cuenta1[j] == cuenta2){
                        Ubicacion[j]=j;
                }

        char coinsidencia1[cuenta2+1], coinsidencia2[cuenta2+1];

        int espacios = 16 - cuenta2, ubi=0;
        for(i = 0; i < 64; i++){
                if (Ubicacion[i] != -1){
                        for( j = 0; j < cuenta2; j++){
                                coinsidencia1[j]=Nombre_archivo[i][espacios+j];
                                coinsidencia2[j]=Archivo_a_eliminar[j];
                                ubi=i;
                        }
                }
        }
	
	int new = atoi(Cluster_inicial[ubi]) * BUFSIZE;//cluster en el que inicia * 1024
        if (strcmp(coinsidencia1, coinsidencia2) == 0 ) { 
                fd5=open(/dev/zero,O_RDONLY);
		lseek(fd,new,SEEK_SET);
                char buf[atoi(T_archivo[ubi])];
                n = read(fd5, buf, atoi(T_archivo[ubi]));
                write(fd, buf, n); 
        }else{
                printf("No se encontro el archivo");}


}

void main (int argc, char *argv[]) {
	
	fd=open("fiunamfs.img",O_RDWR);  //Abre el archivo
   	read(fd,&Nombre_FS,8);		//Leer el nombre del sistema de archivos
	Nombre_FS[8]='\0';
	lseek(fd,10,SEEK_SET);		//Reecorre al bit 10, donde esta la version
   	read(fd,&Version_FS,3);   	//lee 3 bits a partir de donde esta
        Version_FS[3]='\0';

	if (strcmp(Nombre_FS, "FiUnamFS") == 0){
        	//printf ("fd = %d\n",fd); 	//Imprime el descriptor de archivo
		printf("El filesystem es: %s\n",Nombre_FS);
		printf("Version: %s\n\n\n",Version_FS); 
		lista();
		Copiar_a_mi_sistema();
		Copiar_de_mi_sistema();
		Eliminar();
   	}else{
		printf("No es un sistema de archivos valido FiUnamFS");
	}
        
   	cerrar = close(fd);	
}



