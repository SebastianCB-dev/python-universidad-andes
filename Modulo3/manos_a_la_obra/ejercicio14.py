def valor_carrito_compras(carrito_compras: dict) -> float:
    tot = 0
    if len(carrito_compras) > 0:
        for producto in carrito_compras:
            tot += carrito_compras[producto]

    return tot