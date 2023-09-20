#Explorador del lenguaje Mitos

#crear enumerables
from enum import Enum, auto
#expresiones regulares
import re

class TipoComp(Enum):
    # enumerable con los tipos de componentes léxicos que existen en Mitos

    MASTER =  auto()
    FUNCION = auto()
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
    GLOBAL = auto()


class ComponenteLexico:
    # clase que identifica los diferentes componentes léxicos
    tipo: TipoComp
    texto: str
    linea: int

    def __init__(self, pTipo: TipoComp, pTexto: str, pLinea: int):
        self.tipo = pTipo
        self.texto = pTexto
        self.linea = pLinea

    def aTexto(self):
        formatoSTR = f'{self.tipo:20} <{self.texto}> "en la linea" {self.linea}'
        return formatoSTR


class Explorador:
    # clase que procesa el codigo y genera los componentes lexicos
    texto: str
    componentes = []

    descriptores = [
        (TipoComp.MASTER, r'^zeus'),
        (TipoComp.FUNCION, r'^ra'),
        (TipoComp.PUNTUACION, r'^:'),
        (TipoComp.PARENTESIS, r'^(){}'),
        (TipoComp.COMENTARIO, r'^--'),
        (TipoComp.CONDICIONAL, r'^(temis|atenea)'),
        (TipoComp.REPETICION, r'^ciclope'),
        (TipoComp.COMPARADOR,r'^(==|!=|<|>|<=|>=)'),
        (TipoComp.OPEMATE,r'^(+|-|/|*|raizQ)'),
        (TipoComp.TIPO,r'^(fenix|unicornio|ponto|supay)'),
        (TipoComp.CONSTANTE, r'^(!)'),
        (TipoComp.VARIABLE,r'^(#)'),
        (TipoComp.BOOLEANO,r'^(true|false)'),
        (TipoComp.ENTERO, r'^[0123456789]*'),
        (TipoComp.ENTERO, r'^[0123456789]*.[0123456789]*'),
        (TipoComp.TEXTO,r'^([a-z]*[A-Z]*[0-9]*)~'),
        (TipoComp.GLOBAL,r'^(global)')
    ]

    def __init__(self, pArchivo):
        self.texto = pArchivo
        self.componentes = []

    def explorar(self):
        # itera sobre cada línea del archivo y genera los componentes lexicos

        for linea in self.texto:
            resultado = self.procesarLinea(linea)
            self.componentes = self.componentes + resultado
    
    def procesarLinea(self, linea: str):
        print("yo no quiero hacer esto")
    
    #def imprimirComponentes(self):
        #imprime los componentes lexicos
        
       #for componente in self.componentes:
            #print(componente)