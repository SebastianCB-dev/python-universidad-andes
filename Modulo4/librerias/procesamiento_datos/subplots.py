
#!SUBPLOTS = Varias graficas por figura
# El orden de las graficas será de izquierda a derecha

import matplotlib.pyplot as plt

fig, axes = plt.subplots(2,3, figsize=(12,8), sharex=True, sharey=True)


num_ciudad = 0
for fila in axes:
    for ax in fila:
        ax.plot(meses, temps[num_ciudad], "r", label="temperatura")
        ax.set_xticklabels(meses)
        ax.set_xlabel("Meses")
        ax.set_ylabel("Temperatura")
        ax.set_title(nombres[num_ciudad])
        num_ciudad += 1

# recalcular las posiciones
plt.tight_layout()
fig.show()

# -------------------SUBPLOTS CON DOS SERIES---------------
fig, axes = plt.subplots(2,3, figsize=(12,8), sharex=True, sharey=True)

num_ciudad = 0
for fila in axes:
    for ax in fila:
        ax.plot(meses, temps[num_ciudad], "r", label="temperatura")
        ax.set_xticklabels(meses)
        ax.set_xlabel("Meses")
        ax.set_ylabel("Temperatura")
        ax.set_title(nombres[num_ciudad])
        ax2 = ax.twinx()
        ax2.plot(meses, precip[num_ciudad], "b", label="temperatura")

        num_ciudad += 1

plt.tight_layout()
