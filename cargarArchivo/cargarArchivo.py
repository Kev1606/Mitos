# Procesa un archivo de texto y retorna un string de linea por linea
def leer_archivo(ruta_archivo):
    with open(ruta_archivo) as archivo:
        for linea in archivo:
            yield linea.strip("\n")
