#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <sys/mman.h>
#include <semaphore.h>
#include <string.h>

#define SEMAPHORES 1

int main()
{
  char *x = mmap(NULL, sizeof(char)*10, PROT_READ | PROT_WRITE,
               MAP_SHARED | MAP_ANONYMOUS, -1, 0);
  strcpy(x, "0");

  int i;
  int child;
  sem_t *semaforo = mmap(NULL, sizeof(sem_t), PROT_READ | PROT_WRITE,
             MAP_SHARED | MAP_ANONYMOUS, -1, 0);
  int temp;
  sem_init (semaforo, 1, 1);
  for (i=0; i<10; ++i)
    {
      child = fork();
      if (child==0)
    {
      usleep(rand()%20000);

      if (SEMAPHORES)
        sem_wait(semaforo);
      printf("[%d] Trying to access the resource\n", getpid());
      temp=atoi(x);
      printf("[%d] Using the resource\n", getpid());
      temp++;
      sprintf(x, "%d", temp);

      if (SEMAPHORES)
        sem_post(semaforo);
      printf("[%d] Just used the resource\n", getpid());
      usleep(rand()%20000);

      if (SEMAPHORES)
        sem_wait(semaforo);
      printf("[%d] Trying to access the resource\n", getpid());
      temp=atoi(x);
      printf("[%d] Using the resource\n", getpid());
      temp++;
      sprintf(x, "%d", temp);

      if (SEMAPHORES)
        sem_post(semaforo);
      printf("[%d] Just used the resource\n", getpid());
      printf("[%d] EXITING\n", getpid());
      exit(1);
    }
    }

   while (wait(NULL)>=0);

  printf("x is: %s\n", x);
  munmap(x, sizeof(int));
  munmap(semaforo, sizeof(sem_t));

  return 0;
}
