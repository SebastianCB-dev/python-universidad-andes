import matplotlib.pyplot as plt

meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
temperaturas_bog = [14.3, 14.3, 15.0, 14.7, 14.7, 14.5, 14.3, 14.2, 14.3, 14.3, 14.5, 14.4]
precipitacion_bog = [5,5,5,5,5,5,5,5,5,5,5,5]

# Figura Base
fig = plt.figure(figsize=(7,4))

color_fondo = "#444444"
color_temp = "#FFAF5E"
color_prec = "#3399DC"

ax = fig.add_axes([0.1,0.1,0.8,0.8])
# background
ax.set_facecolor(color_fondo)

#Transparencia en el fondo de la figura
ax.set_alpha(0.9)

ax.plot(meses, temperaturas_bog,color=color_temp,
       linewidth=0.75, linestyle="--",
       marker='s', markersize=8, markerfacecolor="red",
       label="temperatura")
# Style = s, o
ax.set_xlabel("Meses")
ax.set_ylabel("Temperatura", color=color_temp)
ax.set_title("Temp...")

ax2 = ax.twinx()
ax2.plot(meses, precipitacion_bog, color=color_prec,linewidth=1.25, label="precipitacion")
ax2.set_ylabel("Precipitación", color=color_prec)




