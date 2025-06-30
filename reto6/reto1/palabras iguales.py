try:
    palabras = input("Ingrese palabras separadas por espacio: ").split()

    if not palabras or len(palabras) < 2:
        raise ValueError("Debe ingresar al menos dos palabras para comparar.")

    resultado = []

    for i in range(len(palabras)):
        for j in range(i + 1, len(palabras)):
            palabra1 = palabras[i]
            palabra2 = palabras[j]

            if sorted(palabra1) == sorted(palabra2):
                if palabra1 not in resultado:
                    resultado.append(palabra1)
                if palabra2 not in resultado:
                    resultado.append(palabra2)

    print(resultado)

except ValueError as error:
    print(f"Error: {error}")
except Exception as error:
    print(f"error inesperado: {error}")
# El programa pide varias palabras.
# Compara cada palabra con las demas.
# Si tienen las mismas letras, las guarda en una lista.
# Al final muestra solo esas palabras que coinciden en letras.