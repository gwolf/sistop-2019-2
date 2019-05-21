import mmap
import os
from core.Menu import Menu
from datetime import datetime
from math import ceil

class FiUnamFS(Menu):

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
                fs[1024+(64*i):1024+(64*i)+15] = "AQUI_NO_VA_NADA".encode('ascii')
                fs[1024+(64*i)+16:1024+(64*i)+24] = ("0"*(24-16)).encode('ascii')
                fs[1024+(64*i)+25:1024+(64*i)+30] = ("0"*(30-25)).encode('ascii')
                fs[1024+(64*i)+31:1024+(64*i)+45] = ("0"*(45-31)).encode('ascii')
                fs[1024+(64*i)+46:1024+(64*i)+60] = ("0"*(60-46)).encode('ascii')
                fs[1024+(64*i)+61:1024+(64*i)+64] = ("0"*(64-61)).encode('ascii')
            fs[1024*5:] = str("\x00"*(1024*1435)).encode('ascii')
            f.close()

    def parse_dir(self):
        for input_dir in range(self.num_input_dir):
            name_dir = self.map[1024+(64*input_dir):1024+(64*input_dir)+15].decode('ascii').replace(" ","")
            tam_archivo = int(self.map[1024+(64*input_dir)+16:1024+(64*input_dir)+24])
            cluster_inicial = int(self.map[1024+(64*input_dir)+25:1024+(64*input_dir)+30])
            fecha_creacion = int(self.map[1024+(64*input_dir)+31:1024+(64*input_dir)+45])
            fecha_modificacion = int(self.map[1024+(64*input_dir)+46:1024+(64*input_dir)+60])
            self.inputs_dir.append(dict(id=input_dir,name_dir=name_dir,size_file=tam_archivo,inic_cluster=cluster_inicial,
                                        fc = fecha_creacion, fm = fecha_modificacion))

    def __init__(self, root):
        super(FiUnamFS, self).__init__()
        self.root = root
        self.void_entrada_dir = "AQUI_NO_VA_NADA"
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

    def get_index_dir(self,name):
        try:
            lista = []
            for elem in self.inputs_dir:
                if elem['name_dir'] == name:
                    lista.append(elem['id'])
            return lista
        except:
            return -1
    
    def get_index_not_dir(self,name):
        try:
            lista = []
            for elem in self.inputs_dir:
                if elem['name_dir'] != name:
                    lista.append(elem['id'])
            return lista
        except:
            return -1
    
    def write_index_dir(self):
        dir_cluster_offset=1024
        size_input_dir = 64
        for input_dir in self.inputs_dir:
            i = int(input_dir['id'])
            self.map[dir_cluster_offset+(size_input_dir*i):dir_cluster_offset+(size_input_dir*i)+15] = (" "*(15-len(input_dir['name_dir']))+input_dir['name_dir']).encode('ascii')
            self.map[dir_cluster_offset+(size_input_dir*i)+16:dir_cluster_offset+(size_input_dir*i)+24] = ("0"*(8-len(str(input_dir['size_file'])))+str(input_dir['size_file'])).encode('ascii')
            self.map[dir_cluster_offset+(size_input_dir*i)+25:dir_cluster_offset+(size_input_dir*i)+30] = ("0"*(5-len(str(input_dir['inic_cluster'])))+str(input_dir['inic_cluster'])).encode('ascii')
            self.map[dir_cluster_offset+(size_input_dir*i)+31:dir_cluster_offset+(size_input_dir*i)+45] = ("0"*(14 - len(str(input_dir['fc'])))+str(input_dir['fc'])).encode('ascii')
            self.map[dir_cluster_offset+(size_input_dir*i)+46:dir_cluster_offset+(size_input_dir*i)+60] = ("0"*(14- len(str(input_dir['fm'])))+str(input_dir['fm'])).encode('ascii')
        return True
    
     # Lista el contenido del FS
    def listar_contenido(self):
        for input_dir in self.inputs_dir:
            if input_dir["name_dir"] != self.void_entrada_dir:
                print(input_dir["name_dir"])
    
    # regresa los datos del archivo por su nombre
    def read(self,name):
        index = self.get_index_dir(name)
        print("=====")
        print(index)
        print("=====")
        if index != []:
            index = index[0]
            input_dir = self.inputs_dir[index]
            inic_cluster = input_dir['inic_cluster']
            size_file =  input_dir['size_file']
            return self.map[self.size_of_cluster_FS*inic_cluster:self.size_of_cluster_FS*inic_cluster+size_file]
        return False
    
    def get_clusters_ocupados(self):
        ocupados = []
        inputs = self.get_index_not_dir(self.void_entrada_dir)
        if inputs != -1:
            for input_dir in inputs:
                cluster_inicial = self.inputs_dir[input_dir]['inic_cluster']
                tam_cluster = ceil(self.inputs_dir[input_dir]['size_file'] / 1024) + 1
                for cluster in range(cluster_inicial,tam_cluster):
                    ocupados.append(cluster)
            return ocupados
        return []
    
    def get_clusters_usados(self,inic,size):
        usados = []
        tam = ceil(size/1024) + 1
        print(inic)
        print("----")
        print(tam+inic)
        for cluster in range(inic,tam+inic):
            print(cluster)
            usados.append(cluster)
        return usados


    # Escribe un nuevo archivo
    def write(self,name,data):
        index = self.get_index_dir(self.void_entrada_dir)
        if index != -1:
            index = index[0]
            input_dir = self.inputs_dir[index]
            inic_cluster = 0
            size_file =  len(data)
            cluster_ocupados = self.get_clusters_ocupados()
            seccion_valida = False
            for i in range(5,1440):
                if i not in cluster_ocupados:
                    clusters_usados = self.get_clusters_usados(i,size_file)
                    print(clusters_usados)
                    for cluster_usado in clusters_usados:
                        seccion_valida = True
                        if cluster_usado in cluster_ocupados:
                            seccion_valida = False
                            break
                    if seccion_valida == True:
                        inic_cluster = i
                        break
            print(str(self.size_of_cluster_FS*inic_cluster)+":"+str(self.size_of_cluster_FS*inic_cluster+size_file))
            self.map[self.size_of_cluster_FS*inic_cluster:self.size_of_cluster_FS*inic_cluster+size_file] = data
            self.inputs_dir[index]['name_dir'] = name
            self.inputs_dir[index]['inic_cluster'] = inic_cluster
            self.inputs_dir[index]['size_file'] = size_file
            return self.write_index_dir()
        return False
    
    def parse_ruta_a_nombre_archivo(self,path):
        path = path.split("/")
        print(path)
        return path[len(path)-1]

    #copia del FS a un FS externo
    def copiar_FS_a_eXFS(self,source,dest):
        data = self.read(source)
        with open(dest,"wb+") as f:
            f.write(data)
    
    
    #copia del FS externo al FS
    def copiar_eXFS_a_FS(self,source):
        with open(source,"r+") as f:
            fs = mmap.mmap(f.fileno(),0)
            name = self.parse_ruta_a_nombre_archivo(source)
            data = fs.read()
            return self.write(name,data)

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