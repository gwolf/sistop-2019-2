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

    sistema.close()


def obtenerinfo():
    sistema = open(directorio,'r')
    for i in range(5):
        sistema.seek(aux1(i))
        query = sistema.read(aux2(i))
        info.append(query)

    sistema.close()
