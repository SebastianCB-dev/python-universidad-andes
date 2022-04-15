# De cadena a lista 
cadena = "uno dos tres"

lista = cadena.split()

print(lista)

cadena_dos = "Hola,cómo,estás?"

lista_dos = cadena_dos.split(",")

# De lista a cadena
a = " ".join(["uno", "dos", "tres"])

# Función list

a = list(range(1,4))
print(a) # [1,2,3]

b = list("1234567890")
print(b) # ["1","2","3"...]

c = list("La casa de papel")
print(c) # ["L","a", " ", "c","a"...]

# d = list(1212121212) -> ERROR, convertir a str