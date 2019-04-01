#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <iomanip>
#include <time.h>
using namespace std;

struct Pro {
int id;
float llegada;
float tiempo;
float espera; 
}process[5];


int ACualAtiendo(struct Pro){
	int temp,aux;
	
	int i,j;
	int li[5];
	
	for(int x=0; x<6; x++){
	
		li[x]=process[x].llegada;}
		
	   for(int x=0; x<6; x++){
	 //printf("\nc mamo %i",li[x]);
	 }   
	 
	  printf("\n-----------------´");	
	  int max = process[0].llegada;
   	for (int i = 0; i < 6; i++)
        {
            if (process[i].llegada <  max)

                max = process[i].llegada;
		}

	 // printf("\naux-%i",max);
	  return max;
	             
}
int DeDondeSoy(struct Pro,int y){
	int i=0;
	int aux=0;
	
	for (int i = 0; i < 6; i++)
        {
            if (process[i].llegada ==  y){
                aux = process[i].id;}
		}
		return aux;
}
int EjecutaFIFO(struct Pro,int u){
	char tmp;
	tmp=u;
	for (int i = 0; i < 6; i++)
        {
			
				printf("\n se esta ejecutando %c por %.3f",process[i].id,process[i].tiempo);		
			}
	
	
}
void ALaCola(struct Pro){

struct Pro swap;

	for (int i = 0;i < 6; i++){
		for (int j = 0; j< 6-1; j++){
			if (process[j].llegada > process[j+1].llegada){
        swap       = process[j];
        process[j]   = process[j+1];
        process[j+1] = swap;
      }
	  }
}
     /* for(int x=0; x<6; x++){
	 printf("\nc mamo %c",process[x].id);
	 } */  
    
    
}
void Imprimir(struct Pro){
	int t=0;
	printf("\n\nGrafica con fifo\n");
    printf("-",t++);

while (t<process[0].llegada){
printf("-",t++);	
}
printf("|");
	for(int i=0;i<6;i++){
		
		for(int j=0;j<process[i].tiempo;j++){
		printf("%c",process[i].id);
		}
		printf("|");
	   	}

  }

void PreparaRRQ(struct Pro,int q){
/*	int nVueltas[6];
	int Dif[6];
	int c=0;
	for(int i=0;i<6;i++){
		nVueltas[i]=process[i].tiempo/q;
		Dif[i]=process[i].tiempo-(nVueltas[i]*q);
		printf("\n %c [%i] %i: ",process[i].id,i,nVueltas[i]);
		printf("restante %i\n",Dif[i]);	
	}
	*/
	int l=0;
	int c=0;
	int v=0;
	printf("\n ");
	while(l<=6){
	
			if(process[l].tiempo>0){
			for(int u=0;u<3;u++){
			
			printf("%c",process[l].id);
			process[l].tiempo=process[l].tiempo-1;
			}
		printf("|");
		}else{
			l++;
		}
		
	}
}


int main() {
	process[0].id='a';
	process[1].id='b';
	process[2].id='c';
	process[3].id='d';
	process[4].id='e';
	process[5].id='f';
	
	srand (time(NULL)); 
	process[0].llegada = rand() % 30; 
	process[1].llegada = rand() % 30; 
	process[2].llegada = rand() % 30; 
	process[3].llegada = rand() % 30; 
	process[4].llegada = rand() % 30; 
	process[5].llegada = rand() % 30; 

	process[0].tiempo = rand() % 10+1; 
	process[1].tiempo = rand() % 10+1; 
	process[2].tiempo = rand() % 10+1; 
	process[3].tiempo = rand() % 10+1; 
	process[4].tiempo = rand() % 10+1; 
	process[5].tiempo = rand() % 10+1; 
	
	printf("\nInicio %c: %.3f duraacion: %.3f",process[0].id,process[0].llegada,process[0].tiempo);
	printf("\nInicio %c: %.3f duraacion: %.3f",process[1].id,process[1].llegada,process[1].tiempo);
	printf("\nInicio %c: %.3f duraacion: %.3f",process[2].id,process[2].llegada,process[2].tiempo);
	printf("\nInicio %c: %.3f duraacion: %.3f",process[3].id,process[3].llegada,process[3].tiempo);
	printf("\nInicio %c: %.3f duraacion: %.3f",process[4].id,process[4].llegada,process[4].tiempo);
	printf("\nInicio %c: %.3f duraacion: %.3f",process[5].id,process[5].llegada,process[5].tiempo);
	
	int p;
	int o;
	p=ACualAtiendo(*process);
	printf("\na atender a %i",p);
	o=DeDondeSoy(*process,p) ;
	printf("\n se ejecutara %c ",o);
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	ALaCola(*process);
	EjecutaFIFO(*process,o);
	Imprimir(*process);
	 PreparaRRQ(*process,3);
	

}

