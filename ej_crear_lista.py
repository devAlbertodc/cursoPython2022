def crear_lista(n):
    lista = []
    #Range para iterar sobre una lista de numeros:
    for i in range(n):
        lista.append(i)
    return lista
print(crear_lista(10))

def saludo(lista):
    for nombre in lista:
        print(f"Hola {nombre}")

saludo(['Carmen','Juan','Marcelo'])