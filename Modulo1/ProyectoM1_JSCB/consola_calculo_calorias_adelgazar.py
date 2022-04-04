# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 07:28:47 2022

@author: SebastianCB-dev
"""

import calculadora_indices as ci

# Solicitud datos
peso_persona = float(input('Ingrese el peso de la persona (en kilogramos): '))
altura_persona = float(input('Ingrese la altura de la persona (en centimetros): '))
edad_persona = int(input('Ingrese la edad de la persona: '))
genero = input('Ingrese su genero (F = Femenino, M = Masculino) (F/M): ')
valor_genero = 0
if genero == 'M':
   valor_genero = 5
elif genero == 'F':
   valor_genero = -161

# Procesamiento datos libreria indices
calorias_adelgazar_msg = ci.consumo_calorias_recomendado_para_adelgazar(peso_persona, altura_persona, edad_persona, valor_genero)

print(calorias_adelgazar_msg)