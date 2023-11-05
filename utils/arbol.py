# ASA

from enum import Enum, auto

class TipoNodo(Enum):
    
    MASTER                = auto() #
    ASIGNACIÓN            = auto() #
    EXPRESIÓN_MATEMÁTICA  = auto() #
    EXPRESIÓN             = auto() #
    FUNCIÓN               = auto() #
    INVOCACIÓN            = auto() #
    PARAMETROS_FUNCION    = auto() ##
    PARÁMETROS_INVOCACIÓN = auto() #
    INSTRUCCIONES         = auto() #
    REPETICIÓN            = auto() 
    BIFURCACION           = auto() #
    TEMIS                 = auto() #
    SINO                  = auto()
    OPERADOR_LÓGICO       = auto()
    CONDICIÓN             = auto()
    COMPARACIÓN           = auto()
    RETORNO               = auto()
    ERROR                 = auto()
    PRINCIPAL             = auto()
    BLOQUE_INSTRUCCIONES  = auto() #
    OPEMATE               = auto() #
    COMPARADOR            = auto()
    VARIABLE              = auto() #
    BOOLEANO              = auto() #
    TEXTO                 = auto() #
    ENTERO                = auto() #
    FLOTANTE              = auto() #
    IDENTIFICADOR         = auto() #
    TIPO                  = auto()
    STRING                = auto()

import copy

class NodoÁrbol:

    tipo      : TipoNodo
    contenido : str
    atributos : dict

    def __init__(self, tipo, contenido = None, nodos = [], atributos = {}):

        self.tipo      = tipo
        self.contenido = contenido
        self.nodos     = nodos
        self.atributos = copy.deepcopy(atributos)

    def visitar(self, visitador):
        return visitador.visitar(self)


    def __str__(self):

        # Coloca la información del nodo
        resultado = '{:30}\t'.format(self.tipo)
        
        if self.contenido is not None:
            resultado += '{:10}\t'.format(self.contenido)
        else:
            resultado += '{:10}\t'.format('')


        if self.atributos != {}:
            resultado += '{:38}'.format(str(self.atributos))
        else:
            resultado += '{:38}\t'.format('')

        if self.nodos != []:
            resultado += '<'

            # Imprime los tipos de los nodos del nivel siguiente
            for nodo in self.nodos[:-1]:
                if nodo is not None:
                    resultado += '{},'.format(nodo.tipo)

            resultado += '{}'.format(self.nodos[-1].tipo)
            resultado += '>'

        return resultado


class ÁrbolSintáxisAbstracta:

    raiz : NodoÁrbol

    def imprimir_preorden(self):
        self.__preorden(self.raiz)

    def __preorden(self, nodo: NodoÁrbol):

        print(nodo)

        if nodo is not None:
            for nodop in nodo.nodos:
                self.__preorden(nodop)