import datetime
#from datetime import date

class FestivalMusical:
    #Pass permite que la clase este vacia y pueda ejecutar las siguientes instrucciones fuera de la clase:
    #pass

    #Constructor de la clase __init son metodos internos de python:
    def __init__(self, nombre, pais, estilo):
        self.nombre = nombre
        self.pais = pais
        self.estilo = estilo

    def festival_metodo(self):
        #print('El mejor festival es: ',self)
        return self

    @classmethod
    #Pasar objeto de clase y atributo:
    def valor_ticket(cls, valor):
        cls.valor_ticket = valor
        print("El valor del ticket es: ",valor)

    #Metodo estatico (no se puede acceder con un objeto de la clase, solo se accede con la Clase):
    @staticmethod
    def dia_evento(dia):
        if dia.weekday() == 5 or dia.weekday() == 6:
            print("Es un final de semana")
        else:
            print("Es un dia laborable")

festival1 = FestivalMusical('Benicassim','España','pop')
print(festival1.nombre, festival1.pais, festival1.estilo)
FestivalMusical.valor_ticket(180)

#dia_hoy = date.today()
dia_hoy = datetime.date(2022, 10, 22)
print(f'El festival {festival1.nombre} es hoy {dia_hoy}')
FestivalMusical.dia_evento(dia_hoy)
#print(festival1.festival_metodo())
#del festival1
print(FestivalMusical.festival_metodo(festival1.nombre))

#Pasar clase a diccionario:
print(festival1.__dict__)
#print(help(festival1))

print(FestivalMusical.valor_ticket)
print(festival1.valor_ticket)