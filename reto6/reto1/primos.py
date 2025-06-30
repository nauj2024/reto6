try:
    entrada = input("Ingrese numeros separados por espacio: ")
    
    if not entrada.strip():
        raise ValueError("No se ingresaron numeros.")

    lista = list(map(int, entrada.split()))
    listareturn = []

    for n in lista:
        if n < 2:
            continue
        raiz = int(n**0.5)
        for i in range(2, raiz + 1):
            if n % i == 0:
                break
        else:
            listareturn.append(n)

    print(listareturn)

except ValueError as error:
    print("Error de valor:", error)
except Exception as error:
    print("error inesperado:", error)
# El programa pide varios numeros y muestra cuales son primos.
# Convierte lo que se escribe en una lista de numeros.

# Recorre la lista de numeros:
# - Si es menor que 2, lo salta porque no puede ser primo.
# - Revisa si tiene divisores desde el 2 hasta su raiz cuadrada.
# - Si encuentra un divisor, no es primo.
# - Si no encuentra ningun divisor, lo guarda como primo.

# Al final muestra solo los numeros primos.