import os

CARPETA = 'contactos/'#Carpeta donde se encuentran los archivos
EXTENSION = '.txt'#Extension del archivo

#Contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria
        

def app():
    #Revisa si la carpeta existe
    crear_directorio()
    
    #Preguntar al usuario la accion a realizar
    
    preguntar = True
    while preguntar:
        #Muestra el menu de opciones
        mostrar_menu()
        opcion = int(input('Seleccione una opción: '))
        #Ejecutar las opciones correspondientes
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            print('Ver contactos')
            preguntar = False
        elif opcion == 4:
            print('Buscar contacto')
            preguntar = False
        elif opcion == 5:
            print('Eliminar contacto')
            preguntar = False
        else:
            print('Opción no válida')

def crear_directorio():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)#Crea la carpeta donde se almacenará los contactos
    #else:
    #    print('La carpeta ya existe')

def mostrar_menu():
    print(f'''Seleccione una opción:
1. Crear un nuevo contacto
2. Editar un contacto
3. ver contactos
4. buscar un contacto
5. Eliminar un contacto''')


def existe_contacto(nombre_contacto):
    #Revisar si el archivo existe
    return os.path.isfile(CARPETA + nombre_contacto + EXTENSION)


def agregar_contacto():
    print('Agregar contacto')
    nombre_contacto = input("Nombre del contacto: ")
    
    #Revisar si el archivo existe
    existe = existe_contacto(nombre_contacto)
    
    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, "w") as archivo:
            #Resto de los campos
            telefono_contacto = input('Agregar telefono: ')
            categoria_contacto = input('Agregar categoria: ')
            #Intanciar la clase de contacto
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            #Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\n')
            archivo.write('telefono: ' + contacto.telefono + '\n')
            archivo.write('categoria: ' + contacto.categoria + '\n')
            #Mostrar mensaje de exito
            print('Contacto agregado correctamente')
    else:
        print('Ese contacto ya existe')
  
    #Reiniciar el programa
    app()
    
    
def editar_contacto():
    print('Escribir nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar: ')
    #Revisar si el archivo existe
    existe = existe_contacto(nombre_anterior)
    if existe:
         with open(CARPETA + nombre_anterior + EXTENSION, "w") as archivo:
             #Resto de los campos
              nombre_contacto = input("Nuevo nombre: ")
              telefono_contacto = input('Agregar nuevo telefono: ')
              categoria_contacto = input('Agregar nueva categoria: ')
              contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
              archivo.write('Nombre: ' + contacto.nombre + '\n')
              archivo.write('telefono: ' + contacto.telefono + '\n')
              archivo.write('categoria: ' + contacto.categoria + '\n')
              #Renombrar el archivo
              os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
              #Mostrar mensaje de exito
         print('Contacto editado correctamente')
    else:
        print('El contacto no existe')
    #Reiniciar el programa    
    app()

#Iniciar el programa
app()