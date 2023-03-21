class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre  # Atributo
        self.categoria = categoria
        # Default: Public, PROTECTED: _x Puede ser modificado en la misma clase, PRIVATE: __x
        self.__precio = precio

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, precio: {self.__precio}')

    # GETTERS Y SETTERS - Get = Obtiene un valor, SET = Agrega un valor

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio


# Instanciar la clase
restaurant = Restaurant('pizzeria', 'Comida italiana', 50)
restaurant.mostrar_informacion()
restaurant.set_precio(80)
precio = restaurant.get_precio()
print(precio)
restaurant2 = Restaurant('pizzeria2', 'Comida casual', 20)
restaurant2.mostrar_informacion()
restaurant2.set_precio(50)
precio2 = restaurant2.get_precio()
print(precio2)
