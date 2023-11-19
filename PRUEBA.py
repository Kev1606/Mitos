from cargarArchivo import cargarArchivo as utils
from ExploradorMitos import Explorador
from analizador.analizadorMitos import Analizador
from Verificador.verificadorMitos import Verificador

archivo = "./Ejemplos/DiaSemana.txt"

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
analizador.imprimirArbol()
print("---------------------------------------------------"+'\n'+ '\n' + '\n')
verificador = Verificador(analizador.getASA())
verificador.verificar()
verificador.imprimirArbol()