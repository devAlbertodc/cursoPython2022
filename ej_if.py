'''
numero1 = int(input("Ingresa un número entero: "))
numero2 = int(input("Ingresa otro número entero: "))
if numero1 > numero2:
    numero_mayor = numero1
else:
    numero_mayor = numero2
print(f'El numero mayor es {numero_mayor}')
'''


#Ejemplo 2: if anidados:
'''clave = input("Ingresa la clave: ")

if len(clave) >= 8:
    print("Clave verificada")

    if clave == '12345678':
        print("La clave es correcta")
    else:
        print("Clave incorrecta")
else:
    clave != '12345678'
    print('Tu clave tiene menos de 8 caracteres o es incorrecta.')
'''

#Ejemplo 3:
# Se obtienen dos números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
# Se elige el número mayor
if numero1 == numero2:
    print("Los números tienen idéntico valor")
elif numero1 > numero2:
    numero_mayor = numero1
    print("El número mayor es:", numero_mayor)
else:
    numero_mayor = numero2
    print("El número mayor es:", numero_mayor)