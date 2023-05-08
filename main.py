import os
import keyword

import pandas as pd

# Palabras clave que no podemos utilizar:
print(keyword.kwlist)

variable = 50
print(variable)

def funcion():
    """
    Comentario de varias lineas
    """
    x = 50
    return x

foo = funcion(largotexto_muy_largo,
              texto_muy_largo,
              texto_muy_largo,
              texto_muy_largo,
              texto_muy_largo)
print(foo)
print(funcion())
print('Hola', 'mundo', sep='\n')