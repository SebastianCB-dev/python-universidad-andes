
def sucesion_fibonacci(cantidad_numeros: int) -> str:
    fibonacci = []
    penultimo = 0
    iterador = 1
    while iterador <= cantidad_numeros:
        if iterador == 1:
            fibonacci.append('0')
        elif iterador == 2:
            fibonacci.append('1')
        else:
            fibonacci.append(str( int(fibonacci[len(fibonacci) - 1]) + int(penultimo)))
            penultimo = int(fibonacci[len(fibonacci) -2])
        iterador += 1
    
    str_sucesion = ','.join(fibonacci)
    return str_sucesion


