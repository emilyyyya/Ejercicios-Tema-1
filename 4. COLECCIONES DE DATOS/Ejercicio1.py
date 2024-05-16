"""
This module contains functions related to user management.
"""

def imprimir_estado_usuario(usuario, administradores):
    """
    Print the state of a user.

    Args:
        usuario (str): The user to check.
        administradores (set): The set of administrators.

    Returns:
        None
    """
    if usuario in administradores:
        print(usuario, "es administrador")
    else:
        print(usuario, "no es administrador")

# Crear conjunto de usuarios
usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}

# Crear conjunto de administradores
administradores = {"Juan", "Marta"}

# Remover a Juan del conjunto de administradores
administradores.discard("Juan")

# Añadir a Marcos como nuevo administrador
administradores.add("Marcos")

# Mostrar el estado de cada usuario
for usuario in usuarios:
    imprimir_estado_usuario(usuario, administradores)
