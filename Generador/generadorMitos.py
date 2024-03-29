from utils.arbol import ÁrbolSintáxisAbstracta
from Generador.visitadores import VisitantePython
class Generador:
    asa: ÁrbolSintáxisAbstracta
    visitador: VisitantePython  #Hay que cambiar el tipo de dato para cuando se haga el visitador. 
    ambienteEstandar = """import sys
import random as r
def generarAleatorio(inicioRango, finRango):
    return r.randint(inicioRango, finRango)
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
            self.asa.imprimir_preorden()
    def guardarSalida(self, salida):
        "Guarda la salida en un archivo"
        with open("output.py", "w") as archivo:
            archivo.write(self.ambienteEstandar)
            archivo.write(salida)
    def generar(self):
        resultado = self.visitador.visitar(self.asa.raiz)
        print(self.ambienteEstandar)
        print(f"resultado: {resultado}")
        self.guardarSalida(resultado)