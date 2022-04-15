numeros = [10,20,30,40]

print(numeros)

nombres = ["Sebastian", 'John', 'Javier', 'Miguel']

print(nombres)

a = [1, 1+1, 6 // 2]

print(a)

# Lista variada
lista_variada = ["hola", 2.5, 5, [10,20]]

len(lista_variada) # 4

c = [5,6] + [7,8] # [5,6,7,8]

# Corte
z = [1,2,3,4,5]
z[1:3] # 2,3 
z[1:-1] #  2,3,4

#Creación listas
a = list(range(1,4)) 
print(a) #1,2,3

j = [0] * 10
print(j) # [0,0,0,0,0,0,0,0,...]

# Eliminación de items en una lista
lista = ["a","b","c","d","e","f"]
print(lista)
lista[1:3] = []
print(lista) # ["a","d","e","f"] 

# Agregando elementos en un indice

lista = ["a","d","f"]
print(lista)

lista[1:1] = ["b","c"]
print(lista) #["a","b","c","d","f"]

a = ["uno","dos", "tres"]
del a[1]
del a[:1]




