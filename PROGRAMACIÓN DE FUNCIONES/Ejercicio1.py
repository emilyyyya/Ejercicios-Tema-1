def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo a partir de su base y altura.

    Args:
    base (float): La longitud de la base del rectángulo.
    altura (float): La altura del rectángulo.

    Returns:
    float: El área del rectángulo.
    """
    return base * altura

# Solicitar al usuario que ingrese la base y la altura del rectángulo
base = float(input("Ingresa la base del rectángulo: "))
altura = float(input("Ingresa la altura del rectángulo: "))

# Calcular el área del rectángulo
area = area_rectangulo(base, altura)

# Mostrar el área del rectángulo
print("El área del rectángulo con base {} y altura {} es: {}".format(base, altura, area))
