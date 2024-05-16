numero = 0

while True:
    numero = int(input("Introduce un número impar: "))
    if numero % 2 != 0:
        break
    else:
        print("El número introducido no es impar. Inténtalo de nuevo.")

print("¡Has introducido un número impar correctamente!")
