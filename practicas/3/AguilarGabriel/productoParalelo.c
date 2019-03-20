//Aguilar Luna Gabriel Daniel
//El archivo lleva a cabo el producto punto de dos vectores, de longitud variable, con procesamiento en paralelo
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<omp.h>
void  prodpunto(int*,int*,int);
void funcionArr(int*,int);
int main()
{
	srand(time(NULL));
	 int n=rand()%11+1;
	 printf("Tamaño de los vectores: %d\n",n);
	 int vector1[n],vector2[n];
	 funcionArr(vector1,n);
	 funcionArr(vector2,n);
	 prodpunto(vector1,vector2,n);
}
void funcionArr(int* vector,int n)
{
	 for(int i=0;i<n;i++)
	 {
	 	vector[i]=rand()%11;
	 	printf("%4d", vector[i]);
	 }
	 printf("\n");
}
void prodpunto(int* vect1, int* vect2, int n){
	
	int i,tid,nth;
	int res=0, resp[n];

	#pragma omp parallel for reduction(+:res)
		for (i = 0; i < n; ++i){
			res+=vect1[i]*vect2[i];
			printf("%3d", vect1[i]*vect2[i]);
			if (i+1<n){
				printf(" +");
			}
		}
		printf(" =%d\n", res);
}

