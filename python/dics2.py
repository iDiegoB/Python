#Iniciar un Diccionario vacio
jugador = {}
print(jugador)

jugador ['nombre'] = 'diego'
jugador ['puntaje'] = 0
print(jugador)

#incrementando puntaje
jugador ['puntaje'] = 100
print(jugador)

#Acceder a un valor
print(jugador.get('consola', 'No existe ese valor'))

#Iterar en el diccionario
for llave, valor in jugador.items():
    print(llave, valor)
 
 
#Eliminar jugador y puntaje
del jugador['nombre']
del jugador['puntaje']
print(jugador)