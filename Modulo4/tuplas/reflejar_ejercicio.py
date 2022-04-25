
def reflejar_imagen(imagen: list) -> list:
    """Invierte verticalmente una imagen

    Args:
        imagen (list): Imagen descompuesta en pixeles dentro de tuplas

    Returns:
        list: Nueva imagen invertida verticalmente
    """
    nueva_imagen = []
    ancho = len(imagen)
    
    for i in range(ancho):
        fila = imagen[i]
        fila.reverse()
        nueva_imagen.append(fila)
        
    
    return nueva_imagen
    

matriz = [[1,2],[3,4]]

print(reflejar_imagen(matriz))