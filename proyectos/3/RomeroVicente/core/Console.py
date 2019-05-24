import argparse
#from fuse import FUSE
from core.FiUnamFS import FiUnamFS

class Console:
    def __init__(self):
        self.parser = parser = argparse.ArgumentParser()
        #self.parser.add_argument('-M','--mount-point',nargs='?',type=str, required=True, help='Define el archivo binario que contiene el sistema de archivos')
        self.parser.add_argument('-R','--root',nargs='?', type=str, required=True, help='Define el archivo que contiene o contendra el sistema de archivos')
        self.parser.add_argument('-N','--name-vol',nargs='?', type=str, help='Define la etiqueta del volumen')
        self.parser.add_argument('-C','--create', default=False,action="store_true", help='Define si se creara nuevo sistema de archivos')
        self.args = parser.parse_args()

    def iniciar_consola(self):
        if self.args.create:
            FiUnamFS.create_new_fs(self.args.root,self.args.name_vol)
        FS = FiUnamFS(self.args.root)
        FS.iniciar_menu()
        #FUSE(FiUnamFS(self.args.root),self.args.mount_point, nothreads=True, foreground=True)