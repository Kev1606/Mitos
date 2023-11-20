from utils.arbol import NodoÁrbol, ÁrbolSintáxisAbstracta, TipoNodo
from Generador.visitadores import VisitantePython


class VisitantePython:
    tabuladores = 0

    def visitar(self, nodo: TipoNodo):
        resultado = ""
        if nodo.tipo is TipoNodo.MASTER:
            resultado = self.visitarMaster(nodo)
        elif nodo.tipo is TipoNodo.ASIGNACIÓN:
            resultado = self.visitarAsignacion(nodo)
        elif nodo.tipo is TipoNodo.EXPRESIÓN_MATEMÁTICA:
            resultado = self.visitarExpresionMatematica(nodo)
        elif nodo.tipo is TipoNodo.EXPRESIÓN:
            resultado = self.visitarExpresion(nodo)
        elif nodo.tipo is TipoNodo.FUNCIÓN:
            resultado = self.visitarFuncion(nodo)
        elif nodo.tipo is TipoNodo.INVOCACIÓN:
            resultado = self.visitarInvocacion(nodo)
        elif nodo.tipo is TipoNodo.PARAMETROS_FUNCION:
            resultado = self.visitarParametrosFuncion(nodo)
        elif nodo.tipo is TipoNodo.PARÁMETROS_INVOCACIÓN:
            resultado = self.visitarParametrosInvocacion(nodo)
        elif nodo.tipo is TipoNodo.INSTRUCCIONES:
            resultado = self.visitarInstruccion(nodo)
        elif nodo.tipo is TipoNodo.REPETICIÓN:
            resultado = self.visitarRepeticion(nodo)
        elif nodo.tipo is TipoNodo.BIFURCACION:
            resultado = self.visitarBifurcacion(nodo)
        elif nodo.tipo is TipoNodo.TEMIS:
            resultado = self.visitarTemis(nodo)
        elif nodo.tipo is TipoNodo.SINO:
            resultado = self.visitarSino(nodo)
        elif nodo.tipo is TipoNodo.OPERADOR_LÓGICO:
            resultado = self.visitarOperadorLogico(nodo)
        elif nodo.tipo is TipoNodo.CONDICIÓN:
            resultado = self.visitarCondicion(nodo)
        elif nodo.tipo is TipoNodo.COMPARACIÓN:
            resultado = self.visitarComparacion(nodo)
        elif nodo.tipo is TipoNodo.RETORNO:
            resultado = self.visitarRetorno(nodo)
        elif nodo.tipo is TipoNodo.ERROR:
            resultado = self.visitarError(nodo)
        elif nodo.tipo is TipoNodo.PRINCIPAL:
            resultado = self.visitarPrincipal(nodo)
        elif nodo.tipo is TipoNodo.BLOQUE_INSTRUCCIONES:
            resultado = self.visitarBloqueInstrucciones(nodo)
        elif nodo.tipo is TipoNodo.OPEMATE:
            resultado = self.visitarOpeMate(nodo)
        elif nodo.tipo is TipoNodo.COMPARADOR:
            resultado = self.visitarComparador(nodo)
        elif nodo.tipo is TipoNodo.VARIABLE:
            resultado = self.visitarVariable(nodo)
        elif nodo.tipo is TipoNodo.BOOLEANO:
            resultado = self.visitarBooleano(nodo)
        elif nodo.tipo is TipoNodo.TEXTO:
            resultado = self.visitarTexto(nodo)
        elif nodo.tipo is TipoNodo.ENTERO:
            resultado = self.visitarEntero(nodo)
        elif nodo.tipo is TipoNodo.FLOTANTE:
            resultado = self.visitarFlotante(nodo)
        elif nodo.tipo is TipoNodo.IDENTIFICADOR:
            resultado = self.visitarIdentificador(nodo)
        elif nodo.tipo is TipoNodo.TIPO:
            resultado = self.visitarTipo(nodo)
        elif nodo.tipo is TipoNodo.STRING:
            resultado = self.visitarString(nodo)
        else:
            raise Exception("Error")
        return resultado

    def visitarMaster(self, nodoActual):
        return

    def visitarAsignacion(self, nodoActual):
        return

    def visitarExpresionMatematica(self, nodoActual):
        return

    def visitarExpresion(self, nodoActual):
        return

    def visitarFuncion(self, nodoActual):
        funcion = """\ndef {}({}):\n{}"""
       
        elementos = []
        for nodo in nodoActual.nodos:
           elementos += [nodo.visitar(self)]

        return funcion.format(elementos[0],elementos[1], '\n'.join(elementos[2]))
    
    def visitarInvocacion(self, nodoActual):
        return

    def visitarParametrosInvocacion(self, nodoActual):
        return

    def visitarParametrosFuncion(self, nodoActual):
        return

    def visitarInstruccion(self, nodoActual):
        return

    def visitarRepeticion(self, nodoActual):
        return

    def visitarBifurcacion(self, nodoActual):
        return

    def visitarTemis(self, nodoActual):
        return

    def visitarSino(self, nodoActual):
        return

    def visitarOperadorLogico(self, nodoActual):
        return

    def visitarCondicion(self, nodoActual):
        return

    def visitarComparacion(self, nodoActual):
        """
        Comparación::= Valor (Comparador) Valor
        """
        resultado = "{} ({}) {}"
        elementos = []
        for nodo in nodoActual.nodos:
            elementos.append += [nodo.visitar(self)]
        return resultado.format(elementos[0], elementos[1], elementos[2])

    def visitarRetorno(self, nodoActual):
        """
        Retorno:: hades (Valor)?
        """
        resultado = "return {}"
        valor = ""
        for nodo in nodoActual.nodos:
            valor = nodo.visitar(self)
        return resultado.format(valor)

    def visitarError(self, nodoActual):
        return

    def visitarPrincipal(self, nodoActual):
        return

    def visitarBloqueInstrucciones(self, nodoActual):
        return

    def visitarOpeMate(self, nodoActual):
        return

    def visitarComparador(self, nodoActual):
        return nodoActual.contenido

    def visitarVariable(self, nodoActual):
        return

    def visitarBooleano(self, nodoActual):
        if nodoActual.contenido == "Verdadero":
            return 'True'
        elif nodoActual.contenido == "Falso":
            return 'False'
        else:
            return nodoActual.contenido


    def visitarTexto(self, nodoActual):
        return nodoActual.contenido

    def visitarEntero(self, nodoActual):
        return nodoActual.contenido

    def visitarFlotante(self, nodoActual):
        return nodoActual.contenido

    def visitarIdentificador(self, nodoActual):
        return nodoActual.contenido

    def visitarTipo(self, nodoActual):
        return

    def visitarString(self, nodoActual):
        return nodoActual.contenido
