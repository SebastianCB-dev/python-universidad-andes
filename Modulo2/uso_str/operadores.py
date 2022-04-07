print("a" < "aa")
print("á" < "a")
print("A" < "a")
print("A" < "á")

ss = 'Hola, Mundo!'
tt = ss.upper() # Todo Mayus

ll = tt.lower() # Todo Minus

hh = ss.title() # Capitalizar palabras

qq = ss.swapcase() # Reverse de mayusculas y minusculas

aa = 'Un pequeño ejemplo'
bb = aa.replace("pequeño", "gran")
print(bb)

c = 'Un Ejemplo = A.'
print(c.find("=")) # Si esta nos devuelve el indice de su primera aparición. Si no está, devuelve el valor -1
print(c.find("!")) # -1 porque no esta en c

print("Hola, Mundo!".count("o")) # Cuenta cuantas veces esta la cadena en otra cadena

## METODO FORMAT
# Formatear una cadena

n1 = 4
n2 = 5
s3 = "2**10 = {0} y {1} * {2} = {3:.3f}".format(2**10, n1,n2, n1*n2)
#help('FORMATTING') -> Documentation

h1 = "Simon Jose Antonio"
h2 = "de la Santísima Trinidad"
h3 = 'Bolívar y Palacios'

print("PI con tres decimales es {0:.3f}".format(3.1415926))
print("123456789  123456789  123456789")
print("|||{0:<25}|||{1:^25}|| |{2:>25}|||nació en {3}|||".format(h1,h2,h3,2001))