try:
    print("1 : suma")
    print("2 : resta")
    print("3 : multiplicacion")
    print("4 : division")
    
    op = int(input("Que operacion desea realizar (1, 2, 3 o 4): "))

    if op not in [1, 2, 3, 4]:
        raise ValueError("Opcion invalida. Debe ser 1, 2, 3 o 4.")

    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))

    resultado = 0

    if op == 1:
        resultado = num1 + num2
    elif op == 2:
        resultado = num1 - num2
    elif op == 3:
        resultado = num1 * num2
    elif op == 4:
        if num2 == 0:
            raise ZeroDivisionError("No se puede dividir por cero.")
        resultado = num1 / num2

    print(resultado)

except ValueError as error:
    print("Error de valor:", error)
except ZeroDivisionError as error:
    print("Error de division:", error)
except Exception as error:
    print("error inesperado:", error)

#Este programa funciona como una calculadora simple. 
#Primero, le muestra al usuario un menú con cuatro operaciones (suma, resta, multiplicación y división). 
# Luego, el usuario escribe qué operación quiere hacer (1, 2, 3 o 4) y también ingresa dos números.

#Dependiendo de la opción que elija, el programa hace la operación correspondiente con los dos números y muestra el resultado. 
# En el caso de la división, se asegura de que el segundo número no sea cero para evitar errores.