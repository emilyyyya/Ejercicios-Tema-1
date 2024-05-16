import math

def area_circulo(radio):
    """
    Calcula el área de un círculo a partir de su radio.

    Args:
    radio (float): El radio del círculo.

    Returns:
    float: El área del círculo.
    """
    return math.pi * radio ** 2

# Solicitar al usuario que ingrese el radio del círculo
radio = float(input("Ingresa el radio del círculo: "))

# Calcular el área del círculo
area = area_circulo(radio)

# Mostrar el área del círculo
print("El área del círculo con radio {} es: {}".format(radio, area))
