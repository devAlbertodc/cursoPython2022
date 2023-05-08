import os
from pathlib import Path

#Crear carpeta directorio_quijote en directorio actual
fichero_path = Path('.','directorio_quijote')

#Crear carpeta si no existe:
if not fichero_path.exists():
    os.makedirs(fichero_path)

#Ruta completa y dar nombre al documento:
fichero_path = fichero_path.joinpath('quijote2.txt')

#Abrir fichero y escribir las lineas en el fichero:
with fichero_path.open('w') as file:
    lineas = [
        "Primera parte del ingenioso hidalgo don Quijote de la Mancha \n"
        "Capítulo primero. Que trata de la condición y ejercicio del famoso \n"
        "hidalgo don Quijote \n"
    ]
    file.writelines(lineas)