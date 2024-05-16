from Modulos.crear_un_texto import consulta_local, consulta_online
from Modulos.funciones_archivos import guardar_clima_actual
from Modulos.funciones_clima import obtener_clima_actual, obtener_pronostico
from Graficas.grafica_dia1 import datos_pronostico, obtener_pronostico_grafica
from Graficas.grafica_excel import graficar_excel


def main():
    api_key = '33f8a5645d6c546cbf65483583c7149a'
    ciudad = input('Ingrese una ciudad: ')

    while True:
        print("Consulta del clima de",ciudad,":")
        print("1. Clima actual")
        print("2. Pronóstico semanal")
        print("3. Graficas de los dias de la semana")
        print("4. Guardar clima actual en archivo de texto")
        print("5. Graficar datos en excel")
        print("6. Consulta de datos en txt")
        print("7. Salir")


        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            clima = obtener_clima_actual(ciudad, api_key)
            print(clima)
        elif opcion == '2':
            pronostico = obtener_pronostico(ciudad, api_key)
            print(pronostico)
        elif opcion == '3':
          datos_pronostico_dic = obtener_pronostico_grafica(ciudad,api_key)
          datos_pronostico(datos_pronostico_dic)
        elif opcion == '4':
            datos = obtener_clima_actual(ciudad, api_key)
            guardar_clima_actual(ciudad,datos)
        elif opcion == '5':
            pais = input('Ingrese el pais: ')
            graficar_excel(ciudad,pais)
        elif opcion == '6':
            lat = 44.34
            lon=10.99
            consulta_online(lat, lon, api_key)
            print(consulta_local()) 
        elif opcion == '7':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")

if __name__ == "__main__":
    main()
