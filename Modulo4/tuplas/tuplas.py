# Como funcionan las listas?
lista = [1,2,3,4,5,6,7,8,9]
print(lista)
# Se pueden modificar los datos
lista[2] = 9
# Se pueden añadir datos
lista.append(-1)

##################### !TUPLAS ##############################

tupla = (1,2,3,4,5,6,7,8)
type(tupla) #tuple
# tupla[1] = 1 --> ERROR 

# ? Es posible crear la tupla sin especificar los parentesis
tupla2 = 1,2,3
type(tupla2)

tupla_unitaria = (1,)

# Indexación es igual que en las listas
tupla_filatrada = tupla[:2]
len(tupla_filatrada) 


##! Empaquetado y desempaquetado

#Empaquetado
tupla_ejemplo = "Sebastian", "Carrillo", 21

#Desempaquetado
nombre, apellido, edad = tupla_ejemplo

print(nombre, apellido, edad)





