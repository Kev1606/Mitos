from ExploradorMitos import TipoComp, ComponenteLexico
from utils.arbol import ÁrbolSintáxisAbstracta, NodoÁrbol, TipoNodo

class Analizador:

    ########## IMPORTANTE NOTAR QUE EN MITOS, EN VEZ DEL TIPO DE COMPONENTE INDENTIFICADOR, SE UTILIZA TEXTO ##########

    componentesLexicos : list
    cantidadComponentes: int
    posicionComponenteActual : int
    componenteActual : ComponenteLexico

    def __init__(self, listaComponentes):

        self.componentesLexicos = listaComponentes
        self.cantidadComponentes = len(listaComponentes)

        self.posicionComponenteActual = 0
        self.componenteActual = listaComponentes[0]

        self.asa = ÁrbolSintáxisAbstracta()
    
    # Metodo que inicia el analisis por descenso recursivo
    def analizar(self):
        self.asa.raiz = self.analizarPrograma()

    def imprimirArbol(self):
        self.asa.imprimir_preorden()

    def imprimirLista(self):
        print(self.componentesLexicos)

    # Empieza a analizar la estructura del programa, verifica asignaciones y definiciones de funciones
    def analizarPrograma(self):
        nodosNuevos = []

        # analiza si hay asignaciones o funciones
        while (True):

            # Si es asignación
            if ((self.componenteActual.texto).strip() == TipoComp.TEXTO):
                nodosNuevos = [self.analizarAsignacion()]

            # Si es función
            elif ((self.componenteActual.texto).strip() == 'ra'):
                nodosNuevos += [self.analizarFuncion()]

            else:
                break

        # De fijo al final una función principal
        if ((self.componenteActual.texto).strip() == 'zeus'):
            nodosNuevos += [self.__analizar_principal()]
        else:
            pass

        
        return NodoÁrbol(TipoNodo.MASTER, nodos=nodosNuevos)
    
    
    # Asignacion ::= Variable '=' [Fenix | Unicornio | Ponto | Supay | FuncionAmbiente]
    def analizarAsignacion(self):

        nodosNuevos = []

        # La variable en esta posición es obligatoria
        nodosNuevos += [self.verificarVariable()] 

        # Despues de la variable es obligatorio el '='
        self.verificar('=')

        
        if self.componenteActual.tipo in [TipoComp.ENTERO, TipoComp.FLOTANTE, TipoComp.BOOLEANO, TipoComp.TEXTO, TipoComp.STRING]:
            nodosNuevos += [self.analizarTipo()]

        # los paréntesis obligatorios (es un poco feo) 
        elif (self.componenteActual.texto).strip() == '(': 
            nodosNuevos += [self.analizarExpresionMatematica()] 

        # En caso de ser una llamada a una funcion o simplemente un texto 
        elif self.componenteActual.tipo == TipoComp.TEXTO:

            if self.__componente_venidero().texto == '(':
                nodosNuevos += [self.analizarInvocacion()]
            else:
                nodosNuevos += [self.verificarTexto()]

        else:
            raise SyntaxError('Se cay[o]', self.componenteActual.texto)

        return NodoÁrbol(TipoNodo.ASIGNACIÓN, nodos=nodosNuevos)
    
    # analiza que tipo de componente es
    # Tipo ::= ['fenix' | 'unicornio' | 'ponto' | 'supay']   EN EL EXPLORADOR NO SE UTILIZA UNICORNIO, SINO TEXTO
    # analizar_Literal del profe
    def analizarTipo(self):

        if self.componenteActual.tipo is TipoComp.TIPO:
            nodo = self.verificarTipo()

        elif self.componenteActual.tipo is TipoComp.TEXTO:
            nodo = self.verificarTexto()

        elif  self.componenteActual.tipo is TipoComp.BOOLEANO:
            nodo = self.verificarBooleano()

        elif self.componenteActual.tipo is TipoComp.ENTERO:
            nodo = self.verificarEntero()

        elif self.componenteActual.tipo is TipoComp.STRING:
            nodo = self.verificarString()

        else:
            nodo = self.verificarFlotante()

        return nodo
    
    # ExpresionMate ::= Variable | Numero | '(' Expresion ')'
    def analizarExpresionMatematica(self):

        nodosNuevos = []
        
        # Se verifica si es una variable
        if self.componenteActual.tipo == TipoComp.VARIABLE:
            nodosNuevos += [self.verificarVariable()]

        # Se verifica si es funcion
        elif self.componenteActual.tipo == TipoComp.TEXTO:
            if self.__componente_venidero().texto == '(':
                nodosNuevos += [self.analizarLlamada()]
            else:
                nodosNuevos += [self.verificarTexto()]

        # Se verifica si es un numero entero
        elif self.componenteActual.tipo == TipoComp.ENTERO:
            nodosNuevos += [self.verificarEntero()]

        # Se verifica si es un numero flotante
        elif self.componenteActual.tipo == TipoComp.FLOTANTE:
            nodosNuevos += [self.verificarFlotante()]
        
        # Al no ser ninguna de las anteriores, se analiza la Expresion
        else:
            self.verificar('(')

            nodosNuevos += [self.analizarExpresion()]

            self.verificar(')')

        return NodoÁrbol(TipoNodo.EXPRESIÓN_MATEMÁTICA, nodos=nodosNuevos)
    
    # Se analiza la expresion: Expresion ::= ExpresionMate Operador_Mate ExpresionMate
    def analizarExpresion(self):

        nodosNuevos = []

        # Acá no hay nada que hacer todas son obligatorias en esas
        # posiciones
        nodosNuevos += [self.analizarExpresionMatematica()]

        nodosNuevos += [self.verificarOperador()]

        nodosNuevos += [self.analizarExpresionMatematica()]

        return NodoÁrbol(TipoNodo.EXPRESIÓN , nodos=nodosNuevos)
    
    def analizarFuncion(self):
        """
        Función ::=  ra TEXTO (ParámetrosFunción) BloqueInstrucciones
        """
        nodosNuevos = []
        self.verificar('ra')
        nodosNuevos += [self.verificarTexto()]
        self.verificar('(')
        nodosNuevos += [self.analizarParametrosInvocacion()]
        self.verificar(')')
        nodosNuevos += [self.analizarBloqueInstrucciones()]
        return NodoÁrbol(TipoNodo.FUNCIÓN, \
                contenido=nodosNuevos[0].contenido, nodos=nodosNuevos)
    
    
    def analizarBloqueInstrucciones(self):
        """
        BloqueInstrucciones ::= '{' ListaInstrucciones '}'
        """
        nodosNuevos = []
        self.verificar('{')

        nodosNuevos += [self.analizarListaInstrucciones()] 

        # Analizar el resto de instrucciones en el bloque (si es que hay)
        while (self.componenteActual.texto).strip() != '}':
            nodosNuevos += [self.analizarListaInstrucciones()]
            if (self.componenteActual.texto).strip() == '}':
                break
        self.verificar('}')
        
        return NodoÁrbol(TipoNodo.BLOQUE_INSTRUCCIONES, nodos=nodosNuevos)

    def analizarListaInstrucciones(self):
        """
        Instruccion ::= Funcion | Si_Desicion | (Asignacion | Invocacion) | Retorno | Mientras_Instruccion
        """
        nodosNuevos = []

        if (self.componenteActual.texto).strip() == 'ra':
            nodosNuevos += [self.analizarFuncion()]
        elif (self.componenteActual.texto).strip() == 'temis':
            nodosNuevos += [self.analizarBifurcacion()]  
        elif self.componenteActual.tipo == TipoComp.TEXTO:
            if self.__componente_venidero().texto == '=':
                nodosNuevos += [self.analizarAsignacion()]
            elif self.__componente_venidero().tipo == TipoComp.OPEMATE:
                self.siguienteComponente()
                nodosNuevos += [self.analizarOpeMate()]
            elif (self.__componente_venidero().texto).strip() == '(':
                self.analizarExpresionMatematica()
            else:
                nodosNuevos += [self.analizarInvocacion()]
        elif self.componenteActual.tipo == TipoComp.TIPO:
            nodosNuevos += [self.analizarTipo()]
            nodosNuevos += [self.analizarAsignacion()]
        elif (self.componenteActual.texto).strip() == 'hades':
            nodosNuevos += [self.analizarRetorno()]
        elif (self.componenteActual.texto).strip() == 'sisifo':
            nodosNuevos += [self.analizarMientras()]
        else:
            self.verificar(';')
        
        return NodoÁrbol(TipoNodo.INSTRUCCIONES, nodos=nodosNuevos)

    def analizarOpeMate(self):
        nodosNuevos = []
        self.verificarTipoComponente(TipoComp.OPEMATE)
        self.siguienteComponente()
        self.verificar('=')
        nodosNuevos += [self.analizarAsignacionEspecial()]

        return NodoÁrbol(TipoNodo.ASIGNACIÓN, nodos=nodosNuevos)

    def analizarAsignacionEspecial(self):
        nodosNuevos = []
        if self.componenteActual.tipo == TipoComp.ENTERO or self.componenteActual.tipo == TipoComp.FLOTANTE:
            nodosNuevos += [self.analizarTipo()]
        elif (self.componenteActual.texto).strip() == '(':
            nodosNuevos += self.analizarExpresionMatematica()
        else:
            mensajeError = f"Se esperaba ENTERO, FLOTANTE, OPERACION_MATE, pero se obtuvo: {self.componenteActual.tipo}"
            raise SyntaxError (mensajeError)
        
        return NodoÁrbol(TipoNodo.ASIGNACIÓN, nodos=nodosNuevos)

    def analizarMientras(self):

        nodosNuevos = []

        nodosNuevos += [self.verificarSisifo()]

        self.verificar('(')
        nodosNuevos += [self.analizarComparacion()]
        self.verificar(')')

        nodosNuevos += [self.analizarBloqueInstrucciones()]
        return NodoÁrbol(TipoNodo.REPETICIÓN, nodos=nodosNuevos)

    def analizarBifurcacion(self):
        """
        Si_Desicion ::= temis ExpresionBloqueInstrucciones (Sino_Desicion)?
        Si_Desicion ::= temis '(' Condicion ')' atenea '{' Instruccion* '}'
        """
        nodosNuevos = []
        
        nodosNuevos += [self.analizar_Temis()]
        nodosNuevos += [self.verificarAtenea()]
        nodosNuevos += [self.analizarBloqueInstrucciones()]

        return NodoÁrbol(TipoNodo.BIFURCACION, nodos=nodosNuevos)

    def analizar_Temis(self):
        nodosNuevos = []
        self.verificar('temis')
        self.verificar('(')
        nodosNuevos += [self.analizarComparacion()]
        self.verificar(')')
        
        return NodoÁrbol(TipoNodo.TEMIS, nodos=nodosNuevos)

    # Comparacion ::= (Fenix | Numero | Ponto | Texto | Booleano) Operador_Comparativo (Fenix | Numero | Ponto | Texto | Booleano)
    def analizarComparacion(self):
        
        nodosNuevos = []

        # Sin opciones, todo se analiza
        nodosNuevos += [self.analizarParametro()]
        nodosNuevos += [self.__verificar_comparador()]
        nodosNuevos += [self.analizarParametro()]

        return NodoÁrbol(TipoNodo.COMPARACIÓN, nodos=nodosNuevos)

    def analizarLlamada(self):

        nodosNuevos = []

        #todos son obligatorios en ese orden
        nodosNuevos += [self.verificarTexto()]
        self.verificar('(')
        nodosNuevos += [self.analizarParametrosLlamada()]
        self.verificar(')')

        return NodoÁrbol(TipoNodo.INVOCACIÓN , nodos=nodosNuevos)
    
    def analizarInvocacion(self):
    
        nodosNuevos = []

        #todos son obligatorios en ese orden
        nodosNuevos += [self.verificarTexto()]
        self.verificar('(')
        nodosNuevos += [self.analizarParametrosInvocacion()]
        self.verificar(')')

        return NodoÁrbol(TipoNodo.INVOCACIÓN , nodos=nodosNuevos)
    
    def analizarParametrosLlamada(self):

        nodosNuevos = []

        # Fijo un valor tiene que haber
        nodosNuevos += [self.analizarParametro()]

        while( (self.componenteActual.texto).strip() == ','):
            self.verificar(',')
            nodosNuevos += [self.analizarParametro()]
        # Esto funciona con lógica al verrís... Si no revienta con error
        # asumimos que todo bien y seguimos.

        return NodoÁrbol(TipoNodo.PARÁMETROS_INVOCACIÓN , nodos=nodosNuevos)
    
    # ListaArgumentos ::= Expresion | Expresion ',' ListaArgumentos
    def analizarParametrosInvocacion(self):
    
        nodosNuevos = []

        # Fijo un valor tiene que haber
        nodosNuevos += [self.analizarParametro()]
        nodosNuevos += [self.verificarVariable()]

        while( (self.componenteActual.texto).strip() == ','):
            self.verificar(',')
            nodosNuevos += [self.analizarParametro()]
            nodosNuevos += [self.verificarVariable()]
        # Esto funciona con lógica al verrís... Si no revienta con error
        # asumimos que todo bien y seguimos.

        return NodoÁrbol(TipoNodo.PARÁMETROS_INVOCACIÓN , nodos=nodosNuevos)
    
    def analizarRetorno(self):
        nodosNuevos = []

        self.verificar('hades')
        nodosNuevos += [self.analizarTipo()]

        return NodoÁrbol(TipoNodo.RETORNO, nodos=nodosNuevos)
    
    # Analiza el parametro de una lista de argumentos (texto, entero, booleano o flotante)
    # Es el equivalente a analizar_valor del profe
    def analizarParametro(self):

        # Verifica si es texto, entero, booleano o flotante
        if self.componenteActual.tipo is TipoComp.TEXTO:
            if self.__componente_venidero().texto == '(':
                nodo = self.analizarLlamada()
            else:
                nodo = self.verificarTexto()
        
        elif self.componenteActual.tipo is TipoComp.STRING:
            nodo = self.verificarString()
        
        elif (self.componenteActual.texto).strip() == '(':
            nodo = self.analizarExpresionMatematica()

        else:
            nodo = self.analizarTipo()

        return nodo



    ''' 
    ################################    FUNCIONES VERIFICAR    ################################
    '''    
    # Verifica el tipo de componente del componente lexico actual
    def verificarTipoComponente(self, tipo_esperado):

        if self.componenteActual.tipo is not tipo_esperado:
            mensajeError = f"ERROR: Tipo esperado: {tipo_esperado} Tipo que se recibio: {self.componenteActual.texto.strip()}"
            print()
            raise SyntaxError (mensajeError)
        
    # Verifica si el texto que recibe como entrada, coincide con el texto del componente actual
    def verificar(self, texto_esperado):

        if (self.componenteActual.texto).strip() != texto_esperado:
            mensajeError = f"ERROR: Texto esperado: {texto_esperado} Texto que se recibio: {self.componenteActual.texto.strip()}"
            print()
            raise SyntaxError (mensajeError)

        self.siguienteComponente()

    def verificarTipo(self):

        self.verificarTipoComponente(TipoComp.TIPO)

        nodo = NodoÁrbol(TipoNodo.TIPO, contenido=(self.componenteActual.texto).strip())
        self.siguienteComponente()
        return nodo

    # Verifica si el componente actual es de tipo TEXTO 
    # Texto::= [a-zA-Z0-9_]+        Texto ::= .+ ES UNA EXPRESION QUE PERMITE CUALQUIER COMBINACION DE CARACTERES
    def verificarTexto(self):
        
        self.verificarTipoComponente(TipoComp.TEXTO)

        nodo = NodoÁrbol(TipoNodo.TEXTO, contenido=(self.componenteActual.texto).strip())
        self.siguienteComponente()
        return nodo

    def verificarString(self):
        self.verificarTipoComponente(TipoComp.STRING)

        nodo = NodoÁrbol(TipoNodo.STRING, contenido=(self.componenteActual.texto).strip())
        self.siguienteComponente()
        return nodo

    # Verifica si el componente lexico actual es una variable
    def verificarVariable(self):
        
        if self.componenteActual.tipo is TipoComp.VARIABLE:
            self.verificarTipoComponente(TipoComp.VARIABLE)
            nodo = NodoÁrbol(TipoNodo.VARIABLE, contenido=(self.componenteActual.texto).strip())
            self.siguienteComponente()
        
        elif self.componenteActual.tipo is TipoComp.TEXTO:
            self.verificarTipoComponente(TipoComp.TEXTO)
            nodo = NodoÁrbol(TipoNodo.TEXTO, contenido=(self.componenteActual.texto).strip())
            self.siguienteComponente()
        else:
            mensajeError = f"ERROR: El componente actual es de tipo: {self.componenteActual.tipo}, no es tipo VARIABLE ni TEXTO"
            raise SyntaxError (mensajeError)
        return nodo
    # Verifica si el componente actual es de tipo BOOLEANO
    def verificarBooleano(self):
        
        self.verificarTipoComponente(TipoComp.BOOLEANO)

        nodo = NodoÁrbol(TipoNodo.BOOLEANO, contenido=(self.componenteActual.texto).strip())
        self.siguienteComponente()
        return nodo
    
    # Verifica que el componente actual es de tipo ENTERO
    def verificarEntero(self):
    
        self.verificarTipoComponente(TipoComp.ENTERO)

        nodo = NodoÁrbol(TipoNodo.ENTERO, contenido=(self.componenteActual.texto).strip())
        self.siguienteComponente()
        return nodo
    
    # Verificar que el tipo de componente es FLOTANTE
    def verificarFlotante(self):
        self.verificarTipoComponente(TipoComp.FLOTANTE)

        nodo = NodoÁrbol(TipoNodo.FLOTANTE, contenido=(self.componenteActual.texto).strip())
        self.siguienteComponente()
        return nodo
    
    # Verifica que el operador matematico sea el correcto
    def verificarOperador(self):
        
        self.verificarTipoComponente(TipoComp.OPEMATE)

        nodo = NodoÁrbol(TipoNodo.OPEMATE, contenido=(self.componenteActual.texto).strip())
        self.siguienteComponente()

        return nodo
    
    def __verificar_comparador(self):
        self.verificarTipoComponente(TipoComp.COMPARADOR)

        nodo = NodoÁrbol(TipoNodo.COMPARADOR, contenido=(self.componenteActual.texto).strip())
        self.siguienteComponente()
        return nodo
    
    def verificarSisifo(self):
        self.verificar('sisifo')
        nodo = NodoÁrbol(TipoNodo.REPETICIÓN, contenido=(self.componenteActual.texto).strip())
        return nodo
    
    def verificarAtenea(self):
        self.verificar('atenea')
        nodo = NodoÁrbol(TipoNodo.CONDICIÓN, contenido=(self.componenteActual.texto).strip())
        return nodo
    '''
    ################    PASAR SIGUIENTE COMPONENTE    ################
    '''

    # Pasa al siguiente componente de la lista de componentes   
    def siguienteComponente(self):
    
        self.posicionComponenteActual += 1

        if self.posicionComponenteActual >= self.cantidadComponentes:
            return

        self.componenteActual = self.componentesLexicos[self.posicionComponenteActual]

    def __componente_venidero(self, avance=1):
        """
        Retorna el componente léxico que está 'avance' posiciones más
        adelante... por default el siguiente. Esto sin adelantar el
        contador del componente actual.
        """
        return self.componentesLexicos[self.posicionComponenteActual+avance]