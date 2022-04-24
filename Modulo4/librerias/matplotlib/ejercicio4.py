# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 15:08:51 2022

@author: SebastianCB-dev
"""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

ruta_imagen = "descarga.jpg"

matriz = mpimg.imread(ruta_imagen).tolist()

nueva = []
alto = len(matriz)
ancho = len(matriz[0])

imagen = []
for i in range(alto):
    fila = []
    for j in range(ancho):
        r = matriz[i][j][0]
        g = matriz[i][j][1]
        b = matriz[i][j][2]
        if i == 0 or i == alto - 1 or j == 0 or j == ancho -1:
            fila.append([255-r, 255-g, 255-b])
        else:
            fila.append([sum([r,g,b])//3]*3)
    nueva.append(fila)
    
plt.imshow(nueva)