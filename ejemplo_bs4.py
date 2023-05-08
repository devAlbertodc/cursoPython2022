from bs4 import BeautifulSoup
import requests

#fortinux.com
url = input("Escribe la URL del sitio web: ")
agrega_http = requests.get('http://' + url)
datos = agrega_http.text

soup = BeautifulSoup(datos, features="html5lib")

for enlace in soup.find_all('a'):
    print(enlace.get('href'))