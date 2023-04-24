def tabla(x):
    print("tabla del: ",x)
    for i in range(1,11):
        rta=x*i
        print(x, "x", i, "=", rta)

x=int(input("ingrese el numero que desea ver la tabla: "))
tabla(x)
