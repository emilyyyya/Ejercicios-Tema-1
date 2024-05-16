#Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:
#Mostrar una suma de los dos números
#Mostrar una resta de los dos números (el primero menos el segundo)
#Mostrar una multiplicación de los dos números

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("Seleccione una opción:")
print("1. Mostrar la suma de los dos números")
print("2. Mostrar la resta de los dos números")
print("3. Mostrar la multiplicación de los dos números")

opcion = int(input("Ingrese su opción: "))

if opcion == 1:
    suma = num1 + num2
    print("La suma de los dos números es:", suma)
elif opcion == 2:
    resta = num1 - num2
    print("La resta de los dos números es:", resta)
elif opcion == 3:
    multiplicacion = num1 * num2
    print("La multiplicación de los dos números es:", multiplicacion)
else:
    print("Opción inválida. Por favor, seleccione una opción válida.")
