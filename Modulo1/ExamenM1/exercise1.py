# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 09:07:28 2022

@author: SebastianCB-dev
"""
from math import sqrt

def vel_en_caida_libre(altura: float)->float:
    velocidad_final = sqrt(2 * 9.8 * altura)
    return round(velocidad_final, 2)

# Programa Principal

vel_en_caida_libre(12)