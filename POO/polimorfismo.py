class Restaurant:
    # Constructor
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre  # Atributo
        self.categoria = categoria
        # Default: Public, PROTECTED: _x Puede ser modificado en la misma clase, PRIVATE: __x
        self.precio = precio

    def mostrar_informacion(self):
        print(
            f'Nombre: {self.nombre}, Categoria: {self.categoria}, precio: {self.precio}')

    # GETTERS Y SETTERS - Get = Obtiene un valor, SET = Agrega un valor

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio


# Crear una clase hijo de restaurant
# HERENCIA
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, alberca):
        # Referencia clase padre
        super().__init__(nombre, categoria, precio)
        self.alberca = alberca
    #Reescribir un METODO (DEBE LLAMARSE IGUAL)        
    def mostrar_informacion(self):
        print(
            f'Nombre: {self.nombre}, Categoria: {self.categoria}, precio: {self.precio}, alberca: {self.alberca}')

    
    #Agregar metodo que solo exista en hotel
    def get_alberca(self):
        return self.alberca


hotel = Hotel('Hotel POO', '5 Estrellas', 200, 'Si')
hotel.mostrar_informacion()
alberca = hotel.get_alberca()
print(alberca)

