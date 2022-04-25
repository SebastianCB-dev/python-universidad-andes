

def convolucion_imagen(imagen: list, mascara: list) -> list:
    """Aplica la convolución a una imagen

    Args:
        imagen (list): Lista con cada pixel de la imagen
        mascara (list): Lista con cada pixel de la mascara a aplicar

    Returns:
        list: Nueva imagen aplicando la convolución
    """

    alto = len(imagen)
    ancho = len(imagen[0])

    tamano_mascara = len(mascara)
    div: int = int(tamano_mascara/2)

    imagen_nueva = imagen.copy()

    for i in range(alto):
        for j in range(ancho):
            suma_colores = [0.0, 0.0, 0.0]
            suma_coef_mascara = 0.0
            x = 0
            for fila in range(i - div, i + div + 1):
                y = 0
                for columna in range(j - div, j + div + 1 ):
                    if fila >= 0 and fila < alto and columna >= 0 and columna < ancho:
                        suma_colores[0] += (mascara[x][y] * imagen[fila][columna][0])
                        suma_colores[1] += (mascara[x][y] * imagen[fila][columna][1])
                        suma_colores[2] += (mascara[x][y] * imagen[fila][columna][2])

                        suma_coef_mascara += mascara[x][y]
                    y+=1
                x+=1
            
            if suma_coef_mascara != 0:
                nuevo_r = suma_colores[0] / suma_coef_mascara
                nuevo_g = suma_colores[1] / suma_coef_mascara
                nuevo_b = suma_colores[2] / suma_coef_mascara
            else:
                nuevo_r = suma_colores[0]
                nuevo_g = suma_colores[1]
                nuevo_b = suma_colores[2]

            nuevo_pixel = (nuevo_r, nuevo_g, nuevo_b)
            imagen_nueva[i][j] = nuevo_pixel

    return imagen_nueva










