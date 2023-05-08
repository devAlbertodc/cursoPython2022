import sqlite3

# Establecer conexion:
connection = sqlite3.connect('ejemplo.sqlite')

# Establecer acceso:
cursor = connection.cursor()

# Ejecutar la sentencia SQL y mostrar resultados:
cursor_object = cursor.execute("SELECT * FROM ejemplo")
print(cursor_object.fetchall())

# Cierre de conexión:
connection.close()
