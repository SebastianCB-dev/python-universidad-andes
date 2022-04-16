
n = int(input("Ingrese el tamaño de la matriz identidad: "))

m = []
i = 0

while i < n:
    fila_nueva = [0] * n
    fila_nueva[i] = 1
    m.append(fila_nueva)
    i += 1

for fila in m:
    print(fila)
