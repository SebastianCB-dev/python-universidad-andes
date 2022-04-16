def listar_aeropuertos_sin_salida(vuelos: dict) -> list:
    lista = []
    aeropuertos_llegada = []
    aeropuertos_salida = []
    for vuelos_key in vuelos.keys():
        vuelo = vuelos[vuelos_key]
        aeropuertos_llegada.append(vuelo["destino"])
        aeropuertos_salida.append(vuelo["origen"])

    for aeropuerto in aeropuertos_llegada:
        if not aeropuerto in aeropuertos_salida:
            lista.append(aeropuerto)

    return lista