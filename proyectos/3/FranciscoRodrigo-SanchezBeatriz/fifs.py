import mmap

class SuperBlock :
    """
        El superbloque para este sistema de archivos ocupa el primer cluster
        del mismo, es decir, ocupa 1024
    """

    f = open('../fiunamfs.img','r+b')
    fs_map = mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)

    # Suberblock information
    name            = fs_map[0:8].decode('utf-8')         # FiUnamFS
    version         = fs_map[10:13].decode('utf-8')       # 0.4
    tagv            = fs_map[20:35].decode('utf-8')       # Mi Sistema
    size_cluster    = int(fs_map[40:45].decode('utf-8'))  # 1024
    numdir_cluster  = int(fs_map[47:49].decode('utf-8'))  # 04
    total_cluster   = int(fs_map[52:60].decode('utf-8'))  # 00001440
    size_dentry     = 64                                  # size dir entry

    f.close()
    fs_map.close()

class Inode :
    """
        De hecho, estrictamente esta clase no es un inode ya que estamos
        guardando el nombre del archivo en él y eso no pasa en los verdaderos
        inodes y obviamente tampoco estamos guardando
        permisos ni propietarios porque NO los tenemos
    """
    offset_fname  = 15
    # offset_fsize = 8
    # offset_fcluster = 5
    # offset_fcreated = 14
    # offset_fmodif = 14

    fname = ""         # 0-15
    fsize = 0          # 16-24
    finit_cluster = 0  # 25-30
    fcreated = ""      # 31-45
    fmodif = ""        # 46-60
    numdir = -1        # numero entre 0-63
                       # por las especificaciones

    def __init__(self, dir_entry):
        self.fname = dir_entry[0:15].decode('utf-8').lstrip()
        self.fsize = int(dir_entry[16:24].decode('utf-8'))
        self.finit_cluster = int(dir_entry[25:30].decode('utf-8'))
        self.fcreated = dir_entry[21:45].decode('utf-8')
        self.fmodif = dir_entry[46:60].decode('utf-8')

class FIFS:
    """FIFS es el sistema de archivos de la Facultad de Ingenieria.
        Para la implementacion de las funciones de este controlador de
        sistema de archivos se estan usando la convencion siguiente
        convención
        * para mostrar el directorio usamos
            ls
        * para eliminar un archivo usamos
            rm [FILE]
        * para copiar un archivo a nuestro sistema
            cpout [FILE]
        * para copiar un archivo alsistema
            cpin [FILE]
        * para desfragmentar
            defrag
    """
    f = open('../fiunamfs.img','a+b')
    fs_map = mmap.mmap(f.fileno(),0,access=mmap.ACCESS_WRITE)

    sb = SuperBlock()

    dentry_notused ='AQUI_NO_VA_NADA'

    def ls(self):
        # usamos del 1-4 clusters, es decir 1024*4 = 4096
        # las entradas miden 64 por lo tanto 4096/64 = 64, entonces el rango
        # del for 0-64
        for j in range(0,64):
            # Como analogia a lo que vimos en la seccion de admin de procesos
            # ptrb es un puntero base que nos indica donde empiezan
            # los metadatos de los archivos y con eso conseguimos que
            # ya solo tengamos que sumarle un desplazamiento.

            # El directorio se encuentra en los cluster de 1-4 y cada cluster
            # mide 1024 por lo tanto debemo ir en 1024, el cluser 0 es el
            # superblock
            prtb = self.sb.size_cluster + j*self.sb.size_dentry
            i = Inode(self.fs_map[prtb:prtb + self.sb.size_dentry])
            if self.dentry_notused != i.fname:
                print("%s\t%d\t%d" %(i.fname,i.finit_cluster,i.fsize))

    def search(self,fe):
        for j in range(0,64):
            prtb = self.sb.size_cluster + j*self.sb.size_dentry
            i = Inode(self.fs_map[prtb:prtb + self.sb.size_dentry])
            if fe == i.fname:
                i.numdir = j
                return i
        return None

    def rm(self,fe):
        #Primero buscar si el archivo existe,
        #si existe, perdemos la ref hacia él
        i = self.search(fe)
        if i is None :
            print("rm: " + fe + " : No such file ")
        else :
            prtb = self.sb.size_cluster + self.sb.size_dentry*i.numdir
            self.fs_map[prtb:prtb + i.offset_fname] = bytes(self.dentry_notused,'utf-8')

    def cpout(self,fe,dir):
        #Primero buscar si el archivo existe,
        #si existe, lo copiamos al directorio especificado
        i = self.search(fe)
        if i is None :
            print("cpout: " + fe + " : No such file ")
        else :
            prtb = self.sb.size_cluster + self.sb.size_dentry*i.numdir
            filecp = open(fe,"a+b")
            cluster = self.sb.size_cluster*i.finit_cluster
            # operacion : 1024*inicio_cluster_del_archivo_a_copiar
            filecp.write(self.fs_map[cluster:cluster + i.fsize])
            filecp.close()

    def cpin(self,fe):
        print("Not build yet")
        # Pseudocodigo
        # Buscar si no hay un archivo con el nombre recibido
        # Si no entonces
        #   buscar un lugar donde quepa el archivo
        #   sino hay lugar, desfragmentamos
        #   si despues de desfragmentar no hay lugar
        #       mandar error
        # Si sí, pedir que renombre el archivo

    def close(self):
        self.fs_map.close()
        self.f.close()
