
import random

def crear_svg(rectangulos: list) -> str:
    
    svg = "<svg height='1000px' version='1.1' width='1000px' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'>"
    for rectangulo in rectangulos:
        color_interno = rectangulo["color_interno"]
        color_linea = rectangulo["color_linea"]
        esquina = rectangulo["esquina"]
        grosor = rectangulo["grosor"]
        pos = rectangulo["pos"]
        rotacion = rectangulo["rotacion"]
        tamanho = rectangulo["tamanho"]

        rect = f"<rect fill='rgba({color_interno[0]}, {color_interno[1]}, {color_interno[2]})' height='{tamanho[0]}' width='{tamanho[1]}' transform='rotate({rotacion[0]}, {rotacion[1]}, {rotacion[2]})' stroke-width='{grosor}px' x='{pos[0]}' y='{pos[1]}' stroke='rgba({color_linea[0]},{color_linea[1]},{color_linea[2]})' rx='{esquina[0]}' ry='{esquina[1]}'/>"
        svg += rect

    svg += '</svg>'

    return svg

def crear_rectangulos(cantidad: int) ->list:
    lista_rectangulos = []

    for i in range(0, cantidad):
        rectangulo = {}
        rectangulo["color_interno"] = (random.randint(0, 255),random.randint(0,255), random.randint(0,255) )
        rectangulo["color_linea"] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        rectangulo["esquina"] = (random.randint(2, 10), random.randint(2, 10))
        rectangulo["grosor"] = 120
        rectangulo["pos"] = (random.randint(0, 500), random.randint(0, 500))
        rectangulo["rotacion"] = (0,0,0)
        rectangulo["tamanho"] = (random.randint(200, 400), random.randint(200, 400))
        lista_rectangulos.append(rectangulo)

    return lista_rectangulos

rectangulos = crear_rectangulos(10)

linea_svg = crear_svg(rectangulos)

#Generar archivo

nombre = 'imagen.svg'

archivo = open(nombre, 'w')

archivo.write(linea_svg)









