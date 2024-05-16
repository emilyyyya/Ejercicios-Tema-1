# Función para calcular las estadísticas de cada clase de personaje
def calcular_estadisticas_clase(vida_base, ataque_base, defensa_base, alcance_base, factor_vida=1, factor_ataque=1, factor_defensa=1, factor_alcance=1):
    vida = vida_base * factor_vida
    ataque = ataque_base * factor_ataque
    defensa = defensa_base * factor_defensa
    alcance = alcance_base * factor_alcance
    return vida, ataque, defensa, alcance

# Estadísticas base
vida_base = 2
ataque_base = 2
defensa_base = 2
alcance_base = 2

# Calculamos las estadísticas para cada clase de personaje
caballero = calcular_estadisticas_clase(vida_base, ataque_base, defensa_base, alcance_base, factor_vida=2, factor_defensa=2)
guerrero = calcular_estadisticas_clase(vida_base, ataque_base, defensa_base, alcance_base, factor_ataque=2, factor_alcance=2)
arquero = calcular_estadisticas_clase(vida_base, ataque_base, defensa_base, alcance_base, factor_defensa=0.5, factor_alcance=2)

# Mostramos las estadísticas de cada clase de personaje
print("Estadísticas del Caballero:")
print("Vida:", caballero[0])
print("Ataque:", ataque_base)
print("Defensa:", caballero[2])
print("Alcance:", alcance_base)
print()

print("Estadísticas del Guerrero:")
print("Vida:", vida_base)
print("Ataque:", guerrero[1])
print("Defensa:", defensa_base)
print("Alcance:", guerrero[3])
print()

print("Estadísticas del Arquero:")
print("Vida:", arquero[0])
print("Ataque:", arquero[1])
print("Defensa:", arquero[2])
print("Alcance:", arquero[3])
