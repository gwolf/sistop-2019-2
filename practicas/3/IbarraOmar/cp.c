/* cp.c */
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdio.h>
#define  BUFSIZE 512
#define  PMODE 0644 /* RW propietario, R grupo y otros */
 
int main(int argc, char *argv[]) /* cp: copia fd1 a fd2 */
{
  int fd1, fd2, n;
  char buf[BUFSIZE];
 
  if (argc != 3)
     error("Usar: cp origen destino", NULL);
 
  if ((fd1 = open(argv[1], 0)) == -1)
     error("cp: no se puede abrir \%s", argv[1]);
 
  if ((fd2 = creat(argv[2], PMODE)) == -1)
     error("cp: no se puede crear \%s", argv[2]);
 
  while ((n = read(fd1, buf, BUFSIZE)) > 0)
     if (write(fd2, buf, n) != n)  error("cp: error al escribir", NULL);
 
  exit(0);
}
 
void error(char *s1, char *s2) /* imprime un mensaje de error y termina */
{
  printf(s1, s2);
  printf("\n");
 
  exit(1);
}
