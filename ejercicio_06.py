'''
Preguntar al usuario un número y mostrar si es par o impar.
Si el número es múltiplo de 4 imprimir el mensaje apropiado al usuario.
'''

num = int(input('Escriba un número: '))

if num % 2 == 0:
    print("Encontrado un número par", num)
    if num % 4 == 0:
        print("El número es multiplo de 4")
else:
    print("Encontrado un número impar", num)