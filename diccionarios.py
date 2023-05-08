#Las claves NO se pueden redefinir, los valores SI
frutas = {'naranja':'naranja', 'manzana':'roja', 'pera':'amarilla'}
print(type(frutas))

#Obtener valor a partir de clave:
print(frutas['pera'])
#Forma alternativa:
frutas_color = frutas.get('pera')
print(frutas_color)

#Eliminar elemento de la lista:
#del frutas['naranja']

#Renombrar valor asociado a una clave existente:
frutas['manzana'] = 'verde'
print(frutas['manzana'])

for clave,valor in frutas.items():
    print(clave, valor)