from utils.arbol import NodoÁrbol, ÁrbolSintáxisAbstracta, TipoNodo


class VisitantePython:
    tabuladores = 0

    def visitar(self, nodo: TipoNodo):
        resultado = ""
        print("tipo: ",nodo.tipo)
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
        instrucciones = []
        for nodo in nodoActual.nodos:
            instrucciones.append(nodo.visitar(self))
        return "\n".join(instrucciones)

    def visitarAsignacion(self, nodoActual):
        resultado = """{}={}"""
        elementos = []
        for nodo in nodoActual.nodos:
            elementos.append(nodo.visitar(self))
        
        if len(elementos) == 2:
            return resultado.format(elementos[1], 0)
        else:
            print(resultado.format(elementos[1], elementos[2]))
            return resultado.format(elementos[1], elementos[2])
    def visitarExpresionMatematica(self, nodoActual):
        expre = """{}"""
        return expre.format(nodoActual.contenido)

    def visitarExpresion(self, nodoActual):
        instrucciones = []
        for nodo in nodoActual.nodos:
            instrucciones.append(nodo.visitar(self))
        return " ".join(instrucciones)

    def visitarFuncion(self, nodoActual):
        funcion = """\ndef {}({}):\n{}"""
       
        elementos = []
        for nodo in nodoActual.nodos:
        #    for i in nodo.nodos:
        #        for j in i.nodos:
        #             print(f"contenido de nodos: {j.tipo}")
           elementos += [nodo.visitar(self)]
        print(f"elementos: {elementos}")

        return funcion.format(elementos[0],elementos[1], '\n'.join(elementos[2]))
    
    def visitarInvocacion(self, nodoActual):
        resultado = """ {}({})"""
        instrucciones = []
        for nodo in nodoActual.nodos:
            instrucciones.append(nodo.visitar(self))
        return resultado.format(instrucciones[0], instrucciones[1])

    def visitarParametrosInvocacion(self, nodoActual):
        # print(f"params: {nodoActual.contenido}")
        # params = """{}"""
        parametros = []

        for nodo in nodoActual.nodos:
            parametros.append(nodo.visitar(self))
        
        if len(parametros) > 0:
            return ",".join(parametros)
        else:
            return ""

    def visitarParametrosFuncion(self, nodoActual):
        params = """{}"""

        return params.format(nodoActual.contenido)

    def visitarInstruccion(self, nodoActual):
        instruccion = ""
        for nodo in nodoActual.nodos:
            instruccion = nodo.visitar(self)
        return instruccion

    def visitarRepeticion(self, nodoActual):
        ciclo = """while {}: \n{}"""

        elementos = []

        for nodo in nodoActual.nodos:
            if nodo.contenido in ["(", ")"]:
                continue
            elementos += [nodo.visitar(self)]

        return ciclo.format(elementos[0],elementos[1])

    def visitarBifurcacion(self, nodoActual):
        desicion = """if {} : \n{}"""

        elementos = []

        for nodo in nodoActual.nodos:
            elementos += [nodo.contenido]

        return desicion.format(elementos[0],elementos[1])

    def visitarTemis(self, nodoActual):
        resultado = """if {} : {}"""
        instrucciones = []
        for nodo in nodoActual.nodos:
            instrucciones.append(nodo.visitar(self))
        return resultado.format(instrucciones[0], "\n".join(instrucciones[1]))

    def visitarCondicion(self, nodoActual):
        return ""

    def visitarComparacion(self, nodoActual):
        """
        Comparación::= Valor (Comparador) Valor
        """
        resultado = "{} {} {}"
        elementos = []
        for nodo in nodoActual.nodos:
            elementos.append(nodo.visitar(self))
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
        return """ERROR"""

    def visitarBloqueInstrucciones(self, nodoActual):
        
        instrucciones = """\n{}"""
        ins = []

        for nodo in nodoActual.nodos:
            ins += [nodo.visitar(self)]
        
        return instrucciones.format(ins)

    def visitarOpeMate(self, nodoActual):
        instrucciones = []
        for nodo in nodoActual.nodos:
            instrucciones.append(nodo.visitar(self))
        return " ".join(instrucciones)

    def visitarComparador(self, nodoActual):
        return nodoActual.contenido

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
        """Tipo:: =  Entero | Flotante | Texto | Booleano"""
        return ""

    def visitarString(self, nodoActual):
        return nodoActual.contenido
