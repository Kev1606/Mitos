from utils.arbol import ÁrbolSintáxisAbstracta, NodoÁrbol, TipoNodo
from utils.tipoDatos import TipoDatos

class TablaSimbolos:

    def __init__(self):
        self.simbolos = []
        self.profundidad = 0
    
    def abrirBloque(self):
        """
        Abre un scope
        """
        self.profundidad += 1
    
    def cerrarBloque(self):
        """
        Cierra un bloque de scope y borra todos los elementos que estan en este bloque
        """
        for registro in self.simbolos:
            if registro['profundidad'] == self.profundidad:
                self.simbolos.remove(registro)
        self.profundidad -= 1
    
    def nuevoRegistro(self, nodo, nombreRegistro=''):
        """
        Agrega un registro nuevo a la tabla de simbolos en el scope iniciado
        antes de llamar a esta funcion
        """
        diccionario = {}
        
        diccionario['nombre'] = nodo.contenido
        diccionario['profundidad'] = self.profundidad
        diccionario['referencia'] = nodo

        self.simbolos.append(diccionario)

    def verificarExistencia(self, nombre):
        """
        Verifica si un Identificador (Texto o Funcion en el caso de mitos) 
        existe como variable/funcion global o local
        """
        for registro in self.simbolos:

            # En caso de ser variable local
            if registro['nombre'] == nombre and registro['profundidad'] <= self.profundidad:
                return registro
        
        raise Exception('No se encontro en el scope', nombre)
    
    def __str__(self):

        resultado = 'TABLA DE SÍMBOLOS\n\n'
        resultado += 'Profundidad: ' + str(self.profundidad) +'\n\n'
        for registro in self.símbolos:
            resultado += str(registro) + '\n'

        return resultado

class Visitante:

    tablaSimbolos: TablaSimbolos

    def __init__(self, nuevaTablaSimbolos):
        self.tablaSimbolos = nuevaTablaSimbolos

    def visitar(self, nodo:TipoNodo):
        """
        Visita cada nodo segun el tipo que sea
        """
        if nodo.tipo is TipoNodo.MASTER:
            self.visitarPrograma(nodo)
        
        elif nodo.tipo is TipoNodo.ASIGNACIÓN:
            self.visitarAsignacion(nodo)
        
        elif nodo.tipo is TipoNodo.EXPRESIÓN_MATEMÁTICA:
            self.visitarExpresionMatematica(nodo)
        
        elif nodo.tipo is TipoNodo.EXPRESIÓN:
            self.visitarExpresion(nodo)

        elif nodo.tipo is TipoNodo.FUNCIÓN:
            self.visitarFuncion(nodo)
        
        elif nodo.tipo is TipoNodo.INVOCACIÓN:
            self.visitarInvocacion(nodo)
        
        elif nodo.tipo is TipoNodo.PARÁMETROS_INVOCACIÓN:
            self.visitarParametrosInvocacion(nodo)

        elif nodo.tipo is TipoNodo.PARAMETROS_FUNCION:
            self.visitarParametrosFuncion(nodo)

        elif nodo.tipo is TipoNodo.INSTRUCCIONES:
            self.visitarInstrucciones(nodo)
        
        elif nodo.tipo is TipoNodo.REPETICIÓN:
            self.visitarRepeticion(nodo)
        
        elif nodo.tipo is TipoNodo.BIFURCACION: 
            self.visitarBifurcacion(nodo)

        elif nodo.tipo is TipoNodo.OPERADOR_LÓGICO: 
            self.visitarOperadorLogico(nodo)
        
        elif nodo.tipo is TipoNodo.CONDICIÓN: 
            self.visitarCondicion(nodo)
        
        elif nodo.tipo is TipoNodo.COMPARADOR: 
            self.visitarComparador(nodo)

        elif nodo.tipo is TipoNodo.COMPARACIÓN: 
            self.visitarComparacion(nodo)
        
        elif nodo.tipo is TipoNodo.RETORNO: 
            self.visitarRetorno(nodo)

        elif nodo.tipo is TipoNodo.ERROR: 
            self.visitarError(nodo)

        elif nodo.tipo is TipoNodo.PRINCIPAL: 
            self.visitarPrincipal(nodo)
        
        elif nodo.tipo is TipoNodo.BLOQUE_INSTRUCCIONES: 
            self.visitarBloqueInstrucciones(nodo)

        elif nodo.tipo is TipoNodo.BOOLEANO: 
            self.visitarBooleano(nodo)

        # ESTE ES NUESTRO IDENTIFICADOR
        elif nodo.tipo is TipoNodo.TEXTO: 
            self.visitarTexto(nodo)
        
        elif nodo.tipo is TipoNodo.ENTERO: 
            self.visitarEntero(nodo)

        elif nodo.tipo is TipoNodo.FLOTANTE: 
            self.visitarFlotante(nodo)
        
        elif nodo.tipo is TipoNodo.VARIABLE: 
            self.visitarVariable(nodo)
        
        elif nodo.tipo is TipoNodo.OPEMATE: 
            self.visitarOpeMate(nodo)
        
        elif nodo.tipo is TipoNodo.STRING: 
            self.visitarString(nodo)

        elif nodo.tipo is TipoNodo.TIPO: 
            self.visitarTipo(nodo)
        
        elif nodo.tipo is TipoNodo.TEMIS: 
            self.visitarTemis(nodo)

        # Aqui se va a mostrar un nodo del analizador que no ha sido declarado arriba,
        # cuando salga, se debe declarar y crear la funcion
        else:
            raise Exception('Se recibio un TipoNodo que no esta definido: ', nodo)