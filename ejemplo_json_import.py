import json

with open('ejemplo_json.json') as fichero:
    datos = json.loads(fichero.read())
    print(datos)

print(datos['lenguajes'])

with open('ejemplo_json.txt', 'w') as fichero_exp:
    json.dump(datos, fichero_exp)