import argparse
from fuse import FUSE
from core.FiUnamFS import FiUnamFS
import logging

class Console:
    def __init__(self):
        self.parser = parser = argparse.ArgumentParser()
        self.parser.add_argument('-M','--mount-point',nargs='?',type=str, required=True, help='Define el directorio que va a ser montado')
        self.parser.add_argument('-R','--root',nargs='?', type=str, required=True, help='Define la raiz del sistema de archivos o el directorio donde sera montado')
        self.args = parser.parse_args()

    def iniciar_consola(self):
        logging.basicConfig(level=logging.DEBUG)
        FUSE(FiUnamFS(self.args.root),self.args.mount_point, nothreads=True, foreground=True)