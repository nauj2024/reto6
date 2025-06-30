try:
    word = input("Ingrese una palabra: ")

    if not word:
        raise ValueError("No se ingreso ninguna palabra.")

    conjuntoword = []

    for letra in word:
        conjuntoword.append(letra)

    conjuntoreverse = list(reversed(conjuntoword))

    if conjuntoreverse == conjuntoword:
        print("es palindromo")
    else:
        print("no es palindromo")

except ValueError as error:
    print(f"Error: {error}")
except Exception as error:
    print(f"error inesperado: {error}")

#Para saber si una palabra es un palíndromo sin usar slicing, 
#primero convertí la palabra en una lista, agregando cada letra con un ciclo for. 
# Luego, usé reversed() para invertir esa lista sin modificar la original, y la convertí en una nueva lista con list(reversed(...)).

#Finalmente, comparé si la lista original es igual a la lista invertida. 
# Si son iguales, significa que la palabra se lee igual al derecho y al revés, por lo tanto es un palíndromo