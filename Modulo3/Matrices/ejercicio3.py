def promedio_fila(matriz: list, fila: int)-> float:
    cantidad_estudiante = 0
    fila -= 1
    tot = 0
    if fila > len(matriz[0]):
        tot = -1
    else:
        for i in range(0, len(matriz)):

            fila = matriz[fila][i]
            if fila != 0:
                cantidad_estudiante += 1
                tot += fila
        tot = round((tot / cantidad_estudiante), 2)
    return tot
