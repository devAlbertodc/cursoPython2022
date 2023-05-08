import sqlite3

#Establecer conexion:
connection = sqlite3.connect('ejemplo.sqlite')

#Establecer acceso:
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS ejemplo(nombre TEXT,ciudad TEXT, telefono INTEGER)')

#Confirmación de cambios a la bbdd:
connection.commit()
connection.close()