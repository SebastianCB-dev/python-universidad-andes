a = "Hola, \nmundo."

print(a)

a[-1] # Ultimo valor de la cadena

a[len(a)-1] # Ultimo valor de la cadena

a[-3] # ==  3 caracteres de atras para adelante ('d')
a[-len(a)] # Primer caracter de la cadena


### --------------------- Metodo FIND ---------------
c = "Un ejemplo = A."
c.find("=") # Retonar el indice 
c.find("ejem")
c.find("za") # Si no se encuentra, retorna -1

# --------------- Subcadenas -------------------
s = "Piratas del Caribe"

x = s[0:7]
print(x) # Piratas

y = s[8:11]
print(y) # del

z = s[12:18]
print(z) # Caribe

fruta = "manzana"
inicio = fruta[:3] # man

final = fruta[3:] # zana

fruta[:] # String completo

# !SALTO DE PASO EN CADENAS
fruta = "Guanabana"
cadena1 = fruta[::1] # salto de paso en 1
cadena1 = fruta[::2] # Salto de paso en 2
cadena1 = fruta[::-1] # Cadena al reves

