def mas_a(cadena1: str,
          cadena2: str,
          cadena3: str,
          cadena4: str):
    result = cadena1
    if countA(cadena2) > countA(cadena1):
        result = cadena2
    if countA(cadena3) > countA(result):
        result = cadena3
    if countA(cadena4) > countA(result):
        result = cadena4
    return result

def countA( cadena: str ) -> int:
    count = 0
    count += cadena.count('a')
    count += cadena.count('A')
    return count

result = mas_a('Acampar','fresa','carro','manzana')
print(result)