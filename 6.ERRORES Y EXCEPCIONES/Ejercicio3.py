colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }

try:
    color = colores['blanco']
except KeyError:
    print("Error: Clave no encontrada. La clave proporcionada no existe en el diccionario.")
