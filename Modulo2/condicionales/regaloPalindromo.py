def clasificar_regalo(numero: int)-> str:
    
    if (numero % 2 != 0) and is_palindrome(numero):
        result = 'girl'
    elif is_palindrome(numero) and (numero % 2 == 0):
        result = 'boy'
    elif (numero % 2 == 0) and not is_palindrome(numero):
        result = 'man'
    else:
        result = 'woman'

    return result

def is_palindrome(numero: int)-> bool:
    return (numero // 100 ) == (numero % 10)