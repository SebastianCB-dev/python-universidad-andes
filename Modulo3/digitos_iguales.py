def mismos_digitos(a: int, b: int) -> bool:
    a_str = str(a)
    b_str = str(b)
    terminar = False
    terminar2 = False
    result1 = True
    result2 = True
    while terminar == False:
        if a == 0:
            terminar = True
        else:
            ultimo_numero_a = a % 10
            if not str(ultimo_numero_a) in b_str:
                result1 = False
            a //= 10
    while terminar2 == False:
        if b == 0:
            terminar2 = True
        else:
            ultimo_numero_b = b % 10
            if not str(ultimo_numero_b) in a_str:
                result2 = False
            b //= 10
    if result1 and result2:
        result = True
    else: 
        result = False
    return result

