import mmap
import os
from core.Menu import Menu
from datetime import datetime
from math import ceil
import datetime
import time

class FiUnamFS(Menu):
    ##  Este metodo inicializa un nuevo FS creando su superbloque y llenando el indice de directorio
    @staticmethod
    def create_new_fs(root,name_vol):
        if name_vol == None:
            name_vol = "NUEVO_VOL"
            size_name_vol = len(name_vol)
            if size_name_vol < 35 - 20:
                 sobrante_name_vol = (35 - 20) - size_name_vol
        with open(root,"w+") as f:
            f.write(("\x00"*(1024*1440)))
            fs = mmap.mmap(f.fileno(),0)
            fs[0:8] = "FiUnamFS".encode('ascii')
            fs[10:13] = "0.4".encode('ascii')
            fs[20:35] = str(("0"*sobrante_name_vol)+name_vol).encode('ascii')
            fs[40:45] = "01024".encode('ascii')
            fs[47:49] = "04".encode('ascii')
            fs[52:60] = "00001440".encode('ascii')
            for i in range(64):
                FiUnamFS.write_input_dir(fs,i)
            fs[1024*5:] = str("\x00"*(1024*1435)).encode('ascii')
            f.close()
    
    ## Este metodo escribe una entrada en el indice de directorio del FS persistente
    def write_input_dir(FS,id,name_file="AQUI_NO_VA_NADA",size_file="",inic_cluster="",cdate="",mdate="",no_use=""):
        offset = 1024
        size_input_dir = 64
        id = int(id)
        try:
            FS[offset+(size_input_dir*id):offset+(size_input_dir*id)+15] = ((" "*(15-len(str(name_file))))+str(name_file)).encode('ascii')
        except:
            print("Nombre no valido")
            return False
        FS[offset+(size_input_dir*id)+16:offset+(size_input_dir*id)+24] = ("0"*(8-len(str(size_file)))+str(size_file)).encode('ascii')
        FS[offset+(size_input_dir*id)+25:offset+(size_input_dir*id)+30] = ("0"*(5-len(str(inic_cluster)))+str(inic_cluster)).encode('ascii')
        FS[offset+(size_input_dir*id)+31:offset+(size_input_dir*id)+45] = ("0"*(14 - len(str(cdate)))+str(cdate)).encode('ascii')
        FS[offset+(size_input_dir*id)+46:offset+(size_input_dir*id)+60] = ("0"*(14 - len(str(mdate)))+str(mdate)).encode('ascii')
        FS[offset+(size_input_dir*id)+61:offset+(size_input_dir*id)+64] = ("\x00"*(3 - len(str(no_use)))+str(no_use)).encode('ascii')
        return True





    # Este metodo lee del FS persistente el indice de directorio y lo asigna a memoria principal
    def parse_dir(self):
        for input_dir in range(self.num_input_dir):
            name_dir = self.map[1024+(64*input_dir):1024+(64*input_dir)+15].decode('ascii').replace(" ","")
            tam_archivo = int(self.map[1024+(64*input_dir)+16:1024+(64*input_dir)+24])
            cluster_inicial = int(self.map[1024+(64*input_dir)+25:1024+(64*input_dir)+30])
            fecha_creacion = int(self.map[1024+(64*input_dir)+31:1024+(64*input_dir)+45])
            fecha_modificacion = int(self.map[1024+(64*input_dir)+46:1024+(64*input_dir)+60])
            self.inputs_dir.append(dict(id=input_dir,name_dir=name_dir,size_file=tam_archivo,inic_cluster=cluster_inicial,
                                        fc = fecha_creacion, fm = fecha_modificacion))
    # Inicializa el FS y valida que sea un FS valido
    def __init__(self, root):
        super(FiUnamFS, self).__init__()
        self.root = root
        self.void_entrada_dir = "AQUI_NO_VA_NADA"
        # Valida que el FS sea archivo valido para inicializar 
        if os.path.isfile(self.root):
            with open(self.root,"r+") as f:
                self.map = mmap.mmap(f.fileno(),0)
                try:
                    self.nombre_FS = self.map[0:8].decode('ascii')
                except:
                    print("el sistema de archivos no es valido")
                    exit()
                self.version_FS = self.map[10:13].decode('ascii')
                self.etiqueta_vol = self.map[20:35].decode('ascii')
                self.size_of_cluster_FS = int(self.map[40:45].decode('ascii'))
                self.num_of_cluster_dir_FS = int(self.map[47:49].decode('ascii'))
                self.num_of_cluster_total_FS = int(self.map[52:60].decode('ascii'))
                self.files = {}
                dir_cluster_offset=1024
                size_input_dir = 64
                self.num_input_dir = int(self.size_of_cluster_FS/size_input_dir * self.num_of_cluster_dir_FS)
                self.inputs_dir = []
                self.descriptor_archivo = 0
                if self.nombre_FS != 'FiUnamFS':
                    print("el sistema de archivos no es valido")
                    exit()
            self.parse_dir()
        else:
            exit()
    # Obtiene una lista de los indices que contiene un nombre pasado por argumento
    def get_index_dir(self,name,key_out='id'):
        try:
            lista = []
            for elem in self.inputs_dir:
                if elem['name_dir'] == name:
                    lista.append(elem[key_out])
            return lista
        except:
            return -1
    # Obtiene una lista de los indices que no tienen el nombre predeterminado
    # Usado comunmente para obtener indices que no contienen la candena 'AQUI NO VA NADA'
    def get_index_not_dir(self,name):
        try:
            lista = []
            for elem in self.inputs_dir:
                if elem['name_dir'] != name:
                    lista.append(elem['id'])
            return lista
        except:
            return -1
    
    # Escribe en el archivo persistente el indice del directorio que esta en memoria principal
    def write_index_dir(self):
        dir_cluster_offset=1024
        size_input_dir = 64
        for input_dir in self.inputs_dir:
            FiUnamFS.write_input_dir(self.map,input_dir['id'],input_dir['name_dir'],input_dir['size_file'],input_dir['inic_cluster'],input_dir['fc'],input_dir['fm'])
        return True
    
     # Lista el contenido del FS
    def listar_contenido(self):
        for input_dir in self.inputs_dir:
            if input_dir["name_dir"] != self.void_entrada_dir:
                print("{0} {1} {2}".format(input_dir["name_dir"],input_dir['inic_cluster'],input_dir['size_file']))
    
    # regresa los datos del archivo por su nombre
    def read(self,name):
        index = self.get_index_dir(name)
        if index != []:
            index = index[0]
            input_dir = self.inputs_dir[index]
            inic_cluster = input_dir['inic_cluster']
            size_file =  input_dir['size_file']
            return self.map[self.size_of_cluster_FS*inic_cluster:self.size_of_cluster_FS*inic_cluster+size_file]
        return False

    ### Escribe un nuevo archivo y escribe su entrada en el directorio
    def write(self,name,data,create_date):
        if name not in self.get_index_dir(name,'name_dir'):
            index = self.get_index_dir(self.void_entrada_dir)
            if index != []:
                index = index[0]
                input_dir = self.inputs_dir[index]
                size_file =  len(data)
                inputs_dir = list(filter(lambda x: x['name_dir'] not in self.void_entrada_dir,self.inputs_dir))
                inputs_dir = sorted(inputs_dir, key = lambda x:x['inic_cluster'],reverse=True)
                if inputs_dir != []:
                    inic_cluster = self.get_cluster_final(inputs_dir[0]) + 1
                else:
                    inic_cluster = 5
                input_dir = dict(inic_cluster=inic_cluster,size_file=size_file)
                cluster_final = self.get_cluster_final(input_dir)
            if (cluster_final < 1440):
                self.set_data(inic_cluster,size_file,data)
                self.inputs_dir[index]['name_dir'] = name
                self.inputs_dir[index]['inic_cluster'] = inic_cluster
                self.inputs_dir[index]['size_file'] = size_file
                self.inputs_dir[index]['fm'] = self.time_to_formatFS(time.time())
                self.inputs_dir[index]['fc'] = self.time_to_formatFS(create_date)
                self.write_index_dir()
                return True
            else:
                print("Ya no hay espacio para meter este archivo")
        else:
            print("Un archivo con el mismo nombre ya existe")
        return False
    
    # Convierte una ruta absoluta y obtiene el nombre del archivo
    def parse_ruta_a_nombre_archivo(self,path):
        path = path.split("/")
        return path[len(path)-1]

    #copia del FS a un FS externo
    def copiar_FS_a_eXFS(self,source,dest):
        data = self.read(source)
        # valida que el destino no sea un directorio
        # Es obligatorio asignar un nombre al archivo que sera copiado al sistema externo
        if not os.path.isdir(dest):
            with open(dest,"wb+") as f:
                f.write(data)
                return True
        return False
    
    
    #copia del FS externo al FS
    def copiar_eXFS_a_FS(self,source):
        if os.path.isfile(source):
            with open(source,"r+") as f:
                fs = mmap.mmap(f.fileno(),0)
                name = self.parse_ruta_a_nombre_archivo(source)
                data = fs.read()
                create_date = os.path.getctime(source)
                return self.write(name,data,create_date)
        print("No es un archivo valido")
        return False
    
    # Desfragmenta el FS 
    def desfragmentar(self):
        self.inputs_dir
        indexes = self.get_index_not_dir(self.void_entrada_dir)
        cluster_nuevo = 5
        for index in indexes:
            cluster_inicial = self.inputs_dir[index]['inic_cluster']
            size_bits = self.inputs_dir[index]['size_file']
            data = self.get_data(cluster_inicial,size_bits)
            cluster_final = self.get_cluster_final(self.inputs_dir[index])
            tam_clusters = len(self.get_list_range(cluster_inicial,cluster_final))
            cluster_inicial = cluster_nuevo
            self.set_data(cluster_inicial,size_bits,data)
            self.inputs_dir[index]['inic_cluster'] = cluster_inicial
            cluster_nuevo = cluster_inicial + tam_clusters
        self.write_index_dir()

    # Obtiene los datos binarios de una entrada en el FS
    def get_data(self,cluster_inicial,size_bits):
        return self.map[self.size_of_cluster_FS*cluster_inicial:self.size_of_cluster_FS*cluster_inicial+size_bits]
    
    # Escribe los datos a una entra den el FS
    def set_data(self,cluster_inicial,size_bits,data):
        try:
            self.map[self.size_of_cluster_FS*cluster_inicial:self.size_of_cluster_FS*cluster_inicial+size_bits] = data
            return True
        except Exception as e:
            print(e)
            return False
    
    # Obtiene el cluster final de una entrada en el directorio
    def get_cluster_final(self,input_dir):
        tam = ceil(input_dir['size_file']/1024) + 1
        return input_dir['inic_cluster'] + tam

    # Obtiene una lista de numeros por medio de un numero inicial y final
    # Este metodo es usado para "mapear" numero de clusters
    def get_list_range(self,init,end):
        lista = []
        for i in range(init,end+1):
            lista.append(i)
        return lista
    # Convierte un timestamp a una cadena con el formato del FS
    def time_to_formatFS(self,time):
        date_time = datetime.datetime.fromtimestamp(time)
        return date_time.strftime("%Y%m%d%H%M%S")

    # Elimina una entrada del indice de directorios dejandola libre
    # No elimina datos pero al no estar mapeados en el indice se consideran basura
    def delete(self,name):
        index = self.get_index_dir(name)
        if index != []:
            index = index[0]
            input_dir = self.inputs_dir[index]
            inic_cluster = input_dir['inic_cluster']
            size_file =  input_dir['size_file']
            self.inputs_dir[index]['name_dir'] = "AQUI_NO_VA_NADA"
            self.inputs_dir[index]['size_file'] = "0"
            self.inputs_dir[index]['inic_cluster'] = "0"
            self.inputs_dir[index]['fc'] = "0"
            self.inputs_dir[index]['fm'] = "0"
            return self.write_index_dir()
        return False