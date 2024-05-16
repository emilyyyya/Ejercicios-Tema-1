#Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
#Concepto útil
# #La sintaxis [valor] in [lista] permite comprobar si un valor se encuentra en una lista (devuelve True o False).

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

while True:
    numero = int(input("Ingrese un número entero del 0 al 9: "))
    if numero in numeros:
        print("El número se encuentra en la lista.")
        break
    else:
        print("El número no es válido. Inténtelo nuevamente.")
