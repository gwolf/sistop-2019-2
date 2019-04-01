from d_museum.guia import Guia
from d_museum.turista import Turista
from d_museum.argumentos import args

def abrir_museo(turistas):
    print("Bienvenidos al museo de Dijkstra")
    for m in range(0,turistas):
        t = Turista(m)
        t.start()


def main():
    abrir_museo(turistas=args.turistas)

if __name__ == '__main__':
    main()
