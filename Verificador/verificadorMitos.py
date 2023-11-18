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
            if registro["profundidad"] == self.profundidad:
                self.simbolos.remove(registro)
        self.profundidad -= 1

    def nuevoRegistro(self, nodo, nombreRegistro=""):
        """
        Agrega un registro nuevo a la tabla de simbolos en el scope iniciado
        antes de llamar a esta funcion
        """
        diccionario = {}

        diccionario["nombre"] = nodo.contenido
        diccionario["profundidad"] = self.profundidad
        diccionario["referencia"] = nodo

        self.simbolos.append(diccionario)

    def verificarExistencia(self, nombre):
        """
        Verifica si un Identificador (Texto o Funcion en el caso de mitos)
        existe como variable/funcion global o local
        """
        for registro in self.simbolos:
            # En caso de ser variable local
            if (
                registro["nombre"] == nombre
                and registro["profundidad"] <= self.profundidad
            ):
                return registro

        raise Exception("No se encontro en el scope", nombre)

    def __str__(self):
        resultado = "TABLA DE SÍMBOLOS\n\n"
        resultado += "Profundidad: " + str(self.profundidad) + "\n\n"
        for registro in self.símbolos:
            resultado += str(registro) + "\n"

        return resultado


class Visitante:
    tablaSimbolos: TablaSimbolos

    def __init__(self, nuevaTablaSimbolos):
        self.tablaSimbolos = nuevaTablaSimbolos

    def visitar(self, nodo: TipoNodo):
        """
        Visita cada nodo segun el tipo que sea
        """
        if nodo.tipo is TipoNodo.MASTER:
            self.__visitarPrograma(nodo)

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

        # elif nodo.tipo is TipoNodo.ERROR:
        #     self.visitarError(nodo)

        # elif nodo.tipo is TipoNodo.PRINCIPAL:
        #     self.visitarPrincipal(nodo)

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
            raise Exception("Se recibio un TipoNodo que no esta definido: ", nodo)

    def __visitarPrograma(self, nodoActual):
        """
        Visita el nodo principal del programa
        """
        for hijo in nodoActual.nodos:
            hijo.visitar(self)

    def visitarAsignacion(self, nodoActual):
        """
        Visita el nodo de asignacion
        """
        # REVISAR PORQUE EN LAS ASIGNACIONES VA DIFERENTE PARA LAS DE PARAMETROS
        # EN PARAMETROS ES .nodos[1] y en las normales es .nodos[0]
        self.tablaSimbolos.nuevoRegistro(nodoActual.nodos[1])

        for hijo in nodoActual.nodos:
            hijo.visitar(self)

        # Si es una funcion
        nodoActual.atributos["tipo"] = nodoActual.nodos[0].atributos["tipo"]
        nodoActual.nodos[0].atributos["tipo"] = nodoActual.nodos[0].atributos[
            "tipo"
        ]

    def visitarExpresionMatematica(self, nodoActual):
        """
        Visita el nodo de expresion matematica
        """
        for hijo in nodoActual.nodos:
            if hijo.tipo == TipoNodo.TEXTO:
                check = self.tablaSimbolos.verificarExistencia(hijo.contenido)
            hijo.visitar(self)

        nodoActual.atributos["tipo"] = TipoDatos.NUMERO

    def visitarExpresion(self, nodoActual):
        """
        Visita el nodo de expresion
        """
        for hijo in nodoActual.nodos:
            hijo.visitar(self)

        nodoActual.atributos["tipo"] = TipoDatos.NUMERO

    def visitarFuncion(self, nodoActual):
        """
        Visita el nodo de funcion
        """
        self.tablaSimbolos.nuevoRegistro(nodoActual)
        self.tablaSimbolos.abrirBloque()

        for hijo in nodoActual.nodos:
            hijo.visitar(self)

        self.tablaSimbolos.cerrarBloque()

        nodoActual.atributos["tipo"] = nodoActual.nodos[2].atributos["tipo"]

    def visitarInvocacion(self, nodoActual):
        """
        Visita el nodo de invocacion
        """
        check = self.tablaSimbolos.verificarExistencia(
            nodoActual.nodos[0].contenido
        )

        if check["referencia"].tipo is not TipoNodo.FUNCIÓN:
            raise Exception(
                "El identificador no es una funcion", nodoActual.nodos[0].contenido
            )

        for hijo in nodoActual.nodos:
            hijo.visitar(self)

        nodoActual.atributos["tipo"] = check["referencia"].atributos["tipo"]

    def visitarParametrosInvocacion(self, nodoActual):
        """
        Visita el nodo de parametros de invocacion
        """
        for hijo in nodoActual.nodos:
            if hijo.tipo == TipoNodo.TEXTO:
                check = self.tablaSimbolos.verificarExistencia(hijo.contenido)
            elif hijo.tipo == TipoNodo.FUNCIÓN:
                raise Exception(
                    "No se puede pasar una funcion como parametro", hijo.contenido
                )
            hijo.visitar(self)

    def visitarParametrosFuncion(self, nodoActual):
        """
        Visita el nodo de parametros de funcion
        """
        for hijo in nodoActual.nodos:
            self.tablaSimbolos.nuevoRegistro(hijo)
            hijo.visitar(self)

    def visitarInstrucciones(self, nodoActual):
        """
        Visita el nodo de instrucciones
        """
        for hijo in nodoActual.nodos:
            hijo.visitar(self)
            nodoActual.atributos["tipo"] = hijo.atributos["tipo"]

    def visitarRepeticion(self, nodoActual):
        """
        Visita el nodo de repeticion
        """
        self.tablaSimbolos.abrirBloque()
        for hijo in nodoActual.nodos:
            hijo.visitar(self)

        self.tablaSimbolos.cerrarBloque()

        nodoActual.atributos["tipo"] = nodoActual.nodos[1].atributos["tipo"]

    def visitarBifurcacion(self, nodoActual):
        """
        Visita el nodo de bifurcacion
        """
        for hijo in nodoActual.nodos:
            hijo.visitar(self)

        nodoActual.atributos["tipo"] = TipoDatos.CUALQUIERA

    def visitarOperadorLogico(self, nodoActual):
        """
        Visita el nodo de operador logico
        """
        # es el if de Python
        self.tablaSimbolos.abrirBloque()
        for hijo in nodoActual.nodos:
            hijo.visitar(self)
        self.tablaSimbolos.cerrarBloque()

        nodoActual.atributos["tipo"] = nodoActual.nodos[1].atributos["tipo"]

    def visitarCondicion(self, nodoActual):
        """
        Visita el nodo de condicion
        """
        for hijo in nodoActual.nodos:
            hijo.visitar(self)

        nodoActual.atributos["tipo"] = TipoDatos.BOOLEANO

    # def visitarComparador(self, nodoActual):

    def visitarComparacion(self, nodoActual):
        """
        Visita el nodo de comparador
        """
        for hijo in nodoActual.nodos:
            if hijo.tipo == TipoNodo.TEXTO:
                check = self.tablaSimbolos.verificarExistencia(hijo.contenido)
            hijo.visitar(self)

        primerValor = nodoActual.nodos[0]
        comparador = nodoActual.nodos[1]
        segundoValor = nodoActual.nodos[2]

        if primerValor.atributos["tipo"] == segundoValor.atributos["tipo"]:
            comparador.atributos["tipo"] = primerValor.atributos["tipo"]
            nodoActual.atributos["tipo"] = TipoDatos.BOOLEANO
        else:
            raise Exception(
                "Los tipos de datos no coinciden",
                primerValor.atributos["tipo"],
                segundoValor.atributos["tipo"],
            )

    def visitarRetorno(self, nodoActual):
        """
        Visita el nodo de retorno
        """
        for hijo in nodoActual.nodos:
            hijo.visitar(self)

        if nodoActual.nodos == []:
            nodoActual.atributos["tipo"] = TipoDatos.NINGUNO
        else:
            for hijo in nodoActual.nodos:
                hijo.visitar(self)
                if hijo.tipo == TipoNodo.TEXTO:
                    check = self.tablaSimbolos.verificarExistencia(hijo.contenido)
                    nodoActual.atributos["tipo"] = check["referencia"].atributos[
                        "tipo"
                    ]
                else:
                    nodoActual.atributos["tipo"] = hijo.atributos["tipo"]

    def visitarBloqueInstrucciones(self, nodoActual):
        """
        Visita el nodo de bloque de instrucciones
        """
        for hijo in nodoActual.nodos:
            hijo.visitar(self)

        nodoActual.atributos["tipo"] = TipoDatos.NINGUNO

        for hijo in nodoActual.nodos:
            if hijo.atributos["tipo"] != TipoDatos.NINGUNO:
                nodoActual.atributos["tipo"] = hijo.atributos["tipo"]

    def visitarBooleano(self, nodoActual):
        """
        Visita el nodo de booleano
        """
        nodoActual.atributos["tipo"] = TipoDatos.BOOLEANO

    def visitarTexto(self, nodoActual):
        """
        Visita el nodo de texto
        """
        nodoActual.atributos["tipo"] = TipoDatos.TEXTO

    def visitarEntero(self, nodoActual):
        """
        Visita el nodo de entero
        """
        nodoActual.atributos["tipo"] = TipoDatos.NUMERO

    def visitarFlotante(self, nodoActual):
        """
        Visita el nodo de flotante
        """
        nodoActual.atributos["tipo"] = TipoDatos.NUMERO

    def visitarVariable(self, nodoActual):
        """
        Visita el nodo de variable
        """
        check = self.tablaSimbolos.verificarExistencia(nodoActual.contenido)
        print(nodoActual.atributos["tipo"])
        nodoActual.atributos["tipo"] = check["referencia"].atributos["tipo"]

    def visitarOpeMate(self, nodoActual):
        """
        Visita el nodo de operacion matematica
        """
        for hijo in nodoActual.nodos:
            hijo.visitar(self)

        nodoActual.atributos["tipo"] = TipoDatos.NUMERO

    def visitarString(self, nodoActual):
        """
        Visita el nodo de string
        """
        nodoActual.atributos["tipo"] = TipoDatos.TEXTO

    def visitarTipo(self, nodoActual):
        """
        Visita el nodo de tipo
        """
        # nodoActual.atributos["tipo"] = TipoDatos.TIPO
        if nodoActual.contenido == "fenix":
            nodoActual.atributos["tipo"] = TipoDatos.NUMERO
        elif nodoActual.contenido == "unicornio":
            nodoActual.atributos["tipo"] = TipoDatos.TEXTO
        else:
            nodoActual.atributos["tipo"] = TipoDatos.CUALQUIERA

    def visitarTemis(self, nodoActual):
        """
        Visita el nodo de if
        """
        # codigo para evaluar el if en la tabla de simbolos
        for hijo in nodoActual.nodos:
            hijo.visitar(self)


class Verificador:
    asa: ÁrbolSintáxisAbstracta
    visitador: Visitante
    tablaSimbolos: TablaSimbolos

    def __init__(self, arbol: ÁrbolSintáxisAbstracta):
        self.asa = arbol
        self.tablaSimbolos = TablaSimbolos()
        self.cargarAmbiente()
        self.visitador = Visitante(self.tablaSimbolos)

    def imprimirArbol(self):
        """
        Imprime el arbol de sintaxis abstracta
        """
        if self.asa.raiz is not None:
            self.asa.imprimir_preorden()
        else:
            print([])

    def cargarAmbiente(self):
        funciones = [()]

    def verificar(self):
        self.visitador.visitar(self.asa.raiz)
