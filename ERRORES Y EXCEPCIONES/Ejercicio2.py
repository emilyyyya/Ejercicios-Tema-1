lista = [1, 2, 3, 4, 5]

try:
    elemento = lista[10]
except IndexError:
    print("Error: Índice fuera de rango. El índice proporcionado excede la longitud de la lista.")
