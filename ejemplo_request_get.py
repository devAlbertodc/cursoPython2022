import requests

url = 'https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2021.zip'
request = requests.get(url)

fichero = url.split('/')[-1]

with open(fichero, 'wb') as ficheroSalida:
    ficheroSalida.write(request.content)