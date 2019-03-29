import argparse

#Código para pedir los datos desde consola
parser = argparse.ArgumentParser(description='Ayuda para el usuario')
parser.add_argument('-t','--turistas', default=20,type=int, help='Define el numero de turistas')
parser.add_argument('-g','--guias', default=5, type=int,help='Define el numero de guias')
args= parser.parse_args()
