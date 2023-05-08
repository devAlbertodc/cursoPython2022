'''
Crear un programa que evalúe la longitud de la hipotenusa (es decir, el lado más largo de un
triangulo rectángulo, el opuesto al ángulo recto) con lados de 3 cms. y 4 cms. utilizando el
Teorema de Pitágoras (El cuadrado de la hipotenusa es igual a la suma de los cuadrados de
los dos catetos). Imprimir el resultado en pantalla.
'''

from math import sqrt

L1 = int(input('introduzca lado1: '))
L2 = int(input('introduzca lado2: '))

# Cálculo de hipotenusa
H = sqrt(L1*L1 + L2*L2)
print(f'El valor de la hipotenusa es: {H}')
