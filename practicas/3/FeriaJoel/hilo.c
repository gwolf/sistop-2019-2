#include <stdio.h>
#include <windows.h>
 
DWORD WINAPI hilo(LPVOID LPARAM);
 
 
int main()
{
HANDLE MiHilo;
DWORD  IdDelHilo;
 
MiHilo=CreateThread(NULL,0,hilo,NULL,0,& IdDelHilo);
 MessageBox(NULL,"2","ventana",MB_OK);
 
return 0;
}
 
DWORD WINAPI hilo(LPVOID LPARAM)
{
   MessageBox(NULL,"1","ventana",MB_OK);
 
}


