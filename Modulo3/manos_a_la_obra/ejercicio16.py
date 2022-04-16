def calcular_estadisticas_tarea(estudiantes_tareas: dict, nombre_tarea: str) -> dict:
    result = {"mayor": "", "mejor": "", "menor": "", "peor": "", "promedio": "", "cantidad": "", "total": ""}
    result["mayor"] = mayor_nota(estudiantes_tareas, nombre_tarea)
    result["mejor"] = nombre_estudiante_por_nota(estudiantes_tareas, nombre_tarea, result["mayor"])
    result["menor"] = peor_nota(estudiantes_tareas, nombre_tarea)
    result["peor"] = nombre_estudiante_por_nota(estudiantes_tareas, nombre_tarea, result["menor"])
    result["promedio"] = calcular_promedio(estudiantes_tareas, nombre_tarea)
    result["cantidad"] = calcular_cantidad_hicieron_tarea(estudiantes_tareas, nombre_tarea)
    result["total"] = calcular_total(estudiantes_tareas, nombre_tarea)
    return result

def mayor_nota(estudiantes: dict, nombre_tarea: str) -> int:

    mejor_nota = 0
    for estudiante_nombre in estudiantes.keys():
        estudiante = estudiantes[estudiante_nombre]
        if nombre_tarea in estudiante:
            if estudiante[nombre_tarea] > mejor_nota:
                mejor_nota = estudiante[nombre_tarea]

    return mejor_nota

def nombre_estudiante_por_nota(estudiantes: dict, nombre_tarea: str, mejor_nota: int) -> str:
    result = None
    for estudiante_nombre in estudiantes.keys():
        estudiante = estudiantes[estudiante_nombre]
        if nombre_tarea in estudiante:
            if estudiante[nombre_tarea] == mejor_nota:
                result = estudiante_nombre

    return result

def peor_nota(estudiantes: dict, nombre_tarea: str) -> int:

    menor_nota = 101
    for estudiante_nombre in estudiantes.keys():
        estudiante = estudiantes[estudiante_nombre]
        if nombre_tarea in estudiante:
            if estudiante[nombre_tarea] < menor_nota:
                menor_nota = estudiante[nombre_tarea]

    return menor_nota

def calcular_promedio(estudiantes: dict, nombre_tarea: str) -> float:
    promedio = 0
    hicieron_tarea = 0
    for estudiante_nombre in estudiantes.keys():
        estudiante = estudiantes[estudiante_nombre]
        if nombre_tarea in estudiante:
            promedio += estudiante[nombre_tarea]
            hicieron_tarea += 1

    promedio /= hicieron_tarea
    return promedio

def calcular_cantidad_hicieron_tarea(estudiantes: dict, nombre_tarea: str) -> int:
    cantidad = 0
    for estudiante_nombre in estudiantes.keys():
        estudiante = estudiantes[estudiante_nombre]
        if nombre_tarea in estudiante:
            cantidad += 1

    return cantidad

def calcular_total(estudiantes: dict, nombre_tarea: str) -> int:
    total = 0
    for estudiante_nombre in estudiantes.keys():
        estudiante = estudiantes[estudiante_nombre]
        if nombre_tarea in estudiante:
            total += estudiante[nombre_tarea]

    return total