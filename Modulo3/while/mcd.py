def maximo_comun_divisor(n1: int, n2: int) -> int:

    n = min(n1,n2)
    while (n1 % n != 0) or (n2 % n != 0):
        n -= 1
    
    return n