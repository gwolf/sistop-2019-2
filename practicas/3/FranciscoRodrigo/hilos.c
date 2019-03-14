#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
#include <pthread.h> 
  
int g = 0;  //variable global
  
void *mihilo(void *vargp) 
{ 
    int *myid = (int *)vargp; 
    static int s = 0; 
 
    ++s; ++g; 

    printf("El hilo: %d,tiene un var. estatica: %d, y una var. global: %d\n", *myid, ++s, ++g); 
} 
  
int main() 
{ 
    pthread_t hilito; 

    for (int i = 0; i < 3; i++) 
        pthread_create(&hilito, NULL, mihilo, (void *)&hilito); 
  
    pthread_exit(NULL); 
    return 0; 
} 