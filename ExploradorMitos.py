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
        (TipoComp.MASTER, r'^(zeus)'),
        (TipoComp.FUNCION, r'^(ra)'),
        (TipoComp.PUNTUACION, r'^:'),
        (TipoComp.PARENTESIS, r'^([(){}])'),
        (TipoComp.COMENTARIO, r'^--'),
        (TipoComp.CONDICIONAL, r'^(temis|atenea)'),
        (TipoComp.REPETICION, r'^(ciclope)'),
        (TipoComp.COMPARADOR,r'^(==|!=|<|>|<=|>=)'),
        (TipoComp.OPEMATE,r'^(+|-|/|*|raizQ)'),
        (TipoComp.TIPO,r'^(fenix|unicornio|ponto|supay)'),
        (TipoComp.CONSTANTE, r'^(!)'),
        (TipoComp.VARIABLE,r'^(#)'),
        (TipoComp.BOOLEANO,r'^(true|false)'),
        (TipoComp.ENTERO, r'^[0123456789]*'),
        (TipoComp.FLOTANTE, r'^(-?[0-9]+\.[0-9]+)'),
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
        componentes = []
        while(linea != ""):

            if (re.match(self.descriptores[0][1])) != None:
                componente = re.match(self.descriptores[0][1])
                nuevoComponente = ComponenteLexico(self.descriptores[0][0], componente.group())
                componentes.append(componente)
                linea = linea[componente.end():]
                break;
            elif (re.match(self.descriptores[1][1])) != None:
                componente = re.match(self.descriptores[1][1])
                nuevoComponente = ComponenteLexico(self.descriptores[1][0], componente.group())
                componentes.append(componente)
                linea = linea[componente.end():]
                break;
            elif (re.match(self.descriptores[2][1])) != None:
                componente = re.match(self.descriptores[2][1])
                nuevoComponente = ComponenteLexico(self.descriptores[2][0], componente.group())
                componentes.append(componente)
                linea = linea[componente.end():]
                break;
            elif (re.match(self.descriptores[3][1])) != None:
                componente = re.match(self.descriptores[3][1])
                nuevoComponente = ComponenteLexico(self.descriptores[3][0], componente.group())
                componentes.append(componente)
                linea = linea[componente.end():]
                break;
            elif (re.match(self.descriptores[5][1])) != None:
                componente = re.match(self.descriptores[5][1])
                nuevoComponente = ComponenteLexico(self.descriptores[5][0], componente.group())
                componentes.append(componente)
                linea = linea[componente.end():]
                break;
            elif (re.match(self.descriptores[6][1])) != None:
                componente = re.match(self.descriptores[6][1])
                nuevoComponente = ComponenteLexico(self.descriptores[6][0], componente.group())
                componentes.append(componente)
                linea = linea[componente.end():]
                break;
            elif (re.match(self.descriptores[7][1])) != None:
                componente = re.match(self.descriptores[7][1])
                nuevoComponente = ComponenteLexico(self.descriptores[7][0], componente.group())
                componentes.append(componente)
                linea = linea[componente.end():]
                break;
            elif (re.match(self.descriptores[8][1])) != None:
                componente = re.match(self.descriptores[8][1])
                nuevoComponente = ComponenteLexico(self.descriptores[8][0], componente.group())
                componentes.append(componente)
                linea = linea[componente.end():]
                break;
            elif (re.match(self.descriptores[9][1])) != None:
                componente = re.match(self.descriptores[9][1])
                nuevoComponente = ComponenteLexico(self.descriptores[9][0], componente.group())
                componentes.append(componente)
                linea = linea[componente.end():]
                break;
            elif (re.match(self.descriptores[10][1])) != None:
                componente = re.match(self.descriptores[10][1])
                nuevoComponente = ComponenteLexico(self.descriptores[10][0], componente.group())
                componentes.append(componente)
                linea = linea[componente.end():]
                break;
            elif (re.match(self.descriptores[11][1])) != None:
                componente = re.match(self.descriptores[11][1])
                nuevoComponente = ComponenteLexico(self.descriptores[11][0], componente.group())
                componentes.append(componente)
                linea = linea[componente.end():]
                break;
            elif (re.match(self.descriptores[12][1])) != None:
                componente = re.match(self.descriptores[12][1])
                nuevoComponente = ComponenteLexico(self.descriptores[12][0], componente.group())
                componentes.append(componente)
                linea = linea[componente.end():]
                break;
            elif (re.match(self.descriptores[13][1])) != None:
                componente = re.match(self.descriptores[13][1])
                nuevoComponente = ComponenteLexico(self.descriptores[13][0], componente.group())
                componentes.append(componente)
                linea = linea[componente.end():]
                break;
            elif (re.match(self.descriptores[14][1])) != None:
                componente = re.match(self.descriptores[14][1])
                nuevoComponente = ComponenteLexico(self.descriptores[14][0], componente.group())
                componentes.append(componente)
                linea = linea[componente.end():]
                break;
            elif (re.match(self.descriptores[15][1])) != None:
                componente = re.match(self.descriptores[15][1])
                nuevoComponente = ComponenteLexico(self.descriptores[15][0], componente.group())
                componentes.append(componente)
                linea = linea[componente.end():]
                break;
            elif (re.match(self.descriptores[16][1])) != None:
                componente = re.match(self.descriptores[16][1])
                nuevoComponente = ComponenteLexico(self.descriptores[16][0], componente.group())
                componentes.append(componente)
                linea = linea[componente.end():]
                break;
            else:
                # MANEJAR EL ERROR AQUI
