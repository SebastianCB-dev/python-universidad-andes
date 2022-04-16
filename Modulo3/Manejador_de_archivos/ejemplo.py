
archivo = open("Gabo.txt", "r")

#################### LECTURA ###################
# ! Si el archivo no existe python lo crea
linea = archivo.readline()

while linea != "":
    print(linea)
    linea = archivo.readline()

archivo.close

########## ESCRITURA #####################
archivo = open("Gabo.txt", "w")

archivo.write("Mi primer archivo escrito desde Python \n")
archivo.write("------ \n")
archivo.write("Hello World \n")

archivo.close()