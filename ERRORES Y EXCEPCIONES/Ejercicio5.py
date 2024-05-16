def agregar_una_vez(lista, el):
    """
    Añade un elemento a una lista si no está repetido.

    Args:
    lista (list): La lista a la cual se añadirá el elemento.
    el: El elemento a añadir.

    Raises:
    ValueError: Si el elemento ya está presente en la lista.

    Returns:
    list: La lista actualizada.
    """
    try:
        if el in lista:
            raise ValueError("Imposible añadir elementos duplicados => {}".format(el))
        else:
            lista.append(el)
    except ValueError as error:
        print("Error:", error)

# Crear una lista vacía
lista = []

# Añadir elementos a la lista
agregar_una_vez(lista, 10)
agregar_una_vez(lista, -2)
agregar_una_vez(lista, "Hola")
agregar_una_vez(lista, 10)  # Este intento fallará debido a un elemento duplicado

# Mostrar el contenido de la lista
print("Contenido de la lista:", lista)
