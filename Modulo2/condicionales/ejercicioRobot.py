def movimiento_robot(orientacion_actual: str,
                     giro_1: str, 
                     giro_2: str,
                     giro_3: str)-> str:

    orientation = hacerGiro(orientacion_actual, giro_1)
    orientation = hacerGiro(orientation, giro_2)
    orientation = hacerGiro(orientation, giro_3)
    
    return str(orientation)
        
def hacerGiro(orientacion: str, giro: str)->str:
    if orientacion == 'N':
            if giro == 'L':
                result = 'W'
            elif giro == 'R':
                result = 'E'
            elif giro == 'H':
                result = 'S'
            else:
                result = 'N'


    elif orientacion == 'S':
            if giro == 'L':
                result = 'E'
            elif giro == 'R':
                result = 'W'
            elif giro == 'H':
                result = 'N' 
            else:
                result = 'S'


    elif orientacion == 'W':
            if giro == 'L':
                result = 'S'
            elif giro == 'R':
                result = 'N'
            elif giro == 'H':
                result = 'E'
            else:
                result = 'W'
    else:
            if giro == 'L':
                result = 'N'
            elif giro == 'R':
                result = 'S'
            elif giro == 'H':
                result = 'W'
            else: 
                result = 'E'

    return result
    


