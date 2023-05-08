from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Para claves arenas y relaciones:
from sqlalchemy.orm import relationship, foreign

# Crear base de datos:
engine = create_engine("sqlite:///estudiantes.db", echo=True)
#Base es una clase de sqlalchemy:
Base = declarative_base()

class Estudiante(Base):
    __tablename__ = "estudiante"

    # Atributos de la clase:
    id = Column(Integer, primary_key=True)
    usuario = Column(String)
    nombre = Column(String)
    apellido1 = Column(String)
    apellido2 = Column(String)
    universidad = Column(String)

    # Constructor de la clase:
    def __init__(self, usuario, nombre, apellido1, apellido2, universidad):
        self.usuario = usuario
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.universidad = universidad

# Crear la tabla:
Base.metadata.create_all(engine)
