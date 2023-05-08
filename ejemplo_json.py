import json

# Ejemplo de diccionario
persona = {"nombre": "Juan", "lenguajes": ["Python", "Shellscripts"]}
print(persona, type(persona))

# Ejemplo de string en JSON
persona = '{"nombre": "Juan", "lenguajes": ["Python", "Shellscripts"]}'
print(persona, type(persona))

#Se convierte objeto string de persona a objeto JSON:
persona_dic = json.loads(persona)
#Acceder a un atributo del objeto Persona:
print(persona_dic['lenguajes'])
#La cadena de texto, tras pasarlo a JSO, ya se reconoce como diccionario:
print(type(persona_dic))

#Proceso inverso de JSON a string
persona_json = json.dumps(persona_dic)
print(persona_json, type(persona_json))