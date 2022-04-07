def son_colineales(x1: int, y1: int,
                   x2: int, y2: int,
                   x3: int, y3: int)->bool:
    
    pendiente_1 = calcular_pendiente(x1,y1,x2,y2)
    pendiente_2 = calcular_pendiente(x2,y2,x3,y3)

    return pendiente_1 == pendiente_2

def calcular_pendiente(x1: int, y1: int,
                       x2: int, y2: int)->int:
    return (y2-y1)/(x2-x1)

#print(son_colineales(-5,3,-1,-3,1,-6))
print(son_colineales(-5,3,-1,-3,1,6))