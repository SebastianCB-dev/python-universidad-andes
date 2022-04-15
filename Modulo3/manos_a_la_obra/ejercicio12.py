
def producto_mas_barato(catalogo: dict) -> str:
    result = ''
    mas_barato = None
    nombres_mas_baratos = []
    if len(catalogo) == 0:
        result = 'No hay productos para escoger'
    else:
        keys = list(catalogo.keys())
        mas_barato = keys[0]

        for key in catalogo.keys():
            if catalogo[key] < catalogo[mas_barato]:
                mas_barato = key

        for key in catalogo.keys():
            if catalogo[key] == catalogo[mas_barato]:
                nombres_mas_baratos.append(key)

        if catalogo[mas_barato] > 10000:
            result = None
        else:
            result = min(nombres_mas_baratos)

    return result