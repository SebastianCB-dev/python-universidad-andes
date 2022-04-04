# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 07:10:20 2022

@author: SebastianCB-dev
"""

def calcular_IMC(peso: float, altura: float)-> float:
    """
    Calcula el índice de masa corporal de una persona a partir de la ecuación

    Parametros
    -------
    peso    (float) -> Peso de la persona en kilogramos (kg)
    altura  (float) -> Altura de la persona en metros (m)
    
    Returns
    -------
    return  (float) -> índice de masa corporal de la persona

    """
    
    return round(peso / (altura ** 2), 2)

def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float)-> float:
    """
    Calcula el porcentaje de grasa de una persona a partir de la ecuación

    Parametros
    -------
    peso         (float) -> Peso de la persona en kilogramos (kg)
    altura       (float) -> Altura de la persona en metros (m)
    edad         (int)   -> Edad de la persona en años
    valor_genero (float) -> Valor que varía segun el genero de la persona: en caso de ser masculino debe ser 10.8 y en caso de ser femenino debe ser 0.
    
    Returns
    -------
    return       (float) -> Porcentaje de grasa que tiene el cuerpo de la persona.

    """
    return round(1.2 * calcular_IMC(peso, altura) + 0.23 * edad - 5.4 - valor_genero, 2)

def calcular_calorias_en_reposo( peso: float, altura: float, edad: int, valor_genero: float) -> float:
    """
    Calcula la cantidad de calorías que una persona quema estando en reposo (esto es, su tasa metabólica basal), a partir de la ecuación 
    
    Parametros
    -------
    peso            (float) -> Peso de la persona en kilogramos (kg)
    altura          (float) -> Altura de la persona en metros (m)
    edad            (int)   -> Edad de la persona en años
    valor_genero    (float) ->Valor que varía segun el genero de la persona: en caso de ser masculino debe ser 5 y en caso de ser femenino debe ser -161.
    
    Returns
    -------
    return (float) -> La cantidad de calorías que la persona quema en reposo.

    """
    return round((10* peso) + (6.25 * altura)- (5 * edad) + valor_genero, 2)


def calcular_calorias_en_actividad( peso: float, altura: float, edad: int, valor_genero: float, valor_actividad: float) -> float:
    """
    Calcula la cantidad de calorías que una persona quema al realizar algún tipo de actividad física (esto es, su tasa metabólica basal según actividad física), a partir de la ecuación 
    
    Parametros
    -------
    peso            (float) -> Peso de la persona en kilogramos (kg)
    altura          (float) -> Altura de la persona en metros (m)
    edad            (int)   -> Edad de la persona en años
    valor_genero    (float) -> Valor que varía segun el genero de la persona: en caso de ser masculino debe ser 5 y en caso de ser femenino debe ser -161.
    valor_actividad (float) -> Valor que depende de la actividad física semanal y toma los valores descriptos anteriormente
    
    Returns
    -------
    return          (float) -> La cantidad de calorías que la persona quema en reposo.

    """
    return round(calcular_calorias_en_reposo(peso, altura, edad, valor_genero) * valor_actividad, 2)


def consumo_calorias_recomendado_para_adelgazar( peso: float, altura: float, edad: int, valor_genero: int) -> str:
    """
    Calcula el rango de calorías recomendado, que debe consumir una persona diariamente en caso de que desee adelgazar, a partir de la ecuación 

    Parametros
    -------
    peso            (float) -> Peso de la persona en kilogramos (kg)
    altura          (float) -> Altura de la persona en metros (m)
    edad            (int) -> Edad de la persona en años
    valor_genero    (float) -> Valor que varía segun el genero de la persona: en caso de ser masculino debe ser 5 y en caso de ser femenino debe ser -161.
    
    Returns
    -------
    return          (str) -> Una cadena indicando el rango de calorías que una persona debe consumir si desea adelgazar. El formato de la cadena debe ser:  ﻿"Para adelgazar es recomendado que consumas entre: XXX y ZZZ calorías al día.". Siendo XXX el rango inferior y ZZZ el rango superior.  
    """
    TMB = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    return f'Para adelgazar es recomendado consumir entre {round(TMB * 80 / 100, 2)} y {round(TMB * 85 / 100, 2)} calorías.'
    
