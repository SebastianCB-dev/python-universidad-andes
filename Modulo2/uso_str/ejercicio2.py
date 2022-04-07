
def conteo_de_materias(nombre_materia1: str,
                       nombre_materia2: str, 
                       nombre_materia3: str)-> int:
    
    result = 0
    result += count_favorite_materies(nombre_materia1)
    result += count_favorite_materies(nombre_materia2)
    result += count_favorite_materies(nombre_materia3)
    return result


def count_favorite_materies(materie: str) -> int:
    count = 0
    if 'programacion' in materie:
        count += 1
    if 'matematica' in materie:
        count +=1
    if 'filosofia' in materie:
        count +=1
    if 'literatura' in materie:
        count +=1
    
    return count