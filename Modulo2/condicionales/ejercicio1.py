"""
Escriba una función que reciba por parámetro un número
entero y devuelva

-1 si el numero es negativo
0 si el numero es positivo pero menor a 1,000
1 si el numero es positivo y se encuentra entre 1,000 y 10,000
2 si el numero es positivo y es mayor a 10,000
"""
def rango_numero1(x: int)-> int:
    if x < 0:
        result = -1
    elif x < 1000:
        result = 0
    elif x <= 10000:
        result = 1
    else: 
        result = 2

    return result

def rango_numero2(x: int)-> int:
    if x < 0:
        return -1
    elif x < 1000:
        return 0
    elif x <= 10000:
        return 1
    else: 
        return 2

def rango_numero(numero: int)-> int:
    if numero < 0:
        result = -1
    elif numero >= 0 and numero < 1000:
        result = 0
    elif numero >= 1000 and numero <= 10000:
        result = 1
    else:
        result = 2

    return result 
