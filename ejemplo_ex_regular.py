import re

texto = 'Hoy es un dia magnifico y maravilloso'
ex_reg = re.search('^Hoy.*so$',texto)
print(ex_reg.string)

ex_reg = re.sub('\\s','    ', texto)
print(ex_reg)