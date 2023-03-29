import os

CARPETA = 'contactos/'  # Carpeta donde se encuentran los archivos
EXTENSION = '.txt'  # Extension del archivo

# Contactos


class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria


def app():
    # ! Revisa si la carpeta existe
    crear_directorio()

    # Preguntar al usuario la accion a realizar

    preguntar = True
    while preguntar:
        # Muestra el menu de opciones
        mostrar_menu()
        opcion = int(input('\nSeleccione su opción: '))
        # Ejecutar las opciones correspondientes
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        elif opcion == 6:
            preguntar = False
        else:
            print('Opción no válida')


def crear_directorio():
    if not os.path.exists(CARPETA):
        # !Crea la carpeta donde se almacenará los contactos
        os.makedirs(CARPETA)
    # else:
    #    print('La carpeta ya existe')


def mostrar_menu():
    print(f'''Seleccione una opción:
1. Crear un nuevo contacto
2. Editar un contacto
3. ver contactos
4. buscar un contacto
5. Eliminar un contacto
6. Salir de la app''')


def existe_contacto(nombre_contacto):
    # !Revisar si el archivo existe
    return os.path.isfile(CARPETA + nombre_contacto + EXTENSION)


def agregar_contacto():
    print('\nAgregar contacto')
    nombre_contacto = input("Nombre del contacto: ")

    # Revisar si el archivo existe
    existe = existe_contacto(nombre_contacto)

    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, "w") as archivo:
            # Resto de los campos
            telefono_contacto = input('Agregar telefono: ')
            categoria_contacto = input('Agregar categoria: ')
            # Intanciar la clase de contacto
            contacto = Contacto(
                nombre_contacto, telefono_contacto, categoria_contacto)
            # Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\n')
            archivo.write('telefono: ' + contacto.telefono + '\n')
            archivo.write('categoria: ' + contacto.categoria + '\n')
            # Mostrar mensaje de exito
            print('Contacto agregado correctamente\n')
    else:
        print('Ese contacto ya existe\n')

    # Reiniciar el programa
    app()


def editar_contacto():
    print('Escribir nombre del contacto a editar\n')
    nombre_anterior = input('Nombre del contacto que desea editar: ')
    # Revisar si el archivo existe
    existe = existe_contacto(nombre_anterior)
    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, "w") as archivo:
            # Resto de los campos
            nombre_contacto = input("Nuevo nombre: ")
            telefono_contacto = input('Agregar nuevo telefono: ')
            categoria_contacto = input('Agregar nueva categoria: ')
            contacto = Contacto(
                nombre_contacto, telefono_contacto, categoria_contacto)
            archivo.write('Nombre: ' + contacto.nombre + '\n')
            archivo.write('telefono: ' + contacto.telefono + '\n')
            archivo.write('categoria: ' + contacto.categoria + '\n')
        # Renombrar el archivo
        os.rename(CARPETA + nombre_anterior + EXTENSION,
                  CARPETA + nombre_contacto + EXTENSION)
        # Mostrar mensaje de exito
        print('Contacto editado correctamente\n')
    else:
        print('El contacto no existe\n')
    # Reiniciar el programa
    app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    
    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                # !Imprime contenidos
                print(linea.rstrip())
            #imprime un separador entre contactos
            print('\r\n')
    app()
def buscar_contacto():
    nombre = input('Seleccione el contacto que desea buscar: ')
    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\nInformacion del contacto: ')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe\r\n')
     # Reiniciar el programa
    app()

def eliminar_contacto():
     nombre = input('Seleccione el contacto que desea eliminar: ')
     try:
         os.remove(CARPETA + nombre + EXTENSION)
         print('Eliminado Correctamente\n')
     except:
         print('No existe ese contacto\n')
     app()
# Iniciar el programa
app()
