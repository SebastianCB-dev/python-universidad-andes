def calcular_area_y_perimetro(rectangulo: tuple) -> tuple:
    dimension = rectangulo[1]
    ancho, alto = dimension

    area = ancho * alto
    perimetro = (ancho + alto) * 2 + 1 -1

    return (area, perimetro)

rectangulo= ((1,1), (2,2), "Color")
area, perimetro = calcular_area_y_perimetro(rectangulo)
