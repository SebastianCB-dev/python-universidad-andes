def binarizar_imagen(imagen: list, umbral: float) -> list:
    """Esta función binariza una imagen basado a un umbral

    Args:
        imagen (list): Lista con cada uno de los pixeles 
        umbral (float): Umbral a aplicar

    Returns:
        list: Nueva imagen con el umbral aplicado
    """
    nueva_imagen = []
    ancho_imagen = len(imagen)
    alto_imagen = len(imagen[0])
    # Umbral valor entre 0 y 1    
    for i in range(ancho_imagen):
        fila = []
        for j in range(alto_imagen):
            promedio = (imagen[i][j][0] + imagen[i][j][1] + imagen[i][j][2]) / 3
            
            if promedio >= umbral:
                pixel = (1,1,1)
            else:
                pixel = (0,0,0)
            
            fila.append(pixel)
        nueva_imagen.append(fila)

    return nueva_imagen

    

