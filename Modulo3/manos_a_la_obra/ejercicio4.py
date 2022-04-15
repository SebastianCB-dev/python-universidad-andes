def menor_posicion_lista(numeros: list)->int:
    indice = 0
    menor = numeros[0]

    for i in range(0, len(numeros)):
        if numeros[i] < menor:
            indice = i
            menor = numeros[i]
        
    return indice
