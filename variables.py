lenguaje = 'Python'
x = 3
y = 3.14

a1, b1 = 4, 5
a1, b1 = b1, a1
print(b1)

x = 5
x += 5
print(x)

print(x * a1 + 5)

print(x)
x = x / 50
print(x)

#Reemplazar comas por puntos y formatear cadena
cantidad = 1580000
#Separador de miles por coma para despues reemplazarlo por puntos
print(f"La cantidad es de: {cantidad:,} de euros".replace(',',"."))

#Separador de miles por coma y los decimales a partir del punto
cantidad = 1580000.7451
print(f"La cantidad es de: {cantidad:,.2f} de euros")

minuto = 3.5
print(f'3,5 minutos son {minuto * 60} segundos')