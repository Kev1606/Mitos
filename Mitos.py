# Archivo principal para el explorador

from cargarArchivo import cargarArchivo as func
from ExploradorMitos import Explorador 

import argparse

# Se crea un objeto ArgumentParser que se utiliza para definir como se deben procesar los 
# argumentos desde la linea de comandos
parser = argparse.ArgumentParser(description='Explorador para el lenguaje Mitos')

# En la siguiente linea, el comando '--solo-explorar' es un argumento el cual indica que solo
# se desea ejecutar el explorador, ademas se agrega el comando --help para brindar al usuario
# la informacion necesaria para la ejecucion del programa
parser.add_argument('--solo-explorar', dest='explorador', action='store_true', 
        help='ejecuta solo el explorador e imprime la lista de componentes léxicos')

# Proporciona la ruta del archivo como entrada 
parser.add_argument('archivo',
        help='Archivo de código fuente')

def mitos():

    args = parser.parse_args() # Procesa los comandos desde linea de comandos

    # En caso de que el usuario brinde como argumento --solo-explorar
    if args.explorador is True: 
        texto = func.leer_archivo(args.archivo) # Llama a la funcion cagar_archivo de la carpeta cargarArchivo
        exp = Explorador(texto)
        exp.explorar()
        exp.imprimir_componentes()
        
    else:
        parser.print_help()


if __name__ == '__main__':
    mitos()
