#Envio un elemento con clave y valor:
def ej_kwargs(**kwargs):
    for clave,valor in kwargs.items():
        print('{0} de {1}'.format(clave, valor))

kwargs = {'tres':3, 'cinco':5, 'siete':7}
ej_kwargs(**kwargs)

print("\nPresiona la tecla Entrar para finalizar el programa.")
input()
print("FIN.")