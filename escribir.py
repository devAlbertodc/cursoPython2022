entrada = """Primera parte del ingenioso hidalgo don Quijote de la Mancha
"""

#with open("quijote1.txt",'w') as file:
#    file.write(entrada)

entrada_agregar = """ En un lugar de la Mancha, de cuyo nombre no quiero
acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en
astillero, adarga antigua, rocín flaco y galgo corredor. Una olla de
algo más vaca que carnero, ...
"""

# En este caso vamos a agregar el texto de la variable “entrada_agregar” al␣final del fichero
#with open("quijote1.txt",'a') as file:
#    file.write(entrada_agregar)

with open("quijote1.txt",'r') as file:
    file.seek(18)
    contenido = file.read(42)
    print(contenido)