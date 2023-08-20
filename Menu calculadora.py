"""Leer dos números, pregunte al usuario que tipo de operación desea realizar:

Suma, resta, multiplicación o división

Verificar un divisor valido

Mostrar ¿cuantas rondas se realizaron?, ¿cuantas fueron operaciones reales?

Al finalizar la operación, preguntar al usuario si desea realizar una nueva operación """

num1 = 0
num2 = 0

opc = 0

total = 0

res = 0 

contR = 0 #Contador de operaciones reales
contF = 0 #Contador de operaciones falsas

controlador = True

print("Menu calculadora")

while controlador:
    print("\nOpcion 1: Suma \nOpcion 2: Resta \nOpcion 3: Multiplicacion \nOpcion 4: Division")

    opc = int(input("\nIngrese el numero, para la operacion que desea realizar: "))

    num1 = float(input("\nFavor ingresar el primer numero: "))
    num2 = float(input("Favor ingresar el segundo numero: "))
    print()

    if opc == 1:
        print("\nLa opcion elegida es suma")
        total = num1 + num2
        print("El total es {}".format(total))
        contR += 1
    elif opc == 2:
        print("\nLa opcion elegida es resta")
        total = num1 - num2
        print("El total es {}".format(total))
        contR += 1
    elif opc == 3:
        print("\nLa opcion elegida es multiplicacion")
        total = num1 * num2
        print("El total es {}".format(total))
        contR += 1
    elif opc == 4:
        print("\nLa opcion elegida es division")
        while num2 == 0:
            print("\nPara la operacion division debe ingresar otra vez el segundo numero disntito a CERO")
            num2 = float(input("Ingrese nuevo valor del segundo numero: "))
        print("Valor nuevo aceptado")
        total = num1 / num2
        print("El total es {}".format(total))
        contR += 1
    else:
        print("Ha ingresado un valor invalido, operacion invalida")
        contF += 1
    
    res = input("\n Opcion Si: s \n Opcion No: n \n¿Desea realizar otra operacion?: ")
    
    while res != "s" and res != "n":
        print("Respuesta invalida, intente de nuevo")
        res = input("\n Opcion Si: s \n Opcion No: n \n¿Desea realizar otra operacion?: ")

    if res == "s":
        print("De vuelta al menu")
    elif res == "n":
        controlador = False
        print("Fin del programa")
    


print("\nNumero de operaciones reales y falsas")

print("\nNumero de operaciones reales: {}".format(contR))
print("Numero de operaciones falsas: {}".format(contF))

print("\nTotal de rondas:",contR + contF)