"""
Modificacion
- Asignacion simple
- Modificacion con loc
- Modificacion con iloc

Ordenamiento
"""
import pandas as pd
import random as np

serie = pd.Series(np.random.normal(100,20,1000))

# Ordenamiento

serie.sort()
serie.sort_index()

# Asignación
copia = serie.copy()
copia[500] = 180

copia[0:100]= 20

copia[900:1000] = [40] * 100

copia.iloc[500] = 180