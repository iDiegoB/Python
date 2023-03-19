lenguajes = ['Python', 'Kotlin', 'Java', 'Javascript']

print(lenguajes)
for i in range(len(lenguajes)):#recorrer un arreglo
    lenguajes[i] = lenguajes[i].upper()
for i in range(len(lenguajes)):
    print(lenguajes[i].lower())
lenguajes.sort()#ordenar un arreglo

#modificar valores de un arreglo
lenguajes[2] = 'PHP'
print(lenguajes)

#agregar elemento a un arreglo
lenguajes.append('Ruby')
print(lenguajes)

#eliminar elemento de un arreglo

del lenguajes[1]
print(lenguajes)

#eliminar de un arreglo
lenguajes.pop()#ultimo elemento
print(lenguajes)

lenguajes.pop(0)#eliminar por posicion
print(lenguajes)

#eliminar por nombre
lenguajes.remove('PHP')
print(lenguajes)