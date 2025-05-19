import pandas as pd
import re

# Cargar los archivos Excel
instalaciones = pd.read_excel('/run/media/andrei/Disco ext/Trabajo/Sincatel/INSTALACIONES.xlsx')
clientes = pd.read_excel('/run/media/andrei/Disco ext/Trabajo/Sincatel/CLIENTES.xlsx')

# Eliminar las columnas que no se necesitan
clientes.drop('NOMBRE', axis=1, inplace=True)
# instalaciones.drop('DIRECCION', axis=1, inplace=True)
instalaciones.drop('CIF', axis=1, inplace=True)

# Reemplazar los valores de cadenas vacias por NAN
instalaciones.replace('', pd.NA, inplace=True)
clientes.replace('', pd.NA, inplace=True)

# Eliminar todas las columnas que esten vacias enteras
instalaciones.dropna(axis=1, how='all', inplace=True)
clientes.dropna(axis=1, how='all', inplace=True)

# Unir los datos de instalaciones y clientes
datos = pd.merge(clientes, instalaciones, on='COD_CLI', how="inner", validate="one_to_many")

# Regex pattern to match xml closing tags
pattern = r'\</(.*?)\>'

columns = datos['CAMPOS_DEF_USUARIO']

# Change to plain text
try:
    for index, column in enumerate(columns):
        # Ensure the column value is not null
        if pd.notna(column):
            regex_results = re.findall(pattern, str(column))
            extracted_value = ''
            for result in regex_results:
                extracted_value = extracted_value + f'{result}: {column.split(f'<{result}>')[1].split(f'</{result}>')[0]} \n'

            datos.at[index, 'CAMPOS_DEF_USUARIO'] = extracted_value
        else:
            datos.at[index, 'CAMPOS_DEF_USUARIO'] = '[Empty]'
except Exception as e:
    print(f'Unexpected error processing excel file: {e}')

datos.to_excel("Clientes_Instalaciones.xlsx", index=False)

