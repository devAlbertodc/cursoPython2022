from sqlalchemy.orm import sessionmaker
from sql_tablas_alchemy import Estudiante, engine

#Crear sesion:
Session = sessionmaker(bind=engine)
session = Session()

#Obtener todos los estudiantes ordenados por su id:
#for estudiante1 in session.query(Estudiante).order_by(Estudiante.id):
#    print(estudiante1.nombre, estudiante1.apellido1, estudiante1.apellido2)


#Ejemplo filtrar base de datos
for Estudiante2 in session.query(Estudiante).filter(
    Estudiante.universidad == 'UPC').order_by(Estudiante.id):
    print(Estudiante2.nombre, Estudiante2.apellido1, Estudiante2.apellido2)

session.close()