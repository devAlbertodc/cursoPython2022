#Trabajar con listas de objetos:
#print(type({'clave1':234,'1':'234'}))

#Entre distitnos tipos se convierte todos los elementos a binario
un_set = set([35,4,74,5,7,5])
#print(type(un_set))
#print(un_set)

#No se pueden repetir valores
un_frozenset = frozenset([35,4,74,5,7,5])
#print(type(un_frozenset))
#print(un_frozenset)

frutas = ['naranja', 'manzana', 'banana']
#print(frutas)

'''
#Lista normal:
lista_numeros = ['1','2','3']
#Crea lista de la misma manera
lista_numeros_nueva = list('123')
print(lista_numeros)
print(lista_numeros_nueva)

#Obtener primer y último valor del array:
print(frutas[0])
print(frutas[-1])

#Reescribir un elemento existente:
frutas[0] = 'pera'
print(frutas)

#Si el parametro que se pasa al index no existe, muestra ValueError: x is not in the list
indice = frutas.index('pera')
print(indice)

#Inserto un elemento en la lista para un indice concreto:
frutas.insert(1, 'naranja')
#Añade elemento en el último valor de la lista
frutas.append('piña')
#Añadir más de un elememto a la vez:
'''
frutas.extend(['manzana','naranja'])
'''
#Eliminar elemento de la lista:
#del frutas[0]
#Eliminar elemento determinado:
#frutas.remove('piña')
#Eliminar último elemento (predeterminado) o especificar elemento:
#print(frutas)
#frutas.pop(3)

#Ordenar lista (con reverse=True como segundo parametro ordena descendente:
#Sortd hace una copia de la lista:
#print(sorted(frutas,reverse=True))

#Devuelve none porque la funcion necesita que le especifiquen un valor
order_frutas = frutas.sort()
#print(order_frutas)

#print(sorted(frutas))
#Lognitud de elementos en la listA:
#print(len(frutas))

print(frutas)
#Obtener primeras dos frutas:
print(frutas[:2])
#Obtener desde segundo item al ultimo:
print(frutas[2:])
#Obtener del segundo al cuarto elemento:
print(frutas[1:4])
#Ultimos cuatro valores de la lista:
print(frutas[-4:])
'''
#Recorrer elementos de una lista:
for fruta in frutas:
    print(f'Elemento: {fruta} ')

#Tupla: lista que no queremos que sea modificada:
coordenadas_vigo = ("O8°43'21.5", "N42°13'58.15")
for coordenada in coordenadas_vigo:
    print(coordenada)

#Como es una tupla, no se pueden añadirelementos ni eliminarlos con append o pop. Solo se puede borrar la tupla entera:
del coordenadas_vigo
print(coordenadas_vigo)