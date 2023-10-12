# Archivo principal para el explorador

from cargarArchivo import cargarArchivo as func
from ExploradorMitos import Explorador 

# Funcion principal del explorador
# Entradas: recibe la ruta del archivo que el usuario desea procesar
# Salidas: Imprime la lista de componentes lexicos 
def mitos(ruta):
    texto = func.leer_archivo(ruta) # Llama a la funcion leer_archivo de la carpeta cargarArchivo
    exp = Explorador(texto) # Invoca el constructor del explorador. Se encuentra en el archivo ExploradorMitos
    exp.explorar()
    exp.imprimir_componentes()

# Despliega un menu para ejecutar cualquiera de los 5 programas disponibles
# Invoca al metodo mitos para el procesamiento del archivo
# Entradas: Un numero del 1-5
def menu():
    while(True):
        print('Ingrese el numero de archivo que desea ejecutar (presione enter para salir): ')
        print("1. Fibonacci")
        print("2. Factorial")
        print("3. EsPrimo")
        print("4. DiaSemana")
        print("5. ConvertirABinario")
        opcion = input("Ingrese el numero: ")
        if opcion == '1':
            mitos("./Ejemplos/Factorial.txt")
        elif opcion == '2':
            mitos("./Ejemplos/Fibonacci.txt")
        elif opcion == '3':
            mitos("./Ejemplos/EsPrimo.txt")
        elif opcion == '4':
            mitos("./Ejemplos/DiaSemana.txt")
        elif opcion == '5':
            mitos("./Ejemplos/ConvertirABinario.txt")
        else:
            break
        input("Presione Enter para continuar")

if __name__ == '__main__':
    menu()
