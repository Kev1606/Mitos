# Explorador

Este repositorio contiene un explorador diseñado para ser utilizado como parte de un compilador. El explorador se encarga de analizar y procesar el código fuente de entrada, identificando y extrayendo los componentes léxicos necesarios para el posterior proceso de compilación.

## Estructura del repositorio

El repositorio se organiza de la siguiente manera:

- **Ejemplos**: Esta carpeta contiene ejemplos de código fuente en formato de archivo de texto (.txt) que pueden ser utilizados para probar el explorador.
- **cargarArchivo**: En esta carpeta se encuentra el archivo cargarArchivo.py, que contiene una función para cargar y leer archivos de código fuente.
- **ExploradorMitos.py**: Este archivo Python contiene las clases y funciones necesarias para la construcción de los componentes léxicos del explorador. Aquí se define la lógica principal para el análisis léxico.
- **Mitos.py**: Este archivo Python es el archivo principal del proyecto. Contiene el código que inicia la ejecución del explorador y utiliza las clases definidas en ExploradorMitos.py para procesar el código fuente de entrada.

## Uso

Para utilizar este explorador en tu proyecto de compilador, sigue estos pasos:

1. Clona este repositorio en tu máquina local usando el siguiente comando:
`git clone https://gitlab.com/proyectocompi/Explorador.git`

2. Asegúrate de que tienes Python 3 instalado en tu sistema.

3. Puedes utilizar los ejemplos de código fuente ubicados en la carpeta Ejemplos o proporcionar tu propio archivo de código fuente.

4. Importa las clases y funciones necesarias desde ExploradorMitos.py en tu proyecto principal (Mitos.py) y utilízalas para analizar el código fuente.

5. Ejecuta el archivo Mitos.py para iniciar el proceso de exploración léxica y obtener los componentes léxicos necesarios para tu compilador.


## Ejecución

Para ejecutar el explorador/analizador/verificador, sigue estos pasos:
`python mitos.py --solo-TIPO ./Ejemplos/ARCHIVO.txt`

Donde TIPO es el tipo de componente léxico que deseas obtener y ARCHIVO es el nombre del archivo de código fuente que deseas analizar.
TIPO puede ser uno de los siguientes:
- explorar
- analizar
- verificar