num = 1
controlador = True #Controlador de tipo booleano

while controlador == True: #No es necesario asignarle una condicion, dado que ya detecta que es true
    print("\nOpcion 1: Agregar \nOpcion 2: Consulta de saldo \nOpcion 3: Codigo SMS \nOpcion 4: Salir")
    num = int(input("Favor ingresar otro numero deseado: "))
    print()
    if num == 1:
        print("Opcion elegida: Agregar ")
    elif num == 2:
        print("Opcion elegida: Consulta de saldo ")
    elif num == 3:
        print("Opcion elegida: Codigo SMS")
    elif num == 4:
        print("Opcion elegida: Salir")
        controlador = False #Una vez que se elige esta opcion, al controlador se le asigna el valor
                            #falso, por lo que cuando vuelve a repetir el ciclo de while, ya no 
                            #cumple con la condicion de controlador == True, por lo que el programa
                            #termina.
    else:
        print("Opcion equivocada intente otra vez")

