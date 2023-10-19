from explorador import TipoComp, ComponenteLéxico
from utils.arbol import ÁrbolSintáxisAbstracta, NodoÁrbol, TipoNodo

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
            raise SyntaxError(str(self.componenteActual))

        
        return NodoÁrbol(TipoNodo.MASTER, nodos=nodos_nuevos)
    
    
    # Asignacion ::= Variable '=' [Fenix | Unicornio | Ponto | Supay | FuncionAmbiente]
    def analizarAsignacion(self):

        nodos_nuevos = []

        # La variable en esta posición es obligatoria
        nodos_nuevos += [self.verificarVariable()] ####################################################

        # Igual el métale
        self.__verificar('=')


        # El siguiente bloque es de opcionales


        if self.componenteActual.tipo in [TipoComp.ENTERO, TipoComp.FLOTANTE, TipoComp.VALOR_VERDAD, TipoComp.TEXTO] :
            nodos_nuevos += [self.__analizar_literal()]

        # los paréntesis obligatorios (es un poco feo)
        elif self.componenteActual.texto == '(': 
            nodos_nuevos += [self.__analizar_expresión_matemática()]

        # Acá tengo que decidir si es Invocación o solo un identificador
        elif self.componenteActual.tipo == TipoComp.IDENTIFICADOR:

            if self.__componente_venidero().texto == '(':
                nodos_nuevos += [self.__analizar_invocación()]
            else:
                nodos_nuevos += [self.__verificar_identificador()]

        else:
            raise SyntaxError('Viejo... acá algo reventó', self.componenteActual)

        return NodoÁrbol(TipoNodo.ASIGNACIÓN, nodos=nodos_nuevos)
    
    
    ''' 
    ################    FUNCIONES VERIFICAR    ################
    '''
    
    # Verifica si el componente lexico actual es una variable
    def verificarVariable(self):
        
        self.verificarTipoComponente(TipoComp.VARIABLE)

        nodo = NodoÁrbol(TipoNodo.VARIABLE, contenido=self.componenteActual.texto)
        self.siguienteComponente()
        return nodo
    
    # Verifica el tipo de componente del componente lexico actual
    def verificarTipoComponente(self, tipo_esperado):

        if self.componenteActual.tipo is not tipo_esperado:
            print()
            raise SyntaxError ((tipo_esperado, str(self.componenteActual.texto)))
        
    
    '''
    ################    PASAR SIGUIENTE COMPONENTE    ################
    '''

    # Pasa al siguiente componente de la lista de componentes   
    def siguienteComponente(self):
    
        self.posicionComponenteActual += 1

        if self.posicionComponenteActual >= self.cantidad_componentes:
            return

        self.componenteActual = self.componentesLexicos[self.posicionComponenteActual]
    def analizarFuncion(self):
        """
        Función ::=  ra Identificador (ParámetrosFunción) BloqueInstrucciones
        """
        nodosNuevos = []
        self.verificar("ra")
        nodosNuevos += [self.verificarIdentificador()]
        self.verificar("(")
        nodos_nuevos += [self.analizarParamsFuncion()]
        self.verificar(')')
        nodos_nuevos += [self.analizarBloqueInstrucciones()]
        return NodoArbol(TipoComp.FUNCION, \
                contenido=nodos_nuevos[0].contenido, nodos=nodos_nuevos)

