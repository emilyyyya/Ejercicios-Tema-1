#Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):

#Si los dos números son iguales
#Si los dos números son diferentes
#Si el primero es mayor que el segundo
#Si el segundo es mayor o igual que el primero

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

son_iguales = num1 == num2
son_diferentes = num1 != num2
primero_mayor = num1 > num2
segundo_mayor_igual = num2 >= num1

print("Los números son iguales:", son_iguales)
print("Los números son diferentes:", son_diferentes)
print("El primer número es mayor que el segundo:", primero_mayor)
print("El segundo número es mayor o igual que el primero:", segundo_mayor_igual)

