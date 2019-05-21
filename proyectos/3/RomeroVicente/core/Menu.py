class Menu:
    def __init__(self):
        self.exit = False

    def print_menu(self):
        print("Selecciona la accion")
        print("1.Listar directorio")
        print("2.Copiar de FS a sistema externo")
        print("3.Copiar de sistema externo a FS")
        print("4.Eliminar archivo")
        print("5.Desfragmentar")
        print("6.Salir")
    
    def seleccionar_accion(self,opcion):
        
        if(opcion == 1):
            self.listar_contenido()
        elif(opcion == 2):
            self.listar_contenido()
            source = input("escribe el nombre del archivo que deseas copiar")
            dest = input("escribe la ruta donde deseas escribir el archivo")
            self.copiar_FS_a_eXFS(source,dest)
        elif(opcion == 3):
            self.listar_contenido()
            source = input("escribe la ruta del archivo que deseas añadir al FS\n_ ")
            self.copiar_eXFS_a_FS(source)
        elif(opcion == 4):
            self.listar_contenido()
            name = input("introduce el nombre del archivo a eliminar")
            self.delete(name)
        elif(opcion == 5):
            print("Se desfragmenta el FS")
            pass
        elif(opcion == 6):
            print("se procede a salir del programa")
            self.exit = True
        else:
            print("opcion invalida")
    
    def iniciar_menu(self):
        while self.exit == False:
            self.print_menu()
            opcion = input("_")
            self.seleccionar_accion(int(opcion))