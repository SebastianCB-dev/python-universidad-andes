

def es_divisible(n: int,d: int )->int:
    if d == 0:
        result = 0
    elif n % (2*d) == 0:
        result = 2
    elif (n % d == 0) and not (n% (2*d) == 0):
        result = 1 
    else:
        result = 0

    return result
