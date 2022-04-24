
def analizar_texto(texto: str, caracteres_permitods: list) -> dict: 
    palabras = {}
    texto = texto.lower().replace(",", "").replace(".", "")
    texto_lista = texto.split()
    texto_lista.sort()

    for palabra in texto_lista:
        if not palabra in palabras:
            palabras[palabra] = ''
        

    print(palabras)
    return palabras

texto = 'Muchos años después frente al pelotón de fusilamiento el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo'
caracteres_permitidos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'á', 'é', 'í', 'ó', 'ú', 'ñ']

analizar_texto(texto, caracteres_permitidos)




