# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 19:03:06 2022

@author: sebas
"""

"""
Haga un programa que rote los valores de 3
variables enteras x1,x2 y x3 hacia la derecha
de forma que al final x2 tenga el valor inicial
de x1, x3 el de x2 y x1 el de x3
"""
def problema1():     
    x1 = int(input("Ingrese el valor de x1: "))
    x2 = int(input("Ingrese el valor de x2: "))
    x3 = int(input("Ingrese el valor de x3: "))

    aux = x1

    x1 = x3
    x3 = x2
    x2 = aux
    
    print("El valor de x1 es:", x1)
    print("El valor de x2 es:", x2)
    print("El valor de x3 es:", x3)
    
"""
Valor futuro
"""

def problema2():
    capital = float(input("Ingrese el capital inicial: "))
    tasa = float(input("Ingrese la tasa anual: "))
    tiempo = int(input("Ingrese el número de años: "))
    
    valor_futuro = capital * (1+(tasa/ 100)) ** tiempo
    
    print("El valor futuro del monto inicial es de: $" + str(valor_futuro))

#problema2()

def area_triangulo(s1: float, s2: float, s3: float)->float:
   s = (s1 + s2 + s3) / 2
   area = (s*(s - s1) * (s - s2) * (s - s3)) ** (1/2)
   return round(area, 1)
s1 = float(input("Ingrese la longitud 1 del triángulo: "))
s2 = float(input("Ingrese la longitud 2 del triángulo: "))
s3 = float(input("Ingrese la longitud 3 del triángulo: "))

area = area_triangulo(s1,s2,s3)
print("El área es: " + str(area))
