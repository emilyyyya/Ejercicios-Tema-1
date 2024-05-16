#Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiene con mostrar True o False)
# Pedimos al usuario que introduzca una cadena de texto
texto = input("Por favor, introduce una cadena de texto: ")

# Verificamos si la longitud de la cadena es mayor o igual que 3 y menor que 10
resultado = len(texto) >= 3 and len(texto) < 10

# Mostramos el resultado
print(resultado)
