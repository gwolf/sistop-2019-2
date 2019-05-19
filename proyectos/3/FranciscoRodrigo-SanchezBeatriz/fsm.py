from fifs import FIFS
import sys

def main():
    fs = FIFS()
    # Seguro que existe un método muchisimo mejor para emular swith case
    # Solo falta buscarlo e implementarlo
    if len(sys.argv) > 1:
        if sys.argv[1] == "ls":
            fs.ls()
        elif sys.argv[1] == "rm":
            if len(sys.argv) == 3:
                fs.rm(sys.argv[2])
                #fs.rm("README.org")
            else:
                print("rm: miss operand")
        elif sys.argv[1] == "cpout":
            # de momento no hay posibilidad de copiar a otro directorio
            if len(sys.argv) == 3:
                fs.cpout(sys.argv[2],"./")
                #fs.cpout("mensaje.png","./")
            else:
                print("cpout: miss operand")
        elif sys.argv[1] == "cpin":
            # de momento no hay posibilidad de copiar a otro directorio
            if len(sys.argv) == 3:
                fs.cpin(sys.argv[2])
            else:
                print("cpin: miss operand")
        else :
            print("Invalid command")
    else :
        print("Please enter a command or use help")

    fs.close()

if __name__ == '__main__':
    main()
