def separar(lista):
    """
    Separa una lista de números enteros en dos listas ordenadas, una con los números pares y otra con los impares.

    Args:
    lista (list): La lista de números enteros.

    Returns:
    tuple: Una tupla con dos listas, una de números pares y otra de números impares.
    """
    pares = []
    impares = []
    
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    
    pares.sort()
    impares.sort()
    
    return pares, impares

# Solicitar al usuario que ingrese los números separados por comas
numeros = input("Ingresa los números separados por comas: ")

# Convertir los números ingresados a una lista de enteros
numeros_lista = [int(numero) for numero in numeros.split(',')]

# Obtener las listas separadas de pares e impares
pares, impares = separar(numeros_lista)

# Mostrar los números pares e impares
print("Números pares:", pares)
print("Números impares:", impares)
