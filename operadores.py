#De toda la cadena obtengo ciertos caracteres:
print('python'[0:6:2])

#Multiplicar cadena por 5 veces:
print('python ' * 5)

#Ver si subcadena esta en cadena:
print('y' in 'python')
print('z' in 'python')
print('z' not in 'python')

#Comparar cadenas:
print('python' == 'Python')
print('python' == 'python')

#Se ordenan segun codigo en ascii
print('python' < 'Python')
print('a' < 'Z')

#Obtener letra con may0r codigo ascii de una palabra
print(max('Python'))
print(min('Python'))

#Pasar texto a mayuscula, minuscula:
print('Python'.upper())
print('Python'.lower())

print('Esto es python'.split(' '))