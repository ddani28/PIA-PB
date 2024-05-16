def guardar_clima_actual(ciudad, datos):
    try:
        nombre_archivo = "consulta_"+ciudad+".txt"
        with open(nombre_archivo, 'w') as archivo:
            contenido = "Clima actual de "+ciudad.upper()+"\n"
            contenido += "Temperatura actual:"+str(datos[0])+"\n"
            contenido += f"Condiciones:"+datos[1]+"\n"
            contenido += "Max.:"+str(datos[2])+"Min.:"+str(datos[3])

            archivo.write(contenido)
    except IOError as e:
        print("Error al guardar el archivo")

