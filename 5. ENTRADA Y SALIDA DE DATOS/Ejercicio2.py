import sys

# Verifica si se proporcionan dos argumentos
if len(sys.argv) != 3:
    print("Uso: python tabla.py [filas] [columnas]")
    sys.exit(1)

# Convierte los argumentos a enteros
try:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])
except ValueError:
    print("Ambos argumentos deben ser números enteros.")
    sys.exit(1)

# Verifica si los números están en el rango permitido
if not (1 <= filas <= 9 and 1 <= columnas <= 9):
    print("Los números deben estar en el rango del 1 al 9.")
    sys.exit(1)

# Bucle para iterar sobre las filas
for i in range(filas):
    # Bucle para iterar sobre las columnas
    for j in range(columnas):
        # Imprime un asterisco sin salto de línea
        print(" * ", end='')
    # Después de imprimir una fila completa, añade un salto de línea
    print()

