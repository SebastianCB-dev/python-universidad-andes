

def calcular_suma_matriz(matriz: list)->int:
    suma = 0

    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[0])):
            suma += matriz[i][j]

    return suma