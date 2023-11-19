from utils.arbol import NodoÁrbol, ÁrbolSintáxisAbstracta, TipoNodo
from Generador.visitadores import VisitantePython
class VisitantePython:
    tabuladores = 0
    def visitar(self, nodo: TipoNodo):
        resultado = ""