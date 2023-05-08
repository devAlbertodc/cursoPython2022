import pandas as pd

#Fichero importar:
fichero_csv = 'catalogo_cf.csv'
fichero_tsv = 'catalogo_cf.tsv'

#Ficheros exportar:
escribir_csv = 'catalogo_cf_exp.csv'
escribir_tsv = 'catalogo_cf_exp.tsv'

#Lectura de ambos ficheros:
leer_csv = pd.read_csv(fichero_csv, encoding='ISO-8859-1')
#Indicar separador:
leer_tsv = pd.read_csv(fichero_tsv, encoding='utf-8-sig', sep="\t")

#Leer primeras 20 lineas del encabezado:
print(leer_csv.head(10))
print(leer_tsv.head(10))

#Escribir en el fichero csv las primeras 10 filas:
with open(escribir_csv,'w', encoding='ISO-8859-1') as write_csv:
    # index=False no muestra el índice
    write_csv.write(leer_csv.head(10).to_csv(sep=',', index=False))

# Escribir en el fichero csv las primeras 10 filas:
with open(escribir_tsv, 'w', encoding='utf-8-sig') as write_tsv:
    # index=False no muestra el índice
    write_tsv.write(leer_tsv.head(10).to_csv(sep='\t', index=False))
