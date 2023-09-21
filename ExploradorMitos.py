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
        (TipoComp.OPEMATE, r'^(\+|\-|\/|\*|raizQ)$'),
        (TipoComp.TIPO,r'^(fenix|unicornio|ponto|supay)'),
        (TipoComp.CONSTANTE, r'^(!)'),
        (TipoComp.VARIABLE,r'^(#)'),
        (TipoComp.BOOLEANO,r'^(true|false)'),
        (TipoComp.ENTERO, r'^[0123456789]+'),
        (TipoComp.FLOTANTE, r'^(-?[0-9]+\.[0-9]+)'),
        (TipoComp.TEXTO,r'^([a-zA-Z0-9_-]*)'),
        (TipoComp.GLOBAL,r'^(global)')
    ]

    def __init__(self, pArchivo):
        self.texto = pArchivo
        self.componentes = []

    def explorar(self):
        # itera sobre cada línea del archivo y genera los componentes lexicos

        for num, linea in enumerate(self.texto, 1):
            resultado = self.procesarLinea(linea, num)
            #  es para evitar que se agregue None a la lista de componentes por comentario que no retorna nada
            if resultado != None:
                self.componentes = self.componentes + resultado
    
    def procesarLinea(self, linea: str, numLinea: int):
        componentes = []
        # termina cuando la linea esta vacia o es un salto de linea o es un comentario de linea 
        while(linea != "" or linea != "\n"):
            linea = linea.strip()
            if (re.match(self.descriptores[0][1], linea)) != None:
                componente = re.match(self.descriptores[0][1], linea)
                nuevoComponente = ComponenteLexico(self.descriptores[0][0], componente.group(), numLinea)
                componentes.append(nuevoComponente)
                linea = linea[componente.end():]
                
            elif (re.match(self.descriptores[1][1], linea)) != None:
                componente = re.match(self.descriptores[1][1], linea)
                nuevoComponente = ComponenteLexico(self.descriptores[1][0], componente.group(), numLinea)
                componentes.append(nuevoComponente)
                linea = linea[componente.end():]
                
            elif (re.match(self.descriptores[2][1], linea)) != None:
                componente = re.match(self.descriptores[2][1], linea)
                nuevoComponente = ComponenteLexico(self.descriptores[2][0], componente.group(), numLinea)
                componentes.append(nuevoComponente)
                linea = linea[componente.end():]
                
            elif (re.match(self.descriptores[3][1], linea)) != None:
                componente = re.match(self.descriptores[3][1], linea)
                nuevoComponente = ComponenteLexico(self.descriptores[3][0], componente.group(), numLinea)
                componentes.append(nuevoComponente)
                linea = linea[componente.end():]
            
            elif (re.match(self.descriptores[4][1], linea)) != None:
                break
                
            elif (re.match(self.descriptores[5][1], linea)) != None:
                componente = re.match(self.descriptores[5][1], linea)
                nuevoComponente = ComponenteLexico(self.descriptores[5][0], componente.group(), numLinea)
                componentes.append(nuevoComponente)
                linea = linea[componente.end():]
                

            elif (re.match(self.descriptores[6][1], linea)) != None:
                componente = re.match(self.descriptores[6][1], linea)
                nuevoComponente = ComponenteLexico(self.descriptores[6][0], componente.group(), numLinea)
                componentes.append(nuevoComponente)
                linea = linea[componente.end():]
                
            elif (re.match(self.descriptores[7][1], linea)) != None:
                componente = re.match(self.descriptores[7][1], linea)
                nuevoComponente = ComponenteLexico(self.descriptores[7][0], componente.group(), numLinea)
                componentes.append(nuevoComponente)
                linea = linea[componente.end():]
                
            elif (re.match(self.descriptores[8][1], linea)) != None:
                componente = re.match(self.descriptores[8][1], linea)
                nuevoComponente = ComponenteLexico(self.descriptores[8][0], componente.group(), numLinea)
                componentes.append(nuevoComponente)
                linea = linea[componente.end():]
                
            elif (re.match(self.descriptores[9][1], linea)) != None:
                componente = re.match(self.descriptores[9][1], linea)
                nuevoComponente = ComponenteLexico(self.descriptores[9][0], componente.group(), numLinea)
                componentes.append(nuevoComponente)
                linea = linea[componente.end():]
                
            elif (re.match(self.descriptores[10][1], linea)) != None:
                componente = re.match(self.descriptores[10][1], linea)
                nuevoComponente = ComponenteLexico(self.descriptores[10][0], componente.group(), numLinea)
                componentes.append(nuevoComponente)
                linea = linea[componente.end():]
                
            elif (re.match(self.descriptores[11][1], linea)) != None:
                componente = re.match(self.descriptores[11][1], linea)
                nuevoComponente = ComponenteLexico(self.descriptores[11][0], componente.group(), numLinea)
                componentes.append(nuevoComponente)
                linea = linea[componente.end():]
                
            elif (re.match(self.descriptores[12][1], linea)) != None:
                componente = re.match(self.descriptores[12][1], linea)
                nuevoComponente = ComponenteLexico(self.descriptores[12][0], componente.group(), numLinea)
                componentes.append(nuevoComponente)
                linea = linea[componente.end():]
                
            elif (re.match(self.descriptores[13][1], linea)) != None:
                componente = re.match(self.descriptores[13][1], linea)
                nuevoComponente = ComponenteLexico(self.descriptores[13][0], componente.group(), numLinea)
                componentes.append(nuevoComponente)
                linea = linea[componente.end():]
                
            elif (re.match(self.descriptores[14][1], linea)) != None:
                componente = re.match(self.descriptores[14][1], linea)
                nuevoComponente = ComponenteLexico(self.descriptores[14][0], componente.group(), numLinea)
                componentes.append(nuevoComponente)
                linea = linea[componente.end():]
                
            elif (re.match(self.descriptores[15][1], linea)) != None:
                componente = re.match(self.descriptores[15][1], linea)
                nuevoComponente = ComponenteLexico(self.descriptores[15][0], componente.group(), numLinea)
                componentes.append(nuevoComponente)
                linea = linea[componente.end():]
                
            elif (re.match(self.descriptores[16][1], linea)) != None:
                componente = re.match(self.descriptores[16][1], linea)
                nuevoComponente = ComponenteLexico(self.descriptores[16][0], componente.group(), numLinea)
                componentes.append(nuevoComponente)
                linea = linea[componente.end():]
            else:
                break

text = """-- imprimir n cantidad de dígitos de la serie de fibonacci
ra cant_fibonacci(fenix #n){
    fenix #actual = 0;
    fenix #siguiente = 1;
    fenix #contador = 0;
    fenix #auxiliar = 0;
    ciclope (contador < n){
        sirena(actual);
        auxiliar= siguiente;
        siguiente = actual + siguiente;
        actual = auxiliar;
        contador += 1;
    };
    hades true;
};"""

lines = text.split('\n')
# print(lines)

# expo = Explorador(["ra cant_fibonacci(fenix #n){"])
expo = Explorador(lines)
expo.explorar()