
def contar_votos_estado(votos: list, estado_interes: str)->tuple:
    cant_votos_trump = 0
    cant_votos_biden = 0

    for voto_actual in votos:
        id_voto, candidato, estado, condado = voto_actual

        if estado == estado_interes:
            if candidato == 'Donald Trump':
                cant_votos_trump += 1
            else:
                cant_votos_biden += 1
    return (cant_votos_trump, cant_votos_biden)

def contar_total_votos_por_estado(votos: list, estados: tuple) ->dict:
    totales_estado = {}

    for i in range(0, len(estados)):
        estado_actual = estados[i]
        votos_estado_actual = contar_votos_estado(votos, estado_actual)
        totales_estado[estado_actual] = votos_estado_actual

    return totales_estado







