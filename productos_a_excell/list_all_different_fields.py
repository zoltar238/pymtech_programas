import pandas as pd


# Cargar los datos
dataframe = pd.read_excel("Clientes_Instalaciones.xlsx")

difenrentes = []

for material in dataframe["MATERIAL"]:
    if material not in difenrentes:
        difenrentes.append(material)

print(difenrentes)