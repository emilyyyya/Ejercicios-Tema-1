import sys

# Verifica si se proporciona un argumento
if len(sys.argv) != 2:
    print("Uso: python descomposicion.py [numero]")
    sys.exit(1)

# Convierte el argumento a un número entero
try:
    numero = int(sys.argv[1])
except ValueError:
    print("El argumento debe ser un número entero positivo.")
    sys.exit(1)

# Verifica si el número es positivo
if numero <= 0:
    print("El número debe ser positivo.")
    sys.exit(1)

# Convierte el número a cadena y obtiene su longitud
numero_str = str(numero)
longitud = len(numero_str)

# Itera sobre los dígitos del número de derecha a izquierda
for i in range(longitud):
    # Obtiene el dígito actual
    digito = int(numero_str[longitud - i - 1])
    # Calcula el valor descompuesto multiplicando el dígito por 10 elevado a la posición
    valor_descompuesto = digito * (10 ** i)
    # Imprime el valor descompuesto rellenado con ceros a la izquierda
    print("{:04d}".format(valor_descompuesto))
