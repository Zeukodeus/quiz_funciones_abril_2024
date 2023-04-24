def ultimo_digito_es_cuatro(x):
    if x % 10 == 4:
        print("El número finaliza en 4")
        return True
    else:
        print("El número no finaliza en 4")
        return False

x = int(input("Ingrese un número: "))
ultimo_digito_es_cuatro(x)