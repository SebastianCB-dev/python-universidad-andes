


def buscar_estudiante(est1: dict,
                      est2: dict,
                      est3: dict,
                      est4: dict,
                      nom: str) -> dict:
    buscado = None

    if est1['nombre'] == nom:
        buscado = est1
    elif est2['nombre'] == nom:
        buscado = est2
    elif est3['nombre'] == nom:
        buscado = est3
    elif est4['nombre'] == nom:
        buscado = est4

    return buscado

def crear_estudiante(nombre: str,
                     codigo: str,
                     genero: str,
                     carrera: str,
                     promedio: float,
                     ssc: int)-> dict:
    return {"nombre": nombre, "codigo": codigo, "genero": genero, "carrera": carrera, "promedio": promedio ,"ssc": ssc}
#PROGRAMA PRINCIPAL
e_1 = crear_estudiante('Lina', '2020101234', 'femenino','Sistemas', 4.78, 2)
e_2 = crear_estudiante('Sebastian','67000302','masculino','Civil',3.21,2)
e_3 = crear_estudiante('Diego', '67000293','masculino','Sistemas',3.89,2)
e_4 = crear_estudiante('Karen', '67020102102', 'femenino', 'Economía', 4.9,2)

nombre = input('Ingrese el nombre del estudiante a buscar: ')

est_buscado = buscar_estudiante(e_1,e_2,e_3,e_4,nombre)

if est_buscado is None:
    print('El estudiante no existe')
else:
    print(f'El estudiante existe y su codigo es {est_buscado["codigo"]}')