# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 11:08:00 2022

@author: sebas
"""

def fahrenheit_to_centigrades( fahrenheit_grades: float) -> float:
    cent_grades = (fahrenheit_grades - 32) * (5 / 9)
    return cent_grades

def centigrades_to_fahrenheit( centigrades_grades: float ) -> float:
    fahr_grades = (centigrades_grades * 9/5) + 32
    return fahr_grades
    
def radianes_to_grades( radianes: float) -> float:
    pi = 3.14159
    return (360*radianes)/(2*pi)
    
def grades_to_radianes( grades: float) -> float:
    pi = 3.14159
    return (grades * 2*pi) / 360

def invert_number( num: int) -> int:
    unidades = num % 10
    num //= 10
    decenas = num % 10
    num //= 10
    centenas = num % 10
    num //= 10
    millares = num % 10
    inverso = (unidades * 1000) + (decenas * 100) + (centenas * 10) + (millares)
    return inverso

print(fahrenheit_to_centigrades(90))

print(centigrades_to_fahrenheit(32))

print(radianes_to_grades(20))

print(grades_to_radianes(360))

print(invert_number(1234))




