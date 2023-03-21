
class Restaurant:
    def agregar_restaurant(self, nombre):
        self.nombre = nombre
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')

restaurant = Restaurant()
restaurant.agregar_restaurant('pizzeria')
restaurant.mostrar_informacion()


restaurant2 = Restaurant()
restaurant2.agregar_restaurant('pizzeria2')
restaurant2.mostrar_informacion()


#Mostrar informacion
print(f'Nombre Restauran: {restaurant.nombre}')
print(f'Nombre Restauran: {restaurant2.nombre}')
