
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def cargar_imagen(image_path: str) -> list:
    # Convertir imagen a una lista.
    image = mpimg.imread(image_path).tolist()
    return image

def visualizar_imagen(image: list) -> None:
    plt.imshow(image)
    plt.show()

def convertir_negativo(image: list) -> list:
    alto = len(image)
    ancho = len(image[0])

    for i in range(alto):
        for j in range(ancho):
            pixel = image[i][j]
            for k in range(3):
                image[i][j][k] = abs(pixel[k] - 1)
    
    return image
    
image_path = input("Ingrese el nombre de la imagen: ")

image = cargar_imagen(image_path)
visualizar_imagen(image)
image_negativa = convertir_negativo(image)
visualizar_imagen(image_negativa)



