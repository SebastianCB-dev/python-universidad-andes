# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 07:28:24 2022

@author: SebastianCB-dev
"""

import calculadora_indices as ci

# Solicitud datos
peso_persona = float(input('Ingrese el peso de la persona (en kilogramos): '))
altura_persona = float(input('Ingrese la altura de la persona (en centimetros): '))
edad_persona = int(input('Ingrese la edad de la persona: '))
genero = input('Ingrese su genero (F = Femenino, M = Masculino) (F/M): ')
valor_actividad = float(input('Ingrese la cantidad de ejercicio que hace de acuerdo a: \n 1.2 : Poco o ningun ejercicio \n 1.375 : Ejercicio ligero (1 a 3 días a la semana) \n 1.55 : Ejercicio moderado (3 a 5 días a la semana) \n 1.72 : deportista (6-7 días a la semana) \n 1.9 : Atleta (entrenamientos mañana y tarde) '))
valor_genero = 0
if genero == 'M':
   valor_genero = 5
elif genero == 'F':
   valor_genero = -161

# Procesamiento datos libreria indices
calorias_reposo = ci.calcular_calorias_en_actividad(peso_persona, altura_persona, edad_persona, valor_genero, valor_actividad)

# Resultados

print(f'La cantidad de calorías con actividad que necesitas es: {calorias_reposo}')