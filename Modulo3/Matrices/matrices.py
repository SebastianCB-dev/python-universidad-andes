M = [[1, 2, 3], [2, 12, 6], [1, 0, -3], [0, -1, 0]]

print(M[0][0]) # 1
print(M[0][1]) # 2
print(M[0][2]) # 3
print(M[1][0]) # 2
print(M[1][1]) # 12

M2 = [[0, 0], [0, 0]]
#Imprimir Matriz
print("", M[0], "\n", M[1])

# !Crear matrices grandes
# !Crea las matrices mal, puesto que todas las filas referencian al mismo arreglo
a = [0] * 6
M = [a] * 3

M[0][0] = 1 # Las anteriores lineas cada fila referencia al mismo arreglo

# Creación de matrices con filas independientes

M = []

for i in range(0, 3): # 3 * 6
    a = [0] * 6
    M.append(a)

print(M)
