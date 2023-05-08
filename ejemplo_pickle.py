import pickle

datos = int(input("Cantidad de datos a ingresar: "))
lista_datos = []

for dato in range(datos):
    datos_i = input('Ingresar dato '+str(dato)+' : ')
    lista_datos.append(datos_i)

fichero = open('datos_pickle','wb')
pickle.dump(lista_datos, fichero)
fichero.close()