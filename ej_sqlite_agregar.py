import sqlite3

#Establecer conexion:
connection = sqlite3.connect('ejemplo.sqlite')

#Establecer acceso:
cursor = connection.cursor()

# Ejeccutar la sentencia SQL
cursor.execute("INSERT INTO ejemplo VALUES ('Carmen', 'Alicante', 456456456)")
cursor.execute("INSERT INTO ejemplo VALUES ('Juan', 'Zamora', 744522411)")

#Confirmación de cambios a la bbdd:
connection.commit()
connection.close()