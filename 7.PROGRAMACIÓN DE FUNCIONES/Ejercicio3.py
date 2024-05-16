def relacion(a, b):
    """
    Determina la relación entre dos números.

    Args:
    a (float): El primer número.
    b (float): El segundo número.

    Returns:
    int: 1 si a > b, -1 si a < b, 0 si a == b.
    """
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

# Comprobar la relación entre los números 5 y 10
resultado_1 = relacion(5, 10)
print("Relación entre 5 y 10:", resultado_1)

# Comprobar la relación entre los números 10 y 5
resultado_2 = relacion(10, 5)
print("Relación entre 10 y 5:", resultado_2)

# Comprobar la relación entre los números 5 y 5
resultado_3 = relacion(5, 5)
print("Relación entre 5 y 5:", resultado_3)
