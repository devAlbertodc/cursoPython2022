#Crear lista
def crear_lista(n):
    lista = []
    for i in range(n):
        lista.append(i)
    return lista

lista = crear_lista(10)

# valores de lista print(lista) lista resultado
lista_res = []
lista_res.append(lista[0])
lista_res.append(lista[-1])
print(f'valores primero y último de la lista: {lista_res}')
print(f'Valor más alto {max(lista_res)}')
print(f'Valor más bajo {min(lista_res)}')