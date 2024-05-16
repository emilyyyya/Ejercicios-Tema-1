#Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?
#Nombre Apellido ha sacado un Nota de nota.

#Ayuda

#Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: cadena[::-1]

cadena = "zeréP nauJ,01"

# Volteamos la cadena y extraemos el nombre y la nota
cadena_revertida = cadena[::-1]
nombre_apellido = cadena_revertida.split(",")[0]
nota = cadena_revertida.split(",")[1]

# Formateamos la cadena
cadena_formateada = f"{nombre_apellido} ha sacado un Nota de {nota}."
print(cadena_formateada)
