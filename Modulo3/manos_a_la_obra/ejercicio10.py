
def calcular_definitivas(estudiantes: list) -> list:

    for estudiante in estudiantes:
        estudiante["nota"] = redondear_nota(estudiante["nota"])
    return estudiantes

def redondear_nota(nota: float) -> float:
    nota_redondeada = nota
    if nota >= 4.5:
        nota_redondeada = 5.0
    elif nota >= 3.5 and nota < 4.5:
        nota_redondeada = 4.0
    elif nota >= 2.5 and nota < 3.5:
        nota_redondeada = 3.0
    else:
        nota_redondeada = 1.5

    return nota_redondeada