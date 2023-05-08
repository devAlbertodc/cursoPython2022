from sqlalchemy.orm import sessionmaker
from sql_tablas_alchemy import Estudiante, engine

#Crear sesion:
Session = sessionmaker(bind=engine, echo=True, future=True)
session = Session()

# Crea las instancias
usuario = Estudiante("juan", "Juan", "Perez", "Lopez", "Complutense")
session.add(usuario)

usuario = Estudiante("Maria", "María", "García", "Gomez", "UPC")
session.add(usuario)

usuario = Estudiante("Beatriz", "Beatriz", "Suarez", "Gonzalez", "Carlos III")
session.add(usuario)

# commit a la base de datos
session.commit()
session.close()