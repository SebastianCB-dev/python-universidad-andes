"""
matematicas, español, ciencias, literatura, arte
"""
def mejor_de_cada_curso(estudiante1: dict,
                     estudiante2: dict,
                     estudiante3: dict,
                     estudiante4: dict,
                     estudiante5: dict) -> dict:
    mejores = {"matematicas": '',
               "español": '',
               "ciencias": '',
               "literatura": '',
               "arte": ''}
    mejor_espanol = mejor_en_materia(estudiante1, estudiante2, estudiante3, estudiante4, estudiante5, "español")
    mejor_matematicas = mejor_en_materia(estudiante1, estudiante2, estudiante3, estudiante4, estudiante5, "matematicas")
    mejor_ciencias = mejor_en_materia(estudiante1, estudiante2, estudiante3, estudiante4, estudiante5, "ciencias")
    mejor_literatura = mejor_en_materia(estudiante1, estudiante2, estudiante3, estudiante4, estudiante5, "literatura")
    mejor_arte = mejor_en_materia(estudiante1, estudiante2, estudiante3, estudiante4, estudiante5, "arte")

    mejores["español"] = mejor_espanol
    mejores["matematicas"] = mejor_matematicas
    mejores["ciencias"] = mejor_ciencias
    mejores["literatura"] = mejor_literatura
    mejores["arte"] = mejor_arte

    return mejores

def mejor_en_materia(e1: dict, e2: dict, e3: dict, e4: dict, e5: dict, materia: str) -> str:
    nota_e1 = float(e1[materia])
    nota_e2 = float(e2[materia])
    nota_e3 = float(e3[materia])
    nota_e4 = float(e4[materia])
    nota_e5 = float(e5[materia])
    mejores = []
    result = max(nota_e1, nota_e2, nota_e3, nota_e4, nota_e5)
    if nota_e1 == result:
        mejores.append( e1['nombre'].lower() )
    if nota_e2 == result:
        mejores.append( e2['nombre'].lower() )
    if nota_e3 == result:
        mejores.append( e3['nombre'].lower() )
    if nota_e4 == result:
        mejores.append( e4['nombre'].lower() )
    if nota_e5 == result:
        mejores.append( e5['nombre'].lower() )
    
    mejor = min(mejores)
    return mejor
    
e1 = {"nombre": "sebastian", "español": 5.0, "literatura": 4.0, "ciencias": 4.0, "arte": 4.0, "matematicas": 4.0}
e2 = {"nombre": "ana", "español": 4.0, "literatura": 4.0, "ciencias": 4.0, "arte": 4.0, "matematicas": 4.0}
e3 = {"nombre": "carlos", "español": 4.0, "literatura": 5.0, "ciencias": 4.0, "arte": 4.0, "matematicas": 4.0}
e4 = {"nombre": "miguel", "español": 4.0, "literatura": 4.0, "ciencias": 5.0, "arte": 4.0, "matematicas": 4.0}
e5 = {"nombre": "john", "español": 4.0, "literatura": 4.0, "ciencias": 4.0, "arte": 5.0, "matematicas": 4.0}

print(mejor_de_cada_curso(e1,e2,e3,e4,e5))