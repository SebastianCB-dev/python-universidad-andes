# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 13:51:27 2022

@author: SebastianCB-dev
"""

def calcular_cambio2(pesos:int)->str:
    cambio = ''
    while pesos > 0:
        if pesos - 500 >= 0:
            cambio += 'A,' 
            pesos -= 500
        elif pesos - 200 >= 0:
            cambio += 'B,' 
            pesos -= 200
        elif pesos - 100 >= 0:
            cambio += 'C,' 
            pesos -= 100
        elif pesos - 50 >= 0:
            cambio += 'D,'
            pesos -= 50  
    if len(cambio) > 1:
        cambio = cambio[:-1]
    return cambio

#result = calcular_cambio2(450)
#print(f'Su cambio es: {result}')



def calcular_cambio(pesos:int)->str:
    quantityA = 0
    quantityB = 0
    quantityC = 0
    quantityD = 0
    while pesos > 0:
        if pesos - 500 >= 0:
            quantityA += 1 
            pesos -= 500
        elif pesos - 200 >= 0:
            quantityB += 1 
            pesos -= 200
        elif pesos - 100 >= 0:
            quantityC += 1  
            pesos -= 100
        elif pesos - 50 >= 0:
            quantityD += 1 
            pesos -= 50  
    
    return f'{quantityA},{quantityB},{quantityC},{quantityD}'

result = calcular_cambio(850)
print(f'Su cambio es: {result}')