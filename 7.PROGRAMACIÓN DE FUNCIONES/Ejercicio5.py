def recortar(numero, minimo, maximo):
    """
    Recorta un número dentro de un rango especificado.

    Args:
    numero (float): El número a recortar.
    minimo (float): El límite inferior.
    maximo (float): El límite superior.

    Returns:
    float: El número recortado dentro del rango especificado.
    """
    if numero < minimo:
        return minimo
    elif numero > maximo:
        return maximo
    else:
        return numero

# Solicitar al usuario que ingrese el número, el límite inferior y el límite superior
numero = float(input("Ingresa un número: "))
minimo = float(input("Ingresa el límite inferior: "))
maximo = float(input("Ingresa el límite superior: "))

# Calcular el número recortado dentro del rango especificado
numero_recortado = recortar(numero, minimo, maximo)

# Mostrar el número recortado
print("El valor recortado entre {} y {} es: {}".format(minimo, maximo, numero_recortado))
