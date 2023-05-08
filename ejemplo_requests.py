import requests
import json
from datetime import datetime

# Módulo REQUESTS
# Ejemplo utilizando la API de Open Notify http://api.open-notify.org/
response = requests.get("http://api.open-notify.org/astros.json")
# print(response.status_code)
#
# def json_astros(obj):
#     texto = json.dumps(obj, sort_keys=True, indent=4)
#     print(texto)
# json_astros(response.json())

# Obtener datos de iss-now.json
respuesta = requests.get("http://api.open-notify.org/iss-now.json")
print(respuesta.status_code)
def json_print(objeto):
    texto = json.dumps(objeto, sort_keys=True, indent=4)
    print(texto)
json_print(respuesta.json())

fecha_unix = respuesta.json()["timestamp"]
json_print(f'Fecha formato Unix: {fecha_unix}')
fecha = datetime.fromtimestamp(fecha_unix)
json_print(f'Fecha formato normal: {fecha}')
