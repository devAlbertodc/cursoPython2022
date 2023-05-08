import pickle

fichero = open('datos_pickle', 'rb')
datos = pickle.load(fichero)

lista = 0

for item in datos:
    print("El dato ", lista, ' es ', item)
    lista = lista +  1