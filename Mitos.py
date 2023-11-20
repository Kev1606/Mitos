# # Archivo principal para el explorador

from cargarArchivo import cargarArchivo as utils
from ExploradorMitos import Explorador
from analizador.analizadorMitos import Analizador
from Verificador.verificadorMitos import Verificador
# from Generador.generadorMitos import Generador
import argparse

parser = argparse.ArgumentParser(description='Intérprete para Mitos')

parser.add_argument('--solo-explorar', dest='explorador', action='store_true',
                    help='Solo ejecutar el explorador y retorna lista de componentes lexicos')

parser.add_argument('--solo-analizar', dest='analizador', action='store_true',
                    help='Solo ejecutar el analizador y retorna un preorden del arbol sintactico')

parser.add_argument('--solo-verificar', dest='verificador', action='store_true',
                    help='Solo ejecutar el verificador y retorna un preorden del arbol sintactico y  y estructuras de apoyo generadas en la verificación')

parser.add_argument('--generar-python', dest='python', action='store_true', 
                    help='Genera código python')

parser.add_argument('archivo', help='Archivo de código fuente')

def mitos():
    args = parser.parse_args()
    if args.explorador is True:
        texto = utils.leer_archivo(args.archivo)

        exp = Explorador(texto)
        exp.explorar()
        exp.imprimir_componentes()
    elif args.analizador is True:
        texto = utils.leer_archivo(args.archivo)

        exp = Explorador(texto)
        exp.explorar()

        analizador = Analizador(exp.componentes)
        analizador.analizar()
        analizador.imprimirArbol()
    elif args.verificador is True:
        texto = utils.leer_archivo(args.archivo)

        exp = Explorador(texto)
        exp.explorar()

        analizador = Analizador(exp.componentes)
        analizador.analizar()

        verificador = Verificador(analizador.getASA())
        verificador.verificar()
        verificador.imprimirArbol()
    elif args.python is True:
        texto = utils.leer_archivo(args.archivo)
        exp = Explorador(texto)
        exp.explorar()

        analizador = Analizador(exp.componentes)
        analizador.analizar()

        verificador = Verificador(analizador.getASA())
        verificador.verificar()

        # generador = Generador(verificador.getASA())
        # generador.generar()
    else:
        parser.print_help()


if __name__ == '__main__':
    mitos()