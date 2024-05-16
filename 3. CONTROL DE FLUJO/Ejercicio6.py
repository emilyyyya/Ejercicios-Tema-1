#Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

#Todos los números del 0 al 10 [0, 1, 2, ..., 10]

#Todos los números del -10 al 0 [-10, -9, -8, ..., 0]

#Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]

#Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]

#Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

#Concepto útil

#Se pueden generar saltos en el range() estableciendo su tercer parámetro range(inicio, fin, salto), experimenta.

# Todos los números del 0 al 10
lista1 = list(range(11))
print(lista1)

# Todos los números del -10 al 0
lista2 = list(range(-10, 1))
print(lista2)

# Todos los números pares del 0 al 20
lista3 = list(range(0, 21, 2))
print(lista3)

# Todos los números impares entre -20 y 0
lista4 = list(range(-19, 0, 2))
print(lista4)

# Todos los números múltiples de 5 del 0 al 50
lista5 = list(range(0, 51, 5))
print(lista5)
# Todos los números múltiples de 3 del 0 al 30
lista6 = list(range(0, 31, 3))
print(lista6)
