def app():
    op="no"
    while op=="no":
        validar()
        op = input("desea salir del programa? si/no: ")
    
def pedir_numero():
    return int(input("ingrese su numero: "))

def validar():
    try:
        num = pedir_numero()
        if num>10 and num<100:
            a(num)
            b(num)
        else:
            print("numero no esta entre 10 y 100")
    except:
        print("error")
        
def a(num):
   for x in range(num,100):
            if x%2!=0:
                print("numero impar: ", x)
def b(num):
    for x in range(num,50):
            if x%3==0 and x%5==0:
                print("numero divisible por 3 y 5:", x)       
      
app()