import requests
import matplotlib.pyplot as plt

api_key = "33f8a5645d6c546cbf65483583c7149a"
ciudad = "Monterrey"

def obtener_pronostico_grafica(ciudad, api_key):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={ciudad}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        datos_pronostico = response.json()
        
        pronostico_dia = {}
            
        for pronostico_hora in datos_pronostico["list"]:
            fecha = pronostico_hora["dt_txt"].split()[0]
            
            if fecha not in pronostico_dia:
                temperaturas = []
                pronostico_dia[fecha] = [temperaturas]

            temperatura = round(pronostico_hora["main"]["temp"] - 273.15)
            pronostico_dia[fecha][0].append(temperatura)
            
        return pronostico_dia

def mostrar_grafica(datos_pronostico, fecha):
    if fecha in datos_pronostico:
        temperaturas = datos_pronostico[fecha][0]
        horas = [h for h in range(len(temperaturas))]

        plt.figure(figsize=(10, 6))
        plt.plot(horas, temperaturas, marker='o')
        plt.title(f'Temperaturas Pronosticadas para {fecha}')
        plt.xlabel('Horas')
        plt.ylabel('Temperatura (°C)')
        plt.xticks(horas, [f'{h}:00' for h in range(len(temperaturas))])
        plt.yticks(range(min(temperaturas), max(temperaturas) + 1))
        plt.grid(True)
        plt.ylim(min(temperaturas) - 1, max(temperaturas) + 1)
        plt.tight_layout()
        plt.show()

def datos_pronostico(datos_pronostico):
    if datos_pronostico:
        fechas_disponibles = list(datos_pronostico.keys())
        print("Fechas disponibles para visualizar el pronóstico:")
        for idx, fecha in enumerate(fechas_disponibles, start=1):
            print(f"{idx}. {fecha}")
    
        opcion = int(input("Ingrese el número de la fecha que desea visualizar: "))
    
        if opcion > 0 and opcion <= len(fechas_disponibles):
            fecha_seleccionada = fechas_disponibles[opcion - 1]
            mostrar_grafica(datos_pronostico, fecha_seleccionada)
        else:
            print("Opción inválida. Ingrese un número válido correspondiente a la fecha.")

