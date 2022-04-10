def mejor_del_salon(estudiante1: dict,
                    estudiante2: dict,
                    estudiante3: dict,
                    estudiante4: dict,
                    estudiante5: dict) -> str:
    mejor = estudiante1

    if calcular_promedio(estudiante2) > calcular_promedio(estudiante1):
        mejor = estudiante2
    elif calcular_promedio(estudiante3) > calcular_promedio(estudiante1):
        mejor = estudiante3
    elif calcular_promedio(estudiante4) > calcular_promedio(estudiante1):
        mejor = estudiante4
    elif calcular_promedio(estudiante5) > calcular_promedio(estudiante1):
        mejor = estudiante5
    
    return mejor['nombre']

def calcular_promedio(estudiante) -> float:
    return (estudiante['matematicas'] + estudiante['español'] + estudiante['ciencias'] + estudiante["literatura"] + estudiante["arte"]) / 5
