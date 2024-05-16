import requests
import json

def consulta_online(lat,lon,api_key):
    try:
        apuntador = open('archivo_R.txt', 'w')

        URL = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}'
        response = requests.get(URL)
        if response.status_code == 200:
            datos = response.json()
            for dato in datos['list']:
                apuntador.write(json.dumps(dato) + '\n')
        else:
            print('Error en la solicitud',response.text)
        apuntador.close()
    except requests.exceptions.ConnectionError as e:
        print('Parece que no tienes internet :/')
        
def consulta_local():
    try:
        apuntador = open('archivo_R.txt', 'r')
        for linea in apuntador:
            print(linea.strip())
    except FileNotFoundError:
        print('El archivo no existe')