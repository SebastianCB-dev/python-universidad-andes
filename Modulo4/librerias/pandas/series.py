"""
Series:
    Una serie son muchos registros, ordenados seun algun criterio
    El mismo tipo de dato para todas las columnas
    Un nombre que describe la serie
    !Tiene un índice y un valor, puede ser repetidas
"""

import pandas as pd

datos = [19,18,29,14,20,20,20,20,19]
temperaturas = pd.Series(datos, name="Temperaturas en Bogotá")
print(temperaturas)

print(type(temperaturas))

print(type(temperaturas.values))

print(type(temperaturas.dtypes))


# ------- SERIES CON INDICES ESPECIFICOS
fechas = ["5/11/20","6/11/20","7/11/20","8/11/20","9/11/20","10/11/20","11/11/20","12/11/20","13/11/20"]

temperaturas2 = pd.Series(datos, index=fechas, name="Temperaturas en Bogotá")
print(temperaturas2)

# ------------ SERIES CON DICCIONARIOS

parejas = {'5/11/20': 19,'6/11/20': 18,'7/11/20': 29,
           '8/11/20': 14,'9/11/20': 20,'10/11/20': 20,
           '11/11/20': 20,'12/11/20': 20,'13/11/20': 19,}

temperaturas3 = pd.Series(parejas)


# Reconstruir indices
temperaturas = temperaturas.reset_index(drop = True)
