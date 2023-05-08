def funcion(tipo, valor='A'):
    print(tipo, valor)

#Pasar valores directos:
funcion('Manzana','Verde')
funcion('telefono', 656656656)

#Poner cada valor a que referencia:
funcion(tipo = 'Carmen', valor='Zaragoza')
#El orden de los argumentos afecta en otros lenguajes:
funcion(valor = 'Carmen', tipo='Zaragoza')

#Si no pongo parámetro, se pone el definido por defecto en la función:
funcion(tipo='Carmen')
