#Ejemplo para intercambiar elementos de una lista:
#Es lo mismo que usar la funcion sort o sorted
lista = [21, 35, 74, 32, 11]
intercammbio = True

while intercammbio:
    intercammbio = False

    for i in range(len(lista) -1):
        #Si el elemento actual es mayor que el proximo, hago intercambio:
        if int(lista[i]) > int(lista[i+1]):
            intercammbio = True
            lista[i], lista[i+1] = lista[i+1], lista[i]
print(lista)

#Copia la lista y deja el originai sin modificar:
print(sorted(lista))

#Modifico la lista verdadera:
print(lista.sort())

#Revertir la lista:
print(sorted(lista,reverse=True))
print(lista.reverse())

#Las dos listas tienen el mismo id y espacio de memoria. Si altero una tabla, se modificara la otra tambien:
lista = [21, 35, 74, 32, 11]
lista_copia = lista
print(id(lista))
print(id(lista_copia))

#Hacer copia de la lista en otra posicion de memoria:
lista_otra = lista.copy()
print(id(lista_otra))

minusculas = ['El','Lenguaje','Python','es','multiplataforma']
mayusculas = [minusc.upper() for minusc in minusculas]
print(mayusculas)

#Multiplicar valores en un rango
dup_valor = [y * 2 for y in range(20)]
print(dup_valor)