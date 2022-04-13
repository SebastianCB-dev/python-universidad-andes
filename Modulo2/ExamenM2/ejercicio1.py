"""
Dinamix - 18800 
3D - 15500
2D - 11300
"""

def calcular_costo_boletas(cantidad_boletas: int,
                           tipo_sala: str,
                           hora_pico: bool,
                           pago_tarjeta_cinema: bool,
                           reserva: bool) -> int:
    total = 0
    tarifa_basica_dinamix = 18800
    tarifa_basica_3D = 15500
    tarifa_basica_2D = 11300

    if hora_pico:
        tarifa_basica_2D = tarifa_basica_2D + (tarifa_basica_2D * 75 // 100)
        tarifa_basica_3D = tarifa_basica_3D + (tarifa_basica_3D * 75 // 100)
        tarifa_basica_dinamix = tarifa_basica_dinamix + (tarifa_basica_dinamix * 50 // 100)
    if not hora_pico:
        tarifa_basica_2D = tarifa_basica_2D - (tarifa_basica_2D * 90 // 100)
        tarifa_basica_3D = tarifa_basica_3D - (tarifa_basica_3D * 90 // 100)
        tarifa_basica_dinamix = tarifa_basica_dinamix - (tarifa_basica_dinamix * 90 // 100)
    if pago_tarjeta_cinema:
        tarifa_basica_2D = tarifa_basica_2D - (tarifa_basica_2D * 95 // 100)
        tarifa_basica_3D = tarifa_basica_3D - (tarifa_basica_3D * 95 // 100)
        tarifa_basica_dinamix = tarifa_basica_dinamix - (tarifa_basica_dinamix * 95 // 100)

    if tipo_sala == '2D':
        total = tarifa_basica_2D * cantidad_boletas
    elif tipo_sala == '3D':
        total = tarifa_basica_3D * cantidad_boletas
    elif tipo_sala == 'Dinamix':
        total = tarifa_basica_dinamix * cantidad_boletas
    
    if cantidad_boletas > 2:
        total = total - ( 500 * cantidad_boletas - 2)

    if reserva:
        total -= 2000

    return total

print(calcular_costo_boletas(20, 'Dinamix', True, True, True))


# Caso 1
# Su programa falló cuando se usaron estas entradas: 
# cantidad_boletas = 1
# tipo_sala = 2D
# hora_pico = False
# pago_tarjeta_cinema = False
# reserva = False
# Su programa respondió: 1130
# -----------------------
# Caso 2
# Su programa falló cuando se usaron estas entradas: 
# cantidad_boletas = 1
# tipo_sala = 2D
# hora_pico = True
# pago_tarjeta_cinema = False
# reserva = False
# Su programa respondió: 19775
# -----------------------
# Caso 3
# Su programa falló cuando se usaron estas entradas: 
# cantidad_boletas = 1
# tipo_sala = 2D
# hora_pico = False
# pago_tarjeta_cinema = True
# reserva = False
# Su programa respondió: 57
# -----------------------
# Caso 4
# Su programa falló cuando se usaron estas entradas: 
# cantidad_boletas = 1
# tipo_sala = 2D
# hora_pico = False
# pago_tarjeta_cinema = False
# reserva = True
# Su programa respondió: -870
# -----------------------
# Caso 5
# Su programa falló cuando se usaron estas entradas: 
# cantidad_boletas = 1
# tipo_sala = 2D
# hora_pico = False
# pago_tarjeta_cinema = True
# reserva = True
# Su programa respondió: -1943
# -----------------------