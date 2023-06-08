def app():
    validar()


def menu():
    print(f'''
MENU:
1. cuadrado
2. triangulo
3. rectangulo
4. salir''')
    op = int(input("ingrese su opcion: "))
    return op
def validar():
    try:
        op=0
        while op!=4:
            op = menu()
            if op==1:
                lado1 = int(input("ingrese primer lado: "))
                print("Perimetro del cuadrado: ",perimetro_cuadrado(lado1))
                print("area del cuadrado: ",area_cuadrado(lado1))
            elif op==2:
                lado1 = int(input("ingrese primer lado: "))
                lado2 = int(input("ingrese segundo lado: "))
                lado3 = int(input("ingrese segu lado: "))
                altura = int(input("ingrese la altura del triangulo: "))
                base = int(input("ingrese la base del triangulo: "))
                print("Perimetro del triangulo: ",perimetro_triangulo(lado1,lado2,lado3))
                print("area del triangulo: ",area_triangulo(altura,base))
            elif op==3:
                lado1 = int(input("ingrese primer lado: "))
                lado2 = int(input("ingrese segundo lado: "))
                print("Perimetro del rectangulo: ",perimetro_rectangulo(lado1,lado2))
                print("area del rectangulo: ",area_rectangulo(lado1,lado2))
            elif op==4:
                print("saliendo...")
            else: 
                print("opcion no valida")
    except:
        print("error")
def perimetro_triangulo(lado1,lado2,lado3):
    return lado1+lado2+lado3
def perimetro_cuadrado(lado1):
    return lado1*4
def perimetro_rectangulo(lado1,lado2):
    return (lado1*2)+(lado2*2)

def area_triangulo(altura,base):
    return altura*base
def area_cuadrado(lado1):
    return lado1*lado1
def area_rectangulo(lado1,lado2):
    return (lado1*lado2)

app()