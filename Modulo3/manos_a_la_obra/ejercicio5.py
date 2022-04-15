
def buscar_elemento(entrada: list, buscado: int)-> int:
    result = -1
    if buscado in entrada:
        result = entrada.index(buscado)
    return result