import pandas as pd

# Cargar los datos
dataframe = pd.read_excel("Clientes_Instalaciones.xlsx")

# Función para clasificar el tipo de instalación
def clasificar_material(row):
    material = str(row["MATERIAL"]).upper()
    campos = str(row["CAMPOS_DEF_USUARIO"])

    if material == "A":
        return campos, "", "", ""
    elif material.startswith("CCTV"):
        return "", campos, "", ""
    elif material.startswith("INTERFONIA"):
        return "", "", campos, ""
    else:
        return "", "", "", campos

# Aplicar la función a cada fila
dataframe[["antenna_instal_existente", "cctv_instal_existente", "intercom_instal_existente", "otros_instal_existente"]] = dataframe.apply(clasificar_material, axis=1, result_type="expand")

# Reemplazar NaNs por cadenas vacías antes del groupby
dataframe.fillna("", inplace=True)

# Agrupar por cliente y combinar los valores sin duplicados
dataframe_grouped = dataframe.groupby("COD_CLI", as_index=False).agg(lambda x: ' / '.join(sorted(set(filter(None, map(str, x))))))

# Guardar el resultado
dataframe_grouped.to_excel("Clientes_Instalaciones_unicos.xlsx", index=False)
