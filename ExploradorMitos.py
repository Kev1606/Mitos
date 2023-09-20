#Explorador del lenguaje Mitos

#crear enumerables
from enum import Enum, auto
#expresiones regulares
import re

class TipoComp(Enum):
    # enumerable con los tipos de componentes léxicos que existen en Mitos

    FUNCION = auto()
    MASTER =  auto()
    PUNTUACION = auto()
    PARENTESIS = auto()

    COMENTARIO = auto()
    CONDICIONAL = auto()
    REPETICION = auto()
    COMPARADOR = auto()
    OPEMATE = auto()

    TIPO = auto()
    CONSTANTE = auto()
    VARIABLE = auto()
    BOOLEANO = auto()
    ENTERO = auto()
    FLOTANTE = auto()
    TEXTO = auto()


class ComponenteLexico:

    tipo: TipoComp
    texto: str

    def __init__(self, pTipo: TipoComp, pTexto: str):
        self.tipo = pTipo
        self.texto = pTexto

    def aTexto(self):
        formatoSTR = f'{self.tipo:20} <{self.texto}>'
        return formatoSTR