import os
import sys
from errno import ENOENT
import mmap
from fuse import FuseOSError, Operations,  LoggingMixIn
from datetime import datetime
from time import time, mktime
from stat import S_IFDIR, S_IFLNK, S_IFREG

class FiUnamFS(LoggingMixIn,Operations):
    def __init__(self, root):
        self.root = root
        self.void_entrada_dir = "AQUI_NO_VA_NADA"
        if os.path.isfile(self.root):
            with open(self.root,"r+") as f:
                self.map = mmap.mmap(f.fileno(),0)
                self.nombre_FS = self.map[0:8].decode('ascii')
                self.version_FS = self.map[10:13].decode('ascii')
                self.etiqueta_vol = self.map[20:35].decode('ascii')
                self.size_of_cluster_FS = int(self.map[40:45].decode('ascii'))
                self.num_of_cluster_dir_FS = int(self.map[47:49].decode('ascii'))
                self.num_of_cluster_total_FS = int(self.map[52:60].decode('ascii'))
                self.files = {}
                now = time()
                self.files['/'] = dict(st_mode=(S_IFDIR | 0o755), st_ctime=now,
                                    st_mtime=now, st_atime=now, st_nlink=2)
                dir_cluster_offset=1024
                size_input_dir = 64
                num_input_dir = int(self.size_of_cluster_FS/size_input_dir * self.num_of_cluster_dir_FS)
                for i in range(num_input_dir):
                    name_file = self.map[dir_cluster_offset+(size_input_dir*i):dir_cluster_offset+(size_input_dir*i)+15].decode('ascii').replace(" ","")
                    if(name_file != 'AQUI_NO_VA_NADA'):
                        tamano_archivo = int(self.map[dir_cluster_offset+(size_input_dir*i)+16:dir_cluster_offset+(size_input_dir*i)+24].decode('ascii'))
                        fecha_creacion = self.map[dir_cluster_offset+(size_input_dir*i)+31:dir_cluster_offset+(size_input_dir*i)+45].decode('ascii')
                        fc = datetime.strptime(fecha_creacion,"%Y%m%d%H%M%S")
                        fc = mktime(fc.timetuple())
                        fecha_modificacion = self.map[dir_cluster_offset+(size_input_dir*i)+46:dir_cluster_offset+(size_input_dir*i)+60].decode('ascii')
                        fm = datetime.strptime(fecha_modificacion,"%Y%m%d%H%M%S")
                        fm = mktime(fm.timetuple())
                        self.files["/"+name_file] = dict(st_nlink=2,
                                st_size=tamano_archivo, st_ctime=fc, st_mtime=fm)
                self.inputs_dir = []
                self.descriptor_archivo = 0
                if self.nombre_FS != 'FiUnamFS':
                    print("el sistema de archivos no es valido")
                    exit()
        else:
            exit()
    
    def buscar_elemento(self,key, value, lista):
        return any(d[key] == value for d in lista)

    def get_index_list_dict(self,key,value,lista):
        return lista.index(filter(lambda n: n.get(key) == value, lista)[0])
    # Obtiene la ruta completa del sistema que va a ser montado
    def _full_path(self, partial):
        if partial.startswith("/"):
            partial = partial[1:]
        path = os.path.join(self.root, partial)
        return path

    # Lee el contenido del directorio
    def readdir(self, path, fh):
        return ['.', '..'] + [x[1:] for x in self.files if x != '/']

    def open(self, path, flags):
        full_path = self._full_path(path)
        print("abrio")
        return os.open(full_path, flags)
    
    def getattr(self,path,fh=None):
        if path not in self.files:
            raise FuseOSError(ENOENT)
        return self.files[path]


    def create(self, path, mode, fi=None):
        self.files[path] = dict(st_mode=(S_IFREG | mode), st_nlink=1,
                                st_size=0, st_ctime=time(), st_mtime=time(),
                                st_atime=time())
        self.descriptor_archivo += 1
        return self.descriptor_archivo

    def read(self, path, length, offset, fh):
        print("leyo")
        os.lseek(fh, offset, os.SEEK_SET)
        return os.read(fh, length)

    def write(self, path, buf, offset, fh):
        print("escribe")
        self.da
        os.lseek(fh, offset, os.SEEK_SET)
        return os.write(fh, buf)

        