import shutil
import os

# Copiar ficheros situados en el mismo directorio
#shutil.copy(src="quijote1.txt", dst="quijote03.txt")

# Copiar ficheros preservando los metadatos
#shutil.copy2(src="quijote1.txt", dst="quijote04.txt")

#Copio la carpeta y todo su contenido:
#shutil.copytree(src='directorio1', dst='directorio3')

#Copio la carpeta y todo el contenido menos las imagenes .jpg
#shutil.copytree(src='directorio1', dst='directorio4',
#                ignore=shutil.ignore_patterns('*.jpg'))

#shutil.move(src='directorio3/imagen.jpg', dst='directorio4/imagen.jpg')

# Mover y renombrar un fichero usando la biblioteca os
os.rename("directorio4/imagen.jpg", "directorio1/imagen.jpg")

#Eliminar fichero:
os.remove('directorio4/imagen.jpg')