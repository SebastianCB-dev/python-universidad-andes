"""
Ejercicio nivel 2: Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2

NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """    
    pelicula = { "nombre": nombre, "genero": genero, "duracion": duracion, "anio": anio, "clasificacion": clasificacion, "hora": hora, "dia": dia }

    return pelicula

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
    result = None
    if nombre_pelicula == p1['nombre']:
        result = p1
    elif nombre_pelicula == p2['nombre']:
        result = p2
    elif nombre_pelicula == p3['nombre']:
        result = p3
    elif nombre_pelicula == p4['nombre']:
        result = p4
    elif nombre_pelicula == p5['nombre']:
        result = p5
    return result

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
    mas_larga = p1
    if p2['duracion'] > mas_larga['duracion']:
        mas_larga = p2
    if p3['duracion'] > mas_larga['duracion']:
        mas_larga = p3
    if p4['duracion'] > mas_larga['duracion']:
        mas_larga = p4
    if p5['duracion'] > mas_larga['duracion']:
        mas_larga = p5
    return mas_larga

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    promedio = (p1['duracion'] + p2['duracion'] + p3['duracion'] + p4['duracion'] + p5['duracion']) // 5
    if promedio < 60:
        result = f"00:{promedio}"
    else:
        horas = promedio // 60
        minutos = promedio - (horas * 60)
        if horas < 10:
            horas = '0' + str(horas)
        if minutos < 10:
            minutos = '0' + str(minutos)
        result = f"{horas}:{minutos}"
    return f"La duración promedio de las peliculas es: {result}"

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    result = []
    if p1['anio'] > anio:
        result.append(p1['nombre'])
    if p2['anio'] > anio:
        result.append(p2['nombre'])
    if p3['anio'] > anio:
        result.append(p3['nombre'])
    if p4['anio'] > anio:
        result.append(p4['nombre'])
    if p5['anio'] > anio:
        result.append(p5['nombre'])
    if len(result) == 0:
        result = 'Ninguna'
    elif len(result) == 1:
        result = result[0]
    elif len(result) > 1:
        result = ','.join(result)
    return result

def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    count = 0
    if p1['clasificacion'] == '18+':
        count += 1
    if p2['clasificacion'] == '18+':
        count += 1
    if p3['clasificacion'] == '18+':
        count += 1
    if p4['clasificacion'] == '18+':
        count += 1
    if p5['clasificacion'] == '18+':
        count += 1
    return count

def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    result = True
    pelicula_generos = peli['genero'].split(',')
    if se_cruza(nueva_hora, p1, nuevo_dia) or se_cruza(nueva_hora, p2, nuevo_dia) or se_cruza(nueva_hora, p3, nuevo_dia) or se_cruza(nueva_hora, p4, nuevo_dia) or se_cruza(nueva_hora, p5, nuevo_dia):
        result = False
    elif control_horario:
        if 'Documental' in pelicula_generos and nueva_hora >= 2200:
            result = False
        elif 'Drama' in pelicula_generos and nuevo_dia == 'Viernes':
            result = False
        elif (nuevo_dia == 'lunes' or nuevo_dia == 'martes' or nuevo_dia == 'miércoles' or nuevo_dia == 'jueves' or nuevo_dia == 'viernes') and (nueva_hora >= 2300 and nueva_hora <= 600):
            result = False
        else:
            result = True
    else:
        result = True

    return result

def se_cruza(nueva_hora: int, pelicula: dict, nuevo_dia: str) -> bool: 
    return  nueva_hora >= pelicula['hora'] and (nueva_hora <= pelicula['hora'] + pelicula['duracion']) and nuevo_dia == pelicula['dia']

def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la
       pelicula que entra igualmente por parametro.
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    result = False
    generos_pelicula = peli['genero'].split(',')
    if edad_invitado >= 18:
        result = True
    else:
        vc = validar_clasificacion(edad_invitado, peli)
        if (edad_invitado < 15 and ('Terror' in generos_pelicula)) or (edad_invitado <= 10 and (len(generos_pelicula) > 1)or (not 'Familiar' in generos_pelicula)) or not vc:
            if autorizacion_padres: 
                result = False
            else: 
                result = True 
    return result

def validar_clasificacion(edad, peli) -> bool:
    result = True
    clasificacion = peli['clasificacion']
    if clasificacion == 'todos':
        result = True
    else: 
        clasificacion = clasificacion[:-1]

        if edad <= int(clasificacion):
            result = False
        else: 
            result = True
    return result









