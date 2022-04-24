# Ejes de referencias
# Configuración de textos

"""
    En el set_ylabel():
        - style="italic"
        - fontweight="bold"

"""


# ! recorrer valores de un eje para darles color

for label in ax.get.yticklabels():
    label.set_color("#fff")

# Cambios en los rangos
# Limitar los rangos
ax.set_ylim(10, 20)
