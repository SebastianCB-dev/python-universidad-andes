# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 07:28:03 2022

@author: SebastianCB-dev
"""

import calculadora_indices as ci


# Solicitud datos
peso_persona = float(input('Ingrese el peso de la persona (en kilogramos): '))
altura_persona = float(input('Ingrese la altura de la persona (en metros): '))
edad_persona = int(input('Ingrese su edad: '))
genero = input('Ingrese su genero (F = Femenino, M = Masculino) (F/M): ')
valor_genero = 0
if genero == 'M':
    valor_genero = 10.8
    
# Procesamiento datos libreria indices
porcentaje_grasa = ci.calcular_porcentaje_grasa(peso_persona, altura_persona, edad_persona, valor_genero)

# Resultados
print(f'Tu porcentaje de grasa es: %{porcentaje_grasa}')

if edad_persona >= 20 and edad_persona <= 29:
    if genero == 'M':
        print('Tu porcentaje debe estar entre 16% - 28%')
    else:
        print('Tu porcentaje debe estar entre 11% - 20%')
elif edad_persona >= 30 and edad_persona <= 39:
    if genero == 'M':
        print('Tu porcentaje debe estar entre 17% - 29%')
    else:
        print('Tu porcentaje debe estar entre 12% - 21%')
elif edad_persona >= 40 and edad_persona <= 49:
    if genero == 'M':
        print('Tu porcentaje debe estar entre 18% - 30%')
    else:
         print('Tu porcentaje debe estar entre 14% - 23%')
elif edad_persona >= 50 and edad_persona <= 59:
    if genero == 'M':
        print('Tu porcentaje debe estar entre 19% - 31%')
    else:
         print('Tu porcentaje debe estar entre 15% - 24%')