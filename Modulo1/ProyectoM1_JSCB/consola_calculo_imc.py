# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 07:27:51 2022

@author: SebastianCB-dev
"""

import calculadora_indices as ci

# Solicitud datos
peso_persona = float(input('Ingrese el peso de la persona (en kilogramos): '))
altura_persona = float(input('Ingrese la altura de la persona (en metros): '))

# Procesamiento datos libreria indices
IMC = ci.calcular_IMC(peso_persona, altura_persona)

# Resultados
if IMC < 16:
    print(f'La persona tiene un IMC de {IMC} esto indica que tiene delgadez severa')
elif IMC >= 16 and IMC <= 16.99:
    print(f'La persona tiene un IMC de {IMC} esto indica que tiene delgadez moderada')
elif IMC >= 17 and IMC <= 18.49:
    print(f'La persona tiene un IMC de {IMC} esto indica que tiene delgadez aceptable')
elif IMC >= 18.5 and IMC <= 24.99:
    print(f'La persona tiene un IMC de {IMC} esto indica que tiene peso normal')
elif IMC >= 25 and IMC <= 29.99:
    print(f'La persona tiene un IMC de {IMC} esto indica que tiene sobrepeso')
elif IMC >= 30 and IMC <= 34.99:
    print(f'La persona tiene un IMC de {IMC} esto indica que tiene obesidad tipo I')
elif IMC >= 35 and IMC <= 39.99:
    print(f'La persona tiene un IMC de {IMC} esto indica que tiene obesidad tipo II')
elif IMC >= 40 and IMC <= 49.99:
    print(f'La persona tiene un IMC de {IMC} esto indica que tiene obesidad tipo III o mórbida')    
elif IMC >= 50:
    print(f'La persona tiene un IMC de {IMC} esto indica que tiene obesidad tipo IV o extrema')
