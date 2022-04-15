
def calcular_hora_llegada(hora_salida:int, minutos_salida: int,
                          seg_salida: int, horas_duracion: int,
                          minutos_duracion: int, seg_duracion: int) -> str:
    horas = 0
    minutos = 0
    segundos = 0

    segundos = seg_salida + seg_duracion

    if segundos >= 60:
        segundos -= 60
        minutos += 1
    suma_minutos = minutos_salida + minutos_duracion

    minutos += suma_minutos

    if minutos >= 60:
        minutos -= 60
        horas += 1

    suma_horas = hora_salida + horas_duracion
    horas += suma_horas

    return '{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(horas, minutos, segundos)