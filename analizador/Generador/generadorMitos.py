from utils.arbol import ÁrbolSintáxisAbstracta
from Generador.visitadores import VisitantePython
class Generador:
    asa: ÁrbolSintáxisAbstracta
    visitador: VisitantePython  #Hay que cambiar el tipo de dato para cuando se haga el visitador. 
    ambienteEstandar = ""
    def __init__(self, nuevoASA: ÁrbolSintáxisAbstracta):
        self.asa = nuevoASA