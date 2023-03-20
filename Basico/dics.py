#Diccionario simple

cancion = {
    'artista' : 'Metallica', #llave y valor
    'cancion': 'Enter Sandman',
    'lanzamiento': 1992,
    'likes': 3000
}

#Acceder a elementos del diccionario
print(cancion['artista'])
print(cancion['lanzamiento'])

artista = cancion['artista']

print(f'Estoy escuchando {artista}')

#agregar nuevos valores
cancion['playlist'] = 'Heavy Metal'

#Reemplazar valor existente
cancion['cancion'] = 'Seek & Destroy'

print(cancion)

#eliminar un valor
del cancion['lanzamiento']
print(cancion)