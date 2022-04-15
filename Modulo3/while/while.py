
from math import sqrt

x = float(input("Digite un número positivo: "))
while x < 0:
    print("No puede ingresar números negativos")
    x = float(input("Digite un número positivo: "))

print("La raíz cuadrada de {0} es {1}".format(x, sqrt(x)))