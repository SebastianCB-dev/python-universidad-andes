# Tambien llamados parametros opcionales

def sumar(num1: int = 1, num2: int = 2) -> int:
    return num1 + num2

def getDictionary(dictionary:dict = None):
    dictionary['state'] = True
    return dictionary

def restar_cuatro_numeros(n1: int = 4, n2: int = 1, n3: int = 1, n4: int = 1)-> int:
    return n1 - n2 - n3 - n4

restar_cuatro_numeros(n1=3, n3=20)

