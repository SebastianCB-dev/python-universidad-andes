a = [1,2,3]
b = [1,2,3]

c = a

# Si apuntan al mismo espacio de memoria

print( a is b )
print( a is c )
print( b is c )

# Si dos variables apuntan a la misma direccion de memoria
# El objeto si se modifica cambiara en las dos que apuntan al mismo espacio de memoria

c[0] = 4
print(a)
print(c)

# Recomendable hacer copia
# ! Copias , Cloning

z = a[:]
y = a.copy()
