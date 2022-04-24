"""
Extraer información
Operaciones matematicas
Operaciones estadisticas, etc.
"""
import pandas as pd

data = {1:2,2:4,3:8,4:16,5:32}
serie = pd.Series(data,name="datos")


# Extraer valores
print(serie.get(2))
print(serie.get(10)) # None

print(serie.iloc[2:4]) # por posicion
print(serie.loc[2:4]) # por indice o clave

# Extraer todos los valores

print(serie.values)
numeros = serie.tolist() # Array
print(numeros) # Array

copia = serie.copy()


# ! OPERACIONES (+ - * / )

serie_nueva = serie + 1
print("Serie nueva".center(50, "#"))
print(serie_nueva)
print("Serie Antigua".center(50, "#"))
print(serie)

# * Se pueden sumar series entre si pero tener cuidado con los indices deben tener los mismos

serie_sumada = serie.add(serie, fill_value=0)

# ! Operaciones estadísticas

serie.max()     # Maximo valor
serie.min()     # Minimo valor
serie.mean()    # Promedio
serie.std()     # Desviacion estandar
serie.median()  # calcula la mediana

