from matplotlib.font_manager import json_dump
import requests
from statistics import mean, mode
import json

def obtener_clima_actual(ciudad, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        datos_clima = response.json()
        temperatura_actual = datos_clima["main"]["temp"]
        condiciones_actuales = datos_clima["weather"][0]["description"]
        temp_min = datos_clima["main"]["temp_min"]
        temp_max = datos_clima["main"]["temp_max"]
        presion = datos_clima["main"]["pressure"]
        humedad = datos_clima["main"]["humidity"]
        velocidad_viento = datos_clima["wind"]["speed"]
        cobertura_nubes = datos_clima["clouds"]["all"]
        salida_sol = datos_clima["sys"]["sunrise"]
        puesta_sol = datos_clima["sys"]["sunset"]

        return (temperatura_actual, condiciones_actuales, temp_min, temp_max, presion, humedad,
                velocidad_viento,cobertura_nubes,
                salida_sol, puesta_sol)
    else:
        print(f'Error al obtener datos del clima para {ciudad}. Código de estado: {response.status_code}')

def obtener_pronostico(ciudad, api_key):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={ciudad}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        datos_pronostico = response.json()
        pronostico_dia = {}   
        for pronostico_hora in datos_pronostico["list"]:
            fecha = pronostico_hora["dt_txt"].split()[0]  # Obtener solo la parte de la fecha (sin la hora)
            
            if fecha not in pronostico_dia:
                pronostico_dia[fecha] = {"temperaturas": [], "condiciones": []}

            temperatura = pronostico_hora["main"]["temp"]
            condiciones = pronostico_hora["weather"][0]["description"]
            pronostico_dia[fecha]["temperaturas"].append(temperatura)
            pronostico_dia[fecha]["condiciones"].append(condiciones)

        for fecha, datos_dia in pronostico_dia.items():
            temperaturas = datos_dia["temperaturas"]
            condiciones = datos_dia["condiciones"]
            
            promedio_temperatura = mean(temperaturas)
            moda_condiciones = mode(condiciones)

            pronostico_dia[fecha]["promedio_temperatura"] = promedio_temperatura
            pronostico_dia[fecha]["moda_condiciones"] = moda_condiciones
           
        return json.dumps(pronostico_dia)
    else:
        print(f'Error al obtener el pronóstico para {ciudad}. Código de estado: {response.status_code}')