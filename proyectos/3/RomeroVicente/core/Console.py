import argparse

class Console:
    def __init__(self):
        self.parser = parser = argparse.ArgumentParser()
        self.parser.add_argument('-M','--mount-point',nargs='?',type=str, required=True, help='Define el punto de montaje')
        self.parser.add_argument('-R','--root',nargs='?', type=str, required=True, help='Define la raiz del sistema de archivos')
        self.args = parser.parse_args()

    def iniciar_consola(self):
        print(self.args)