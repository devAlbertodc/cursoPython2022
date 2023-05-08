#Abrir fichero en formato lectura:
fichero = open('codifica_quijote.txt', 'r')
for linea in fichero:
    pass
    #print(linea)
fichero.close()

#Leer parrafo de un fichero:
with open('codifica_quijote.txt', 'r') as fichero:
    leer = fichero.read(300)
    #print(leer)

#Leer linea del fichero:
with open('codifica_quijote.txt', 'r') as fichero:
    #leer = fichero.readline()
    leer = fichero.readlines(4000)

    #Leer todo el fichero por partes
    for i in leer:
        #Eliminar múltiples lineas en blanco:
        print(i.strip())