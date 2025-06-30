try:
    entrada = input("Ingrese al menos dos numeros separados por espacio: ")

    if not entrada.strip():
        raise ValueError("no se ingreso ningun numero.")

    lista = list(map(int, entrada.split()))

    if len(lista) < 2:
        raise ValueError("ingresar al menos dos numeros para calcular sumas consecutivas.")

    mayor_suma = lista[0] + lista[1]

    for i in range(1, len(lista) - 1):
        suma = lista[i] + lista[i + 1]
        if suma > mayor_suma:
            mayor_suma = suma

    print(mayor_suma)

except ValueError as e:
    print("Error de valor:", e)
except Exception as e:
    print("Ocurrio un error inesperado:", e)
# El programa recibe una lista de numeros.
# Luego revisa la suma de cada par de numeros que estan uno al lado del otro.
# Va guardando la mayor de todas esas sumas.
# Al final, muestra cual fue la mayor suma encontrada.