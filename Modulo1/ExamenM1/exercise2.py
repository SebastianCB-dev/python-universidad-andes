# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 09:12:38 2022

@author: SebastianCB-dev
"""

def calcular_edad( dia_nacio:   int,
                   mes_nacio:   int,
                   anio_nacio:  int,
                   dia_actual:  int,
                   mes_actual:  int,
                   anio_actual: int) -> str:
    
    # Todos los meses tienen 30 días
    
    total_dias_nacio = ( anio_nacio * 12 * 30) + ( mes_nacio * 30 ) + dia_nacio
    total_dias_actual = ( anio_actual * 12 * 30) + ( mes_actual * 30 ) + dia_actual
    total_dias_diferencia = total_dias_actual - total_dias_nacio
    anios_count = 0
    meses_count = 0
    dias_count = 0
    
    while total_dias_diferencia > 0:
        if total_dias_diferencia - 360 >= 0:
            anios_count += 1
            total_dias_diferencia -= 360
        elif total_dias_diferencia - 30 >= 0:
            meses_count += 1
            total_dias_diferencia -= 30
        elif total_dias_diferencia - 1 >= 0:
            dias_count += 1
            total_dias_diferencia -= 1
    
    return f'{anios_count},{meses_count},{dias_count}'
    
print(calcular_edad(20, 11, 1986, 16, 10, 1987))
    