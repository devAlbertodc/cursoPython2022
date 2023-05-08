'''
i = 1
while i <= 100:
    print(i)
    i += 2 * i + i
'''

numero_mayor = -999
numero = int(input("Ingresa un número: "))

while numero != 0:
    if numero > numero_mayor:
        numero_mayor = numero
    else:
        numero = int(input("Ingresa un número: "))

print(f'El número mayor es {numero_mayor}')