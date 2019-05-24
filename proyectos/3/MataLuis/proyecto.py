directorio = 'fiunamfs.img'
tamano_dato = 64
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
