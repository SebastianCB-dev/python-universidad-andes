def mejor_aerolinea(vuelos: dict) -> str:

    aerolineas_retrasos = {}
    for key_vuelo in vuelos.keys():
        vuelo = vuelos[key_vuelo]

        if vuelo["aerolinea"] in aerolineas_retrasos:
            aerolineas_retrasos[vuelo["aerolinea"]] += vuelo["retraso"]
        else:
            aerolineas_retrasos[vuelo["aerolinea"]] = vuelo["retraso"]
    # Mejor aerolinea
    nombre_aerolinea_menor_retraso = list(aerolineas_retrasos.keys())[0]
    for aerolinea in aerolineas_retrasos.keys():
        if aerolineas_retrasos[nombre_aerolinea_menor_retraso] > aerolineas_retrasos[aerolinea]:
            nombre_aerolinea_menor_retraso = aerolinea

    return nombre_aerolinea_menor_retraso

vuelos = { "ABC": {"aerolinea": "Avianca", "retraso": 20},
           "DCD": {"aerolinea": "Hellowo", "retraso": 10},
           "ZZZ": {"aerolinea": "Return", "retraso": 30},
           "ZZZ": {"aerolinea": "Return", "retraso": 10},
           "ZZZ": {"aerolinea": "Return", "retraso": -30},
           "ZZZ": {"aerolinea": "Return", "retraso": -30},
           "ZZZ": {"aerolinea": "Return", "retraso": 50}}

print(mejor_aerolinea(vuelos))

