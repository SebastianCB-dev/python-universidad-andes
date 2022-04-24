# Plots nos sirven para mostrar graficas
# !Twins = Ejes gemelos, mezcla de graficas

import matplotlib.pyplot as plt
# Ejemplo basico
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
temperaturas_bog = [14.3, 14.3, 15.0, 14.7, 14.7, 14.5, 14.3, 14.2, 14.3, 14.3, 14.5, 14.4]

plt.plot(meses,temperaturas_bog)

# Configuración básica

# Definir una figura de tamaño 7 x 4
plt.figure(figsize=(7,4))

# Visualizar los datos
plt.plot(meses, temperaturas_bog, label="temperatura")
plt.xlabel("Meses")
plt.ylabel("Temperatura")
plt.title("Temperatura promedio en Bogotá, por mes (1970-2000)")

# Mostrar el label del plot
plt.legend()

# ------------------------------- AXES ----------------------------------

fig = plt.figure(figsize=(7,4))
# [Izquierda, Abajo, Ancho, Alto] con respecto a el figsize en porcentajes
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(meses, temperaturas_bog, label="temperatura")
ax.set_xlabel("Meses")
ax.set_ylabel("Temperatura")
ax.set_title("Temperatura promedio en Bogotá, por mes (1970-2000)")
ax.legend()

fig.show()
# !Guardar figura en archivo
#fig.savefig("imagen.png")

# -------------------------- GRAFICAS MULTIPLES -----------------
precipitacion_bog = [5,5,5,5,5,5,5,5,5,5,5,5]

fig = plt.figure(figsize=(7,4))
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(meses,temperaturas_bog, label="temperatura")
ax.plot(meses, precipitacion_bog, label="precipitacion")
ax.set_xlabel("Meses")
ax.set_ylabel("Valores")
ax.set_title("Temperatura y precipitacion promedio en Bogotá, por mes (1970-2000)")
ax.legend()

# -------------------------- TWINS ----------------------------
# !Doble eje con dos variables en una gráfica

fig = plt.figure(figsize=(7,4))
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(meses,temperaturas_bog, "r", label="temperatura")
ax.set_xlabel("Meses")
ax.set_ylabel("Temperatura", color="red")
ax.set_title("Temperatura y precipitacion promedio en Bogotá, por mes (1970-2000)")

ax2 = ax.twinx()
ax2.plot(meses, precipitacion_bog, "b", label="precipitacion")
ax2.set_ylabel("Precipitación", color="blue")
