# Archivo principal para el compilador

from cargarArchivo import cargarArchivo as utils
from ExploradorMitos import Explorador 

import argparse

parser = argparse.ArgumentParser(description='Interprete para Ciruelas (el lenguaje)')

parser.add_argument('--solo-explorar', dest='explorador', action='store_true', 
        help='ejecuta solo el explorador y retorna una lista de componentes léxicos')

parser.add_argument('--generar-python', dest='python', action='store_true', 
        help='''Genera código python''')

parser.add_argument('archivo',
        help='Archivo de código fuente')

def ciruelas():

    args = parser.parse_args()

    if args.explorador is True: 

        texto = utils.cargar_archivo(args.archivo)

        exp = Explorador(texto)
        exp.explorar()
        exp.imprimir_componentes()

    elif args.python is True:

        texto = utils.cargar_archivo(args.archivo)

        exp = Explorador(texto)
        exp.explorar()
        
    else:
        parser.print_help()


if __name__ == '__main__':
    ciruelas()
