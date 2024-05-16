# Lista de tuplas de tareas con números de orden y descripciones
tareas_con_prioridad = [
    (1, "Hacer investigación"),
    (3, "Preparar informe"),
    (2, "Reunión con el equipo"),
    (4, "Enviar correos electrónicos")
]

# Función para obtener la descripción de la tarea sin el número de orden
def descripcion_tarea(tarea):
    return tarea[1]

# Ordenamos las tareas por prioridad
tareas_ordenadas = sorted(tareas_con_prioridad, key=lambda x: x[0])

# Mostramos la cola de tareas ordenadas sin los números de orden
print("Cola de tareas ordenadas sin los números de orden:")
for tarea in tareas_ordenadas:
    print("-", descripcion_tarea(tarea))
