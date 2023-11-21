from cargarArchivo import cargarArchivo as utils
from Explorador.ExploradorMitos import Explorador
from Analizador.analizadorMitos import Analizador
from Verificador.verificadorMitos import Verificador

# archivo = "./Ejemplos/ConvertirABinario.txt"
archivo = "./EjemploCaracol/Caracoles.txt"

# EsPrimo revisar lo de la declaracion de variables (line 51) ----- OK
# Fibonacci revisar lo de list out of range (line 175) ----- OK
# ConvertirABinario revisar lo de declaracion de variables (line 51)

# texto = utils.leer_archivo(archivo)
# exp = Explorador(texto)
# exp.explorar()
# analizador = Analizador(exp.componentes)
# analizador.analizar()
# analizador.imprimirArbol()

texto = utils.leer_archivo(archivo)
exp = Explorador(texto)
exp.explorar()
analizador = Analizador(exp.componentes)
analizador.analizar()
# analizador.imprimirArbol()
print("---------------------------------------------------"+'\n'+ '\n' + '\n')
verificador = Verificador(analizador.getASA())
verificador.verificar()
verificador.imprimirArbol()