
num = 1

while num > 0 and num < 5:
    print("\nOpcion 1: Agregar \nOpcion 2: Consulta de saldo \nOpcion 3: Codigo SMS \nOpcion 4: Salir")
    num = int(input("Favor ingresar otro numero deseado: "))
    print()
    if num == 1:
        print("Opcion elegida: Agregar ")
    elif num == 2:
        print("Opcion elegida: Consulta de saldo ")
    elif num == 3:
        print("Opcion elegida: Codigo SMS")
    else:
        print("Opcion elegida: Salir")
        num = 10 #Ejemplo de controlador burdo, porque es la misma variable que controla la estructura
