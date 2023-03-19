def informacion():
    print('diego')


informacion()

# con parametros y argumentos


def informacion2(nombre, puesto='Sin Cargo'):
    print(f'soy {nombre} y soy {puesto}')


informacion2('diego', 'programador')
informacion2('felipe')
informacion2('jorge', 'constructor')

# funciones que retornan valores


def informacion3(nombre):
    return nombre


empleado = informacion3('diego')

print(empleado)

# metodos

print(empleado.upper())
print(empleado.title())
