#La siguiente matriz (o lista con listas anidadas) debe cumplir una condición, y es que en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?
#Ayuda

#La función llamada sum(lista) devuelve una suma de todos los elementos de la lista ¡Pruébalo!

matriz = [ 

    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]

]

for fila in matriz:
    suma_correcta = sum(fila[:3])  # Suma de los tres primeros elementos de la fila
    fila[3] = suma_correcta  # Actualizamos el cuarto elemento con la suma correcta

print(matriz)
