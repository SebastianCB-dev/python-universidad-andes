#Pedimos la dimensión de la matriz
m = int(input("Digite el número de filas: "))
n = int(input("Digite el número de columnas: "))

#Creamos una matriz nula...
M = []
for i in range(0,m):
    M.append([0] * n)

#Setear datos
for i in range(0, m):
    for j in range(0, n):
        M[i][j] = float(input("Digite el contenido de la casilla ["+str(i)+"]["+str(j)+"]: "))

print("La matriz completa es: ")

for i in range(0, m):
    print(M[i])


# Dimension
a = [[1, 0], [0, 1], [0, 0]]
print(len(a[1])) # 2


