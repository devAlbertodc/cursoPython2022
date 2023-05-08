import pandas as pd

#Exportar CSV a Excel con encabezados:
exportar = pd.read_csv('catalogo_cf.csv')
exportar.to_excel('catalogo_cf.xlsx', index=None, header=True)