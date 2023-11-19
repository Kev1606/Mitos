from enum import Enum, auto

class TipoDatos(Enum):
    TEXTO = auto()
    NUMERO = auto()
    ENTERO = auto()
    FLOTANTE = auto()
    BOOLEANO = auto()
    CUALQUIERA = auto()
    COMPARADOR = auto()
    NINGUNO = auto()