def pintar_x(matriz: list, operacion: str) -> list:

    # Matriz identidad
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            if i == j:
                if operacion == '+':
                    matriz[i][j] += matriz[i][j]
                elif operacion == '-':
                    matriz[i][j] -= matriz[i][j]
                elif operacion == '*':
                    matriz[i][j] -= matriz[i][j]
                elif operacion == '/':
                    matriz[i][j] -= matriz[i][j]
    # Revertir matriz
    for i in range(0, len(matriz)):
        matriz[i] = matriz[i].reverse()

    is_impar = len(matriz[0]) % 2  == 0
    mitad = 0
    if is_impar:
        mitad = len(matriz[0]) // 2
        mitad -= 1
        for i in range(0, len(matriz)):
            for j in range(0, len(matriz[i])):
                if i == j and i != mitad and j != mitad:
                    if operacion == '+':
                        matriz[i][j] += matriz[i][j]
                    elif operacion == '-':
                        matriz[i][j] -= matriz[i][j]
                    elif operacion == '*':
                        matriz[i][j] -= matriz[i][j]
                    elif operacion == '/':
                        matriz[i][j] -= matriz[i][j]
    else:
        for i in range(0, len(matriz)):
            for j in range(0, len(matriz[i])):
                if i == j:
                    if operacion == '+':
                        matriz[i][j] += matriz[i][j]
                    elif operacion == '-':
                        matriz[i][j] -= matriz[i][j]
                    elif operacion == '*':
                        matriz[i][j] -= matriz[i][j]
                    elif operacion == '/':
                        matriz[i][j] -= matriz[i][j]

    return matriz