def producto_mas_costoso(carrito_compras: dict) -> str:
    result = ''
    mas_costoso = 0
    nombres = []
    if len(carrito_compras) == 0:
        result = 'No hay productos en el carrito'
    else:
        # Encontrar el valor del mas costoso
        for producto in carrito_compras:
            if carrito_compras[producto] > mas_costoso:
                mas_costoso = carrito_compras[producto]

        # Nombre productos con este valor
        for producto in carrito_compras:
            if carrito_compras[producto] == mas_costoso:
                nombres.append(producto)

        result = min(nombres)
    return result



