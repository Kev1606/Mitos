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
    ASIGNACION = auto()
    PARENTESIS = auto()
    RETORNO = auto()

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
    STRING = auto()


class ComponenteLexico:
    # clase que identifica los diferentes componentes léxicos
    tipo: TipoComp
    texto: str
    linea: int

    def __init__(self, pTipo: TipoComp, pTexto: str, pLinea: int):
        self.tipo = pTipo
        self.texto = pTexto
        self.linea = pLinea

    def __str__(self):
        return f'{self.tipo:20} <{self.texto}> "en la linea" {self.linea}'


class Explorador:
    # clase que procesa el codigo y genera los componentes lexicos
    texto: str
    componentes = []
    
    # (TipoComp.COMPARADOR,r'^(\=\=|\!\=|\<|\>|\<\=|\>\=)')
    descriptores = [
        (TipoComp.MASTER, r'^(zeus)'),
        (TipoComp.FUNCION, r'^(ra\s+)'),
        (TipoComp.PUNTUACION, r'^(\;|\,|\&|\|\|)'),
        (TipoComp.COMPARADOR,r'^(\=\=|\!\=|\<\=|\>\=|\<|\>)'),
        (TipoComp.PARENTESIS, r'^([ \( | \) | \{ | \} ])'),    
        (TipoComp.COMENTARIO, r'^(\-\-\s*)([a-zA-Z0-9_-]+)'),
        (TipoComp.CONDICIONAL, r'^(temis|atenea)'),
        (TipoComp.REPETICION, r'^(sisifo)'),
        (TipoComp.ASIGNACION, r'^='),
        (TipoComp.OPEMATE, r'^(\+|\-|\*{1,2}|\/{1,2}|\%)'),
        (TipoComp.TIPO,r'^(fenix|unicornio|ponto|supay)'),
        (TipoComp.CONSTANTE, r'^(!)'),
        (TipoComp.VARIABLE,r'^(#+)([a-zA-Z0-9_-]+)'),
        (TipoComp.BOOLEANO,r'^(Verdadero|Falso)'),
        (TipoComp.FLOTANTE, r'^(-?[0-9]+\.[0-9]+)'),
        (TipoComp.ENTERO, r'^[0-9]+'),
        (TipoComp.RETORNO,r'^(hades)'),
        (TipoComp.TEXTO,r'^([a-zA-Z0-9_]+)'),
        (TipoComp.GLOBAL,r'^(global)'),
        (TipoComp.STRING,r'^["\'](.+)*["\']')
    ]

    def __init__(self, pArchivo):
        self.texto = pArchivo
        self.componentes = []

    def explorar(self):
        # itera sobre cada línea del archivo y genera los componentes lexicos
        for num, linea in enumerate(self.texto, 1):
            resultado = self.procesarLinea(linea, num)
            
            if resultado == False:
                break
            
            #  es para evitar que se agregue None a la lista de componentes por comentario que no retorna nada
            if resultado != None:
                self.componentes = self.componentes + resultado

    def imprimir_componentes(self):
        for componente in self.componentes:
            print(componente)   # Esto funciona por que el print llama al
                                # método __str__ de la instancia 
    
    def getComponentes(self):
        return self.componentes
    
    def procesarLinea(self, linea: str, numLinea: int):
        componentes = []
        # termina cuando si la linea esta vacia, es salto de linea o un comentario de linea 
        while(linea):
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
                componente = re.match(self.descriptores[4][1], linea)
                nuevoComponente = ComponenteLexico(self.descriptores[4][0], componente.group(), numLinea)
                componentes.append(nuevoComponente)
                linea = linea[componente.end():]
                
            elif (re.match(self.descriptores[5][1], linea)) != None:
                break

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
            elif (re.match(self.descriptores[17][1], linea)) != None:
                componente = re.match(self.descriptores[17][1], linea)
                nuevoComponente = ComponenteLexico(self.descriptores[17][0], componente.group(), numLinea)
                componentes.append(nuevoComponente)
                linea = linea[componente.end():]
            elif (re.match(self.descriptores[18][1], linea)) != None:
                componente = re.match(self.descriptores[18][1], linea)
                nuevoComponente = ComponenteLexico(self.descriptores[18][0], componente.group(), numLinea)
                componentes.append(nuevoComponente)
                linea = linea[componente.end():]
            elif (re.match(self.descriptores[19][1], linea)) != None:
                componente = re.match(self.descriptores[19][1], linea)
                nuevoComponente = ComponenteLexico(self.descriptores[19][0], componente.group(), numLinea)
                componentes.append(nuevoComponente)
                linea = linea[componente.end():]
            else:
                # Manejo de errores                         #ver lexema con error
                print(f'Error lexico en la linea {numLinea} ":  " {linea}')
                return False
            
        return componentes