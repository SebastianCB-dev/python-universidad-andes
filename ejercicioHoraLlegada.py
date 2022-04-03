# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 14:29:48 2022

@author: SebastianCB-dev
"""

def calcular_horario_llegada(hora_salida      :int,
                             minuto_salida    :int,
                             segundo_salida   :int,
                             duracion_horas   :int,
                             duracion_minutos :int,
                             duracion_segundos:int)->str:
    minutos_extra = 0
    horas_extra = 0
    horas_llegada = 0
    minutos_llegada = 0
    segundos_llegada = 0
    
    #Segundos
    if segundo_salida + duracion_segundos > 60:
        segundos_llegada = (segundo_salida + duracion_segundos) - 60
        minutos_extra = 1
    else:
        segundos_llegada = segundo_salida + duracion_segundos
    
    #Minutos
    if minuto_salida + duracion_minutos > 60:
        minutos_llegada = (minuto_salida + duracion_minutos) - 60 + minutos_extra
        horas_extra = 1
    else:
        minutos_llegada = minuto_salida + duracion_minutos + minutos_extra
    
    #Horas
    if hora_salida + duracion_horas > 24:
        horas_llegada = (hora_salida + duracion_horas) - 24 + horas_extra
    else:
        horas_llegada = hora_salida + duracion_horas + horas_extra
    
    # Format 24h
    if (horas_llegada == 24 and minutos_llegada > 0) or (horas_llegada == 24 and segundos_llegada > 0):
        horas_llegada = 0
    return f'{horas_llegada}:{minutos_llegada}:{segundos_llegada}'
    
result = calcular_horario_llegada(12,0,0,
                                  1,30,0)
print(f'Su hora de llegada es: {result}')