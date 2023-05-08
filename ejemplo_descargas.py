from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

zip_url = 'https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2021.zip'

with urlopen(zip_url) as zip_resp:
    with ZipFile(BytesIO(zip_resp.read())) as zfile:
        zfile.extractall('D:\\test\Python\\CursoPython\\descargaStackOverflow')

