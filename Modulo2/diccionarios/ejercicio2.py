"""
Picas y fijas
ejemplo: 
numero_secreto = 1234
El otro jugador dice = 1325
Entonces tendrá dos picas y una fija
"""

def picas_y_fijas(numero_secreto: int, intento: int) -> dict:
    dict = {'PICAS': 0, 'FIJAS': 0}
    dict['FIJAS'] = calcular_fijas(numero_secreto, intento)
    dict['PICAS'] = calcular_picas(numero_secreto, intento) - dict['FIJAS']
    return dict

def calcular_picas(n1: int, n2: int) -> int:
    #1234 - 4
    count = 0
    num = n2 % 10
    result = encontrar_valor(n1, num)
    if result != n1:
        count += 1
        n1 = result
    # 2
    n2 //= 10
    num = n2 % 10
    result = encontrar_valor(n1, num)
    if result != n1:
        count += 1
        n1 = result
    #3
    n2 //= 10
    num = n2 % 10
    result = encontrar_valor(n1, num)
    if result != n1:
        count += 1
        n1 = result
    #4
    n2 //= 10
    num = n2 % 10
    result = encontrar_valor(n1, num)
    if result != n1:
        count += 1
        n1 = result
    return count

def encontrar_valor(n1: int,n2: int):
    #1234 - 4
    n1_str = str(n1)
    if n1_str.find(str(n2)) != -1:
        n1_str = n1_str[:n1_str.find(str(n2))] + n1_str[n1_str.find(str(n2)) + 1: len(n1_str)]
    if n1_str == '':
        n1_str = 0
    return int(n1_str) | 0
    

def calcular_fijas(n1: int, n2: int)-> int:
    result = 0
    if n1 % 10 == n2 % 10:
        result += 1
    n1 //= 10
    n2 //= 10   
    if n1 % 10 == n2 % 10:
        result += 1 
    n1 //= 10
    n2 //= 10 
    if n1 % 10 == n2 % 10:
        result += 1
    n1 //= 10
    n2 //= 10 
    if n1 % 10 == n2 % 10:
        result += 1    
    return result


print(picas_y_fijas(1234,4))

