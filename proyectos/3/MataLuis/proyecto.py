directorio = 'fiunamfs.img'
tamano_dato = 64
aux1 = [0, 10, 20, 40, 47, 52]
aux2 = [8, 3, 15, 5, 2, 8]
info = []
tamano = []
ubicacion = []

def obtenerarchivos():
    sistema = open(directorio,'r')
    posicion = 1024
    while posicion < 5120:
        sistema.seek(posicion)
        query = sistema.read(15)
        
        if query != 'AQUI_NO_VA_NADA':
            info.append(query.replace(" ", ""))
            sistema.seek(posicion+16)
            tamano.append(int(sistema.read(8)))
            sistema.seek(posicion+25)
            ubicacion.append(int(sistema.read(5)))
        posicion = posicion + 64

    posicion = 5120    
    sistema.close()


def obtenerinfo():
    sistema = open(directorio,'r')
    for i in range(5):
        sistema.seek(aux1(i))
        query = sistema.read(aux2(i))
        info.append(query)

    sistema.close()

def copiarPC(archivo):
    sistema = open(directorio, 'r+b')
    posicion_archivo = archivos.index(archivo)
    tamano_archivo = tamano[posicion_archivo]
    ubicacion_archivo = ubicacion[posicion_archivo]*1024
    sistema.seek(ubicacion_archivo)

    copia_archivo = open(archivo,'wb')
    copia.write(sistema.read(tamano_archivo))
    sistema.close()

def eliminar(archivo): 
    sistema = open(directorio,'r+')
    posicion = 1024
    sistema.seek(posicion)
    while posicion < 5120:
        nombre_archivo = sistema.read(15)
        archivo_act = nombre_archivo.strip()
        
        if archivo_act == archivo:
            sistema.seek(posicion)
            sistema.write("AQUI_NO_VA_NADA")
            sistema.wirte('0'*49)
        
            for i in range(len(archivos)):
                info.pop(0)
                tamano.pop(0)
                ubicacion.pop(0)
            obtenerarchivos()
        else:
            posicion = posicion + 64
            sistema.seek(posicion)
    sistema.close
       
