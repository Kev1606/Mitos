from explorador.explorador import TipoComp, ComponenteLéxico
from utils.árbol import ÁrbolSintáxisAbstracta, NodoÁrbol, TipoNodo

class Analizador:

    ########## IMPORTANTE NOTAR QUE EN MITOS, EN VEZ DEL TIPO DE COMPONENTE INDENTIFICADOR, SE UTILIZA TEXTO ##########

    componentesLexicos : list
    cantidadComponentes: int
    posicionComponenteActual : int
    componenteActual : ComponenteLéxico

    def __init__(self, listaComponentes):

        self.componentesLexicos = listaComponentes
        self.cantidadComponentes = len(listaComponentes)

        self.posicionComponenteActual = 0
        self.componenteActual = listaComponentes[0]

        self.asa = ÁrbolSintáxisAbstracta()
    
    # Metodo que inicia el analisis por descenso recursivo
    def analizar(self):
        self.asa.raiz = self.analizarPrograma()

    # Empieza a analizar la estructura del programa, verifica asignaciones y definiciones de funciones
    def analizarPrograma(self):

        nodos_nuevos = []

        # analiza si hay asignaciones o funciones
        while (True):

            # Si es asignación
            if self.componenteActual.tipo == TipoComp.TEXTO:
                nodos_nuevos = [self.analizarAsignacion()]

            # Si es función
            elif (self.componenteActual.texto == 'ra'):
                nodos_nuevos += [self.analizarFuncion()]

            else:
                break

        # De fijo al final una función principal
        if (self.componenteActual.texto == 'zeus'):
            nodos_nuevos += [self.__analizar_principal()]
        else:
            pass #raise SyntaxError(str(self.componenteActual)) En nuestros ejemplos no lo tenemos asi, siempre daria error

        
        return NodoÁrbol(TipoNodo.MASTER, nodos=nodos_nuevos)
    
    
    # Asignacion ::= Variable '=' [Fenix | Unicornio | Ponto | Supay | FuncionAmbiente]
    def analizarAsignacion(self):

        nodos_nuevos = []

        # La variable en esta posición es obligatoria
        nodos_nuevos += [self.verificarVariable()] 

        # Despues de la variable es obligatorio el '='
        self.verificar('=')

        
        if self.componenteActual.tipo in [TipoComp.ENTERO, TipoComp.FLOTANTE, TipoComp.BOOLEANO, TipoComp.TEXTO]:
            nodos_nuevos += [self.analizarTipo()] 

        # los paréntesis obligatorios (es un poco feo) 
        elif self.componenteActual.texto == '(': 
            nodos_nuevos += [self.analizarExpresionMatematica()] 

        # En caso de ser una llamada a una funcion o simplemente un texto 
        elif self.componenteActual.tipo == TipoComp.TEXTO:

            if self.componentePorVenir().texto == '(':
                nodos_nuevos += [self.analizarInvocacion()]
            else:
                nodos_nuevos += [self.verificarTexto()]

        else:
            raise SyntaxError('Viejo... acá algo reventó', self.componenteActual)

        return NodoÁrbol(TipoNodo.ASIGNACIÓN, nodos=nodos_nuevos)
    
    # analiza que tipo de componente es
    # Tipo ::= ['fenix' | 'unicornio' | 'ponto' | 'supay']   EN EL EXPLORADOR NO SE UTILIZA UNICORNIO, SINO TEXTO
    # analizar_Literal del profe
    def analizarTipo(self):

        if self.componenteActual.tipo is TipoComp.TEXTO:
            nodo = self.verificarTexto()

        elif  self.componenteActual.tipo is TipoComp.BOOLEANO:
            nodo = self.verificarBooleano()

        elif self.componenteActual.tipo is TipoComp.ENTERO:
            nodo = self.verificarEntero()

        else:
            nodo = self.verificarFlotante()

        return nodo
    
    # ExpresionMate ::= Variable | Numero | '(' Expresion ')'
    def analizarExpresionMatematica(self):

        nodos_nuevos = []
        
        # Se verifica si es una variable
        if self.componenteActual.tipo == TipoComp.VARIABLE:
            nodos_nuevos += [self.verificarVariable()]

        # Se verifica si es un numero entero
        elif self.componenteActual.tipo == TipoComp.ENTERO:
            nodos_nuevos += [self.verificarEntero()]

        # Se verifica si es un numero flotante
        elif self.componenteActual.tipo == TipoComp.FLOTANTE:
            nodos_nuevos += [self.verificarFlotante()]
        
        # Al no ser ninguna de las anteriores, se analiza la Expresion
        else:
            self.verificar('(')

            nodos_nuevos += [self.analizarExpresion()]

            self.verificar(')')

        return NodoÁrbol(TipoNodo.EXPRESIÓN_MATEMÁTICA, nodos=nodos_nuevos)
    
    # Se analiza la expresion: Expresion ::= ExpresionMate Operador_Mate ExpresionMate
    def analizarExpresion(self):

        nodos_nuevos = []

        # Acá no hay nada que hacer todas son obligatorias en esas
        # posiciones
        nodos_nuevos += [self.analizarExpresionMatematica()]

        nodos_nuevos += [self.verificarOperador()]

        nodos_nuevos += [self.analizarExpresionMatematica()]

        return NodoÁrbol(TipoNodo.EXPRESIÓN , nodos=nodos_nuevos)
    
    def analizarInvocacion(self):
    
        nodos_nuevos = []

        #todos son obligatorios en ese orden
        nodos_nuevos += [self.verificarTexto()]
        self.verificar('(')
        nodos_nuevos += [self.analizarParametrosInvocacion()]
        self.verificar(')')

        return NodoÁrbol(TipoNodo.INVOCACIÓN , nodos=nodos_nuevos)
    
    # ListaArgumentos ::= Expresion | Expresion ‘,’ ListaArgumentos
    def analizarParametrosInvocacion(self):
    
        nodos_nuevos = []

        # Fijo un valor tiene que haber
        nodos_nuevos += [self.analizarParametro()]

        while( self.componente_actual.texto == ','):
            self.verificar(',')
            nodos_nuevos += [self.analizarParametro()]

        # Esto funciona con lógica al verrís... Si no revienta con error
        # asumimos que todo bien y seguimos.

        return NodoÁrbol(TipoNodo.PARÁMETROS_INVOCACIÓN , nodos=nodos_nuevos)
    
    # Analiza el parametro de una lista de argumentos (texto, entero, booleano o flotante)
    # Es el equivalente a analizar_valor del profe
    def analizarParametro(self):

        # Verifica si es texto, entero, booleano o flotante
        if self.componente_actual.tipo is TipoComp.TEXTO:
            nodo = self.verificarTexto()
        else:
            nodo = self.analizarTipo()

        return nodo
    ''' 
    ################    FUNCIONES VERIFICAR    ################
    '''
    
    # Verifica si el componente lexico actual es una variable
    def verificarVariable(self):
        
        # Se verifica que la declaracion de la variable venga con su simbolo respectivo
        if (self.componenteActual.texto)[0] != '#':
            print()
            raise SyntaxError(('x', str(self.componenteActual.texto)))

        self.verificarTipoComponente(TipoComp.VARIABLE)

        nodo = NodoÁrbol(TipoNodo.VARIABLE, contenido=self.componenteActual.texto)
        self.siguienteComponente()
        return nodo
    
    # Verifica el tipo de componente del componente lexico actual
    def verificarTipoComponente(self, tipo_esperado):

        if self.componenteActual.tipo is not tipo_esperado:
            print()
            raise SyntaxError ((tipo_esperado, str(self.componenteActual.texto)))
        
    # Verifica si el texto que recibe como entrada, coincide con el texto del componente actual
    def verificar(self, texto_esperado ):

        if self.componenteActual.texto != texto_esperado:
            print()
            raise SyntaxError ((texto_esperado, str(self.componenteActual.texto)))

        self.siguienteComponente()

    # Verifica si el componente actual es de tipo TEXTO 
    # Texto::= [a-zA-Z0-9_]+        Texto ::= .+ ES UNA EXPRESION QUE PERMITE CUALQUIER COMBINACION DE CARACTERES
    def verificarTexto(self):
        
        self.verificarTipoComponente(TipoComp.TEXTO)

        nodo = NodoÁrbol(TipoNodo.TEXTO, contenido=self.componenteActual.texto)
        self.siguienteComponente()
        return nodo

    # Verifica si el componente actual es de tipo BOOLEANO
    def verificarBooleano(self):
        
        self.verificarTipoComponente(TipoComp.BOOLEANO)

        nodo = NodoÁrbol(TipoNodo.BOOLEANO, contenido=self.componenteActual.texto)
        self.siguienteComponente()
        return nodo
    
    # Verifica que el componente actual es de tipo ENTERO
    def verificarEntero(self):
    
        self.verificarTipoComponente(TipoComp.ENTERO)

        nodo = NodoÁrbol(TipoNodo.ENTERO, contenido=self.componenteActual.texto)
        self.siguienteComponente()
        return nodo
    
    # Verificar que el tipo de componente es FLOTANTE
    def verificarFlotante(self):
        
        self.verificarTipoComponente(TipoComp.FLOTANTE)

        nodo = NodoÁrbol(TipoNodo.FLOTANTE, contenido=self.componenteActual.texto)
        self.siguienteComponente()
        return nodo
    
    # Verifica que el operador sea alguno de los siguientes
    # Operador_Mate ::= Operador_Adicion  | Operador_Resta |  Operador_Division | Operador_Multiplicacion 
    def verificarOperador(self):
        
        self.verificarTipoComponente(TipoComp.OPEMATE)

        nodo = NodoÁrbol(TipoNodo.OPEMATE, contenido=self.componenteActual.texto)
        self.siguienteComponente()

        return nodo
    
    '''
    ################    PASAR SIGUIENTE COMPONENTE    ################
    '''

    # Pasa al siguiente componente de la lista de componentes   
    def siguienteComponente(self):
    
        self.posicionComponenteActual += 1

        if self.posicionComponenteActual >= self.cantidad_componentes:
            return

        self.componenteActual = self.componentesLexicos[self.posicionComponenteActual]
    
    # Retorna el componente siguiente del actual
    def componentePorVenir(self, avance=1):
        
        return self.componentes_léxicos[self.posición_componente_actual+avance]