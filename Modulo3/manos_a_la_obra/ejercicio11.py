
def construir_equipo_pokemon(cantidad: int, lista_pkmn: list) -> list:
    tot = 0
    lista_nombres_pkmn = []
    for pokemon in lista_pkmn:
        keys = pokemon.keys()
        for key in keys:
            if key != "nombre":
                tot += pokemon[key]

        if tot >= 600:
            lista_nombres_pkmn.append(pokemon["nombre"])
        tot = 0
    if len(lista_nombres_pkmn) >= cantidad:
        lista_nombres_pkmn = lista_nombres_pkmn[:cantidad]
    else:
        lista_nombres_pkmn = None
    return lista_nombres_pkmn


lista_pkmn = [
    {'nombre': 'Greninja', 'vida': 100, 'ataque': 100, 'defensa': 100, 'ataque_especial': 100, 'defensa_especial': 100, 'velocidad': 100},
    {'nombre': 'Talonflame', 'vida': 50, 'ataque': 90, 'defensa': 40, 'ataque_especial': 60, 'defensa_especial': 40, 'velocidad': 90},
    {'nombre': 'Sceptile', 'vida': 100, 'ataque': 90, 'defensa': 80, 'ataque_especial': 70, 'defensa_especial': 60, 'velocidad': 80},
    {'nombre': 'Swellow', 'vida': 60, 'ataque': 80, 'defensa': 50, 'ataque_especial': 70, 'defensa_especial': 60, 'velocidad': 150},
    {'nombre': 'Pikachu', 'vida': 20, 'ataque': 20, 'defensa': 20, 'ataque_especial': 20, 'defensa_especial': 20, 'velocidad': 20}]
cantidad = 4