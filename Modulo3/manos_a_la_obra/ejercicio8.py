
def intercalar_palabras(cad1: str, cad2: str)->str:
    resultado = ""

    palabras_1 = cad1.split()
    palabras_2 = cad2.split()

    for i  in range(0, len(palabras_1)):
        resultado += (palabras_1[i] + " " + palabras_2[i] + " ")

    return resultado[:len(resultado)-1]

c_1 = "La casa está cerca río"
c_2 = "linda no muy del grande"

print(intercalar_palabras(c_1,c_2))