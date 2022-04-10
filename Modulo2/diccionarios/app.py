mi_diccionario = {}

mi_diccionario_de_paises = {"Colombia": "0", "Inglaterra": "1"}

# Saber si una clave existe devuelve True or False
print("Colombia" in mi_diccionario_de_paises)

result = mi_diccionario_de_paises.get("Holanda")
print(result)

# Longitud diccionario
print(len(mi_diccionario_de_paises))

# !MUTABILIDAD
# Los diccionarios son mutables

diccionario_equipos = {1: "Chelsea", 2: "Manchester City", 3: "Liverpool"}

alias = diccionario_equipos

#Metodo copy para evitar mutabilidad
copia_diccionario = diccionario_equipos.copy()

# Eliminar llave y valor, validar que exista primero
del copia_diccionario[1]