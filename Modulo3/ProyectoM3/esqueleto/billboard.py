def cargar_canciones(nombre_archivo: str) -> list:
    """
    Esta función recibe como parametro un nombre de archivo a procesar
    y retorna en una lista todas las canciones que estan en el archivo.
    :param nombre_archivo: nombre del archivo a procesar
    :return: Lista de las canciones
    """
    lista_canciones = []
    archivo = open(f"{nombre_archivo}.csv", 'r')
    linea = archivo.readline()
    titles = linea.split(',')
    while linea != '':
        linea = archivo.readline()
        if len(linea) > 0:
            lista_canciones.append(crear_diccionario_cancion(linea.split(',')))
    archivo.close()
    return lista_canciones

def crear_diccionario_cancion(info: list) -> dict:
    """
    Esta función recibe las llaves y los valores de una canción y retorna un diccionario en base a esto.
    :param info: valores del diccionario
    :return: diccionario con la información recibida
    """
    cancion = {}
    cancion["posicion"] = info[0]
    cancion["nombre_cancion"] = info[1]
    cancion["nombre_artista"] = info[2]
    cancion["anio"] = int(info[3])
    cancion["letra"] = info[4]
    return cancion

def buscar_cancion_por_anio(canciones: list, nombre_cancion:str, anio: int) -> dict:
    """
    Función que busca una canción en base a un nombre y un año dentro de una lista.
    :param canciones: Lista de las canciones
    :param nombre_cancion: nombre de la canción a buscar
    :param anio: Año de la canción a buscar
    :return: Diccionario de la cancion encontrada, None si no fue encontrada
    """
    result_cancion = None
    for cancion in canciones:
        if cancion["nombre_cancion"] == nombre_cancion and cancion["anio"] == anio:
            result_cancion = cancion

    return result_cancion

def buscar_canciones_por_anio(canciones: list, anio: int) -> list:
    """
    Función que filtra por año una coleccion de canciones, y elimina la letra de las que fueron filtradas
    :param canciones: Lista de las canciones
    :param anio: Año en el cual se va a realizar el filtro
    :return: Lista con las canciones filtradas por año
    """
    canciones_filtradas = []

    for cancion in canciones:
        if cancion["anio"] == anio:
            del cancion["letra"]
            canciones_filtradas.append(cancion)

    return canciones_filtradas

def buscar_canciones_entre_anios_y_artista(canciones: list, nombre_artista: str, anio_inicial: int, anio_final: int) -> list:
    """
    Función que busca canciones de un artista en un rango de años
    :param canciones: Lista de todas las canciones
    :param nombre_artista: Nombre del artista a buscar
    :param anio_inicial: Año Inicial del filtrado
    :param anio_final: Año final del filtrado
    :return: Lista que compende las canciones con el filtrado anteriormente mencionado.
    """
    canciones_filtradas = []

    for cancion in canciones:
        if cancion["nombre_artista"] == nombre_artista:
            if anio_inicial <= cancion["anio"] <= anio_final:
                del cancion["letra"]
                canciones_filtradas.append(cancion)

    return canciones_filtradas

def buscar_canciones_de_artista(canciones: list, nombre_artista: str) -> list:
    """
    Función que busca todas las canciones de un artista en una lista
    :param canciones: lista de las canciones
    :param nombre_artista: Nombre del artista a filtrar
    :return: Lista con las canciones del artista, retorna vacio si no existe el artista
    """
    canciones_filtradas = []

    for cancion in canciones:
        if cancion["nombre_artista"] == nombre_artista:
            del cancion["letra"]
            canciones_filtradas.append(cancion["nombre_cancion"])

    return canciones_filtradas

def buscar_canciones_por_nombre(canciones: list, nombre_cancion: str)-> list:
    """
    Busca canciones por su nombre y retorna una lista de los artistas que la han interpretado
    :param canciones:
    :param nombre_cancion:
    :return:
    """
    nombre_artistas = []

    for cancion in canciones:
        if cancion["nombre_cancion"] == nombre_cancion:
            nombre_artistas.append(cancion["nombre_artista"])

    return nombre_artistas

def buscar_artistas_con_minimo_de_canciones(canciones: list, cantidad_minima: int) -> dict:
    """
    Función que busca artistas con un minimo de aparicion de canciones en la lista
    :param canciones:Lista con las canciones
    :param cantidad_minima: numero minimo de apariciones
    :return: Diccionario cuyas llaves son los nombres de los artistas que han tenido un número total de canciones (a lo largo de todos los años) superior a la cantidad recibida por parámetro y cuyos valores son la cantidad de canciones que ha tenido cada uno de los artistas.
    """

    conteo_canciones_artistas = {}

    #Conteo artistas
    for cancion in canciones:
        if not cancion["nombre_artista"] in conteo_canciones_artistas:
            conteo_canciones_artistas[cancion["nombre_artista"]] = 1
        else:
            conteo_canciones_artistas[cancion["nombre_artista"]] += 1

    # Eliminar las que no estan en el rango
    conteo_filtrado = {}
    for artista_key in conteo_canciones_artistas.keys():
        if conteo_canciones_artistas[artista_key] > cantidad_minima:
            conteo_filtrado[artista_key] = conteo_canciones_artistas[artista_key]

    return conteo_filtrado

def buscar_artista_con_mas_canciones(canciones: list) -> dict:
    """
    Recibe una lista de canciones y retorna el artista con mas apariciones en el rankin
    :param canciones: Lista de las canciones
    :return: Diccionario con clave del artista con mayor apariciones y el valor con la cantidad
    """
    conteo_canciones_artistas = {}
    #Conteo artistas
    for cancion in canciones:
        if not cancion["nombre_artista"] in conteo_canciones_artistas:
            conteo_canciones_artistas[cancion["nombre_artista"]] = 1
        else:
            conteo_canciones_artistas[cancion["nombre_artista"]] += 1

    artista_con_mas_canciones = {}
    artista_con_mas_canciones[list(conteo_canciones_artistas.keys())[0]] = list(conteo_canciones_artistas.values())[0]

    for artista_key in conteo_canciones_artistas.keys():
        if conteo_canciones_artistas[artista_key] > artista_con_mas_canciones[list(artista_con_mas_canciones.keys())[0]]:
            artista_con_mas_canciones.clear()
            artista_con_mas_canciones[artista_key] = conteo_canciones_artistas[artista_key]

    return artista_con_mas_canciones

def buscar_canciones_todos_los_artistas(canciones: list) -> dict:
    """
    Funcion que recibe una lista de canciones y retorna un diccionario como clave el nombre del artista y valor lista de las canciones de el
    :param canciones: Lista de canciones
    :return: Diccionario con los artistas y la lista de las canciones de ellos
    """
    canciones_artistas = {}
    for cancion in canciones:
        if not cancion["nombre_artista"] in canciones_artistas:
            canciones_artistas[cancion["nombre_artista"]] = [cancion["nombre_cancion"]]
        else:
            if not cancion["nombre_cancion"] in canciones_artistas[cancion["nombre_artista"]]:
                canciones_artistas[cancion["nombre_artista"]].append(cancion["nombre_cancion"])

    return canciones_artistas

def promedio_canciones_artistas(canciones: list) -> dict:
    """
    Funcion que calcula el promedio de canciones de un artista frente a otros
    :param canciones: Lista de las canciones
    :return: Promedio de cada artista
    """
    canciones_artistas = buscar_canciones_todos_los_artistas(canciones)
    tot_canciones = 0

    for cancion_key in canciones_artistas.keys():
        tot_canciones += len(canciones_artistas[cancion_key])

    promedio = tot_canciones / len(canciones_artistas)
    return promedio


