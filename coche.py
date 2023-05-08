#Fichero coche.py
# Ejemplo de clase
class Coche:
    def __init__(self, marca, modelo, tipo):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.capacidad_gasolina = 15
        self.nivel_gasolina = 0

    def gasolina_completo(self):
        self.nivel_gasolina = self.capacidad_gasolina
        print('El depósito de gasolina está lleno')

    def conducir(self):
        print(f'El {self.modelo} se está conduciendo.')

#Herencia: extendiendo la clase
class CocheElectrico(Coche):
    # El método __init__() para crear una clase hija
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo, tipo)
        self.tamanio_bateria = 100
        self.nivel_carga = 0

    # Agregar un nuevo método a la clase
    def cargar(self):
        self.nivel_carga = 100
        print('El coche está cargado.')

    # Sobrescribir un método del padre
    def gasolina_completo(self):
        print('El coche no tiene depósito de gasolina!')

# Creando las instancias de la clase Coche
objeto_coche = Coche('SEAT', 'Ateca', '1.0')

# Acceder a los atributos de ese objeto
print(objeto_coche.marca, objeto_coche.modelo, objeto_coche.tipo)

# Llamando a los métodos de la clase
objeto_coche.gasolina_completo()
objeto_coche.conducir()


#Usar el método padre e hijo
obj_coche_electrico = CocheElectrico('TESLA', 'Modelo 3', 'Berlina')
print(obj_coche_electrico.marca, obj_coche_electrico.modelo,
obj_coche_electrico.tipo)
obj_coche_electrico.cargar()
obj_coche_electrico.conducir()
# Usar el método sobreescrito
obj_coche_electrico.gasolina_completo()


print(isinstance(objeto_coche, Coche))
print(isinstance(obj_coche_electrico, Coche))
print(isinstance(objeto_coche, CocheElectrico))

#Saber si una subclase es un subclase de la clase:
print(issubclass(CocheElectrico, Coche))
print(issubclass(Coche, CocheElectrico))

print(CocheElectrico.__mro__)