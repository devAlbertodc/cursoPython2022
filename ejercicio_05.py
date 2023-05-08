#Crear un programa que le pregunte al usuario su nombre y edad y le muestre el año en que

import datetime

nombre = str(input('Escriba su nombre: '))
edad = int(input('Escriba su edad: '))

x = datetime.datetime.now().year
año = (100 - edad) + x
print(año)