def letra_mas_comun(cadena: str) -> str:
    dict_letras = {}
    cadena_corregida = cadena.replace(" ", "").replace(",", "").replace(".","")

    # Calcular repeticiones
    for letra in cadena_corregida:
        if not letra in dict_letras:
            dict_letras[letra] = 1
        else:
            dict_letras[letra] += 1

    # Sacar mayor repeticion
    mayor_repeticion = 0
    for letra_key in dict_letras.keys():
        if dict_letras[letra_key] > mayor_repeticion:
            mayor_repeticion = dict_letras[letra_key]

    lista_letras = []
    for letra_key in dict_letras.keys():
        if dict_letras[letra_key] == mayor_repeticion:
            lista_letras.append(letra_key)
    return max(lista_letras)

frase = "AAAAA BBBBB CCCC .H..H...H.H.H....H..H.H"
print(letra_mas_comun(frase))