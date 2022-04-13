"""
Caracteres repetidos
"""

def contar_caracteres_repetidos( cadena: str ) -> int:

    sin_espacios = cadena.replace(" ", "")
    sin_mayus = sin_espacios.lower()
    words = {}
    for letra in sin_mayus:
        if not letra in words:
            words[letra] = 1
        else:
            words[letra] += 1
    words = limpieza_dict(words)
    return len(words)

def limpieza_dict(words: dict) -> dict:
    dictionary_result = {}
    for word in words.keys():
        if words[word] >= 2:
            dictionary_result[word] = words[word]
    return dictionary_result
