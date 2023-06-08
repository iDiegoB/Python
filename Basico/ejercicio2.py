op=0
monto_total=0
cont=0

while op!=3:
    print("MENU\n",
        "1.-ingrese su monto a depositar\n",
        "2.-Consultar saldo\n",
        "3.-salir\n")
    op = int(input("ingrese su opcion: "))
    if op==1:
        monto=int(input("ingrese su monto: "))
        monto_total+=monto
        cont+=1
    elif op==2:
        print("su saldo es: ",monto_total)
        print("cantidad de veces que ingreso dinero: ", cont,"\n")
    else:
        print("ingrese opcion valida")
print("saliendo...")
