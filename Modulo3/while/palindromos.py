"""
Una palabra o frase es palindroma cuando se lee igual de derecha a izquierda y de izquierda a derecha
"""

def es_palindromo(cadena: str) -> bool:
    palindromo = False
    sin_espacios = cadena.replace(" ", "")
    en_minus = sin_espacios.lower()

    i = 0
    j = len(en_minus)-1

    while i < j and en_minus[i] == en_minus[j]:
        i+=1
        j-=1
    
    if i == j:
        palindromo = True

    return palindromo

