class Restaurant:
    # Constructor
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre  # Atributo
        self.categoria = categoria
        # Default: Public, PROTECTED: _x Puede ser modificado en la misma clase, PRIVATE: __x
        self.__precio = precio

    def mostrar_informacion(self):
        print(
            f'Nombre: {self.nombre}, Categoria: {self.categoria}, precio: {self.__precio}')

    # GETTERS Y SETTERS - Get = Obtiene un valor, SET = Agrega un valor

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio


# Crear una clase hijo de restaurant
# HERENCIA
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio):
        # Referencia clase padre
        super().__init__(nombre, categoria, precio)


hotel = Hotel('Hotel POO', '5 Estrellas', 200)
hotel.mostrar_informacion()
