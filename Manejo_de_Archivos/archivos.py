def app():
    # Crear Archivo
    # w es escritura, si no existe lo creara
    archivo = open('archivo.txt', 'w')

    # Generar numeros en archivo
    for i in range(0, 20):
        archivo.write(f'Esta es la linea {str(i)} \r\n')
        
    # Cerrar el Archivo
    archivo.close()


app()
