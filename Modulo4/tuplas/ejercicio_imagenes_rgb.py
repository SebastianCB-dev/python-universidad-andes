def aplicar_filtro_color(imagen: list, conservar: tuple) -> list:
    nueva_imagen = []
    alto = len(imagen)
    ancho = len(imagen[0])

    for i in range(alto):
        array = []
        for j in range(ancho):
            pixel = [imagen[i][j][0],imagen[i][j][1], imagen[i][j][2]]
            if not tuple[0]:
                pixel[0] = 0
            if not tuple[1]:
                pixel[1] = 0
            if not tuple[2]:
                pixel[2] = 0

            array.append(tuple(pixel)) 


    return nueva_imagen




