from utils.arbol import ÁrbolSintáxisAbstracta
from Generador.visitadores import VisitantePython
class Generador:
    asa: ÁrbolSintáxisAbstracta
    visitador: VisitantePython  #Hay que cambiar el tipo de dato para cuando se haga el visitador. 
    ambienteEstandar = """import sys

def proteo(numero):
    return str(numero)

def sirena(texto):
    print(texto)
"""

    def __init__(self, nuevoASA: ÁrbolSintáxisAbstracta):
        self.asa = nuevoASA
        self.visitador = VisitantePython()
    def imprimirASA(self):
        "Claramente imprime el ASA"
        if self.asa.raiz is None:
            print([])
        else:
            self.asa.__preorden()
    def generar(self):
        resultado = self.visitador.visitar(self.asa.raiz)
        print(self.ambienteEstandar)
        print(resultado)