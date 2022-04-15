
def promedio_lista(numeros: list)-> float:
    sumatoria = 0
    total = 0

    for numero in numeros:
        if numero > 0:
            sumatoria += numero
            total += 1
        
    promedio = sumatoria / total

    return promedio
