mi_lista = []

#Agrega al final de la lista
mi_lista.append(4)
mi_lista.append(27)
mi_lista.append(3)
mi_lista.append(29)
mi_lista.append(19)

print(mi_lista)

# Insertar en una posición indicada (Indice, Object)
mi_lista.insert(1,12)

# Cuantas veces aparece un elemento en la lista
print(mi_lista.count(4))

# Insertar una lista al final de otra
mi_lista.extend([5,6,4,2,0,12])
print(mi_lista)

# Buscar indice del primer elemento dado (Object) 
mi_lista.index(1)

# Revertir lista
mi_lista.reverse()

#Ordenar lista
mi_lista.sort()

# Remover elemento
mi_lista.remove(1)

# Copy Cloning de una lista
otra_lista = mi_lista.copy()

# Eliminar un elemento pasando indice
otra_lista.pop(1)

# Limpiar lista
mi_lista.clear()