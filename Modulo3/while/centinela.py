def contar_digitos(numero: int) -> int:
    contador = 0
    terminar = False

    while terminar == False:
        if numero == 0:
            terminar = True
        else:
            contador += 1
            numero //= 10

    return contador

num = int(input("Ingrese un número entero: "))
digitos = contar_digitos(num)
print("La cantidad de dígitos del número es", digitos)

def calcular_factorial(n: int) -> int:
    terminar = False
    factorial = 1
    while terminar == False:
        if n == 0:
            terminar = True
        else:
            factorial *= n
            n -= 1
    return factorial

numero = int(input("Ingrese un número entero positivo: "))

while numero < 0:
    print("No se permiten números negativos")
    numero = int(input("Ingrese un entero positivo: "))

print(numero, "! es igual a", calcular_factorial(numero))