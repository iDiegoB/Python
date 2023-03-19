playlist = {}#Diccionario vacio
playlist['canciones'] = []#Lista vacia de canciones


#funcion principal
def app():
    #agregar playlist
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('¿Cómo deseas nombrar la playlist? ')
    
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
        
            #ya tenemos nombre, desactivar true
            agregar_playlist = False
            
            #Mandar llamar la función para agregar canciones
            agregar_canciones()


def agregar_canciones():
    print('Agregar canciones...')
    #Bandera para agregar canciones
    agregar_cancion = True
    while agregar_cancion:
        #Preguntar al usuario que cancion desea agregar
        nombre_playlist = playlist['nombre']
        pregunta = f'''Agrega canciones para la playlist: {nombre_playlist}
Escribe "X" para dejar de agregar canciones
'''
        cancion = input(pregunta)
        
        if cancion == 'X' or cancion == 'x':
            #Dejar de agregar canciones
            agregar_cancion = False
            
            
            #Mostrar resumen
            mostrar_resumen()
        else:
            #Agregar las canciones a la playlist
            playlist['canciones'].append(cancion)
            print(playlist)
    
def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'''Playlist: {nombre_playlist}
Canciones: ''')
    for cancion in playlist['canciones']:
        print(cancion)
app()