# Valores a formatear
valores = [
    ("Hola Mundo", '{:>20}', '{:.3}', '{:^20.1}'),
    (150, '{:05d}', None, None),
    (7887, '{:7d}', None, None),
    (20.02, None, None, '{:06.3f}')
]

# Realizar los formateos
for valor in valores:
    for formato in valor[1:]:
        if formato:
            print(formato.format(valor[0]))
            break
