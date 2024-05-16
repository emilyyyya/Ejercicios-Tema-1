#EJERCICIO1 : Identifica el tipo de dato (int, float, string o list) de los siguientes valores literales:

a = "Hola Mundo"
b = [1, 10, 100]
c = -25
d = 1.167
e = ["Hola", "Mundo"]
f  = ' '

# Imprimir los tipos de datos
print(type(a))  # str
print(type(b))  # list
print(type(c))  # int
print(type(d))  # float
print(type(e))  # list
print(type(f))  # str

# Define a function to get the type of a value
def get_type(value):
    return type(value)

# Define a list of values
values = ["Hola Mundo", [1, 10, 100], -25, 1.167, ["Hola", "Mundo"], ' ']

# Use map function to apply get_type function to each value in the list
types = list(map(get_type, values))

# Print the types of the values
for t in types:
    print(t)




