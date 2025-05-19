import pandas as pd

# Cargar los archivos Excel
instalaciones = pd.read_excel('/run/media/andrei/Disco ext/Trabajo/Sincatel/INSTALACIONES.xlsx')
clientes = pd.read_excel('/run/media/andrei/Disco ext/Trabajo/Sincatel/CLIENTES.xlsx')

# Convertir columnas a enteros (usando Int64 para manejar valores nulos)
instalaciones['COD_CLI'] = pd.to_numeric(instalaciones['COD_CLI'], errors='coerce').astype('Int64')
clientes['COD_CLI'] = pd.to_numeric(clientes['COD_CLI'], errors='coerce').astype('Int64')

# Obtener conjuntos de valores únicos (usando sets para comparación rápida)
valores_instalaciones = set(instalaciones['COD_CLI'].dropna())
valores_clientes = set(clientes['COD_CLI'].dropna())

# Encontrar valores que están en instalaciones pero no en clientes
solo_en_instalaciones = valores_instalaciones - valores_clientes
# Encontrar valores que están en clientes pero no en instalaciones
solo_en_clientes = valores_clientes - valores_instalaciones

# Crear lista de diferencias
diferencias = []

# Añadir valores que están en instalaciones pero no en clientes
for cliente in solo_en_instalaciones:
    indices = instalaciones.index[instalaciones['COD_CLI'] == cliente].tolist()
    for indice in indices:
        diferencias.append({
            'indice_fila': indice + 1,
            'valor': cliente,
            'mensaje': f'CLIENTES.xlsx no contiene el valor: {cliente}'
        })

# Añadir valores que están en clientes pero no en instalaciones
for cliente in solo_en_clientes:
    indices = clientes.index[clientes['COD_CLI'] == cliente].tolist()
    for indice in indices:
        diferencias.append({
            'indice_fila': indice,
            'valor': cliente,
            'mensaje': f'INSTALACIONES.xlsx no contiene el valor: {cliente}'
        })

# Mostrar estadísticas
print(f"Total de valores únicos en INSTALACIONES.xlsx: {len(valores_instalaciones)}")
print(f"Total de valores únicos en CLIENTES.xlsx: {len(valores_clientes)}")
print(f"Valores que están en INSTALACIONES pero no en CLIENTES: {len(solo_en_instalaciones)}")
print(f"Valores que están en CLIENTES pero no en INSTALACIONES: {len(solo_en_clientes)}")

# Mostrar diferencias
print(f"\nSe han encontrado {len(diferencias)} diferencias:")
for diferencia in diferencias[:20]:  # Mostrar primeras 20 diferencias para no saturar la salida
    print(diferencia)

if len(diferencias) > 20:
    print(f"... y {len(diferencias) - 20} más")

# Calcular porcentaje de equivalencia de valores únicos
total_valores_unicos = len(valores_instalaciones.union(valores_clientes))
valores_comunes = len(valores_instalaciones.intersection(valores_clientes))
porcentaje_equivalencia = (valores_comunes / total_valores_unicos) * 100 if total_valores_unicos > 0 else 100

print(f"\nPorcentaje de equivalencia: {porcentaje_equivalencia:.2f}%")
print(f"Valores comunes: {valores_comunes}")
print(f"Total de valores únicos combinados: {total_valores_unicos}")

# Opcional: Guardar los resultados en un Excel
df_diferencias = pd.DataFrame(diferencias)
if not df_diferencias.empty:
    df_diferencias.to_excel('diferencias_detalladas.xlsx', index=False)
    print("\nLos resultados detallados se han guardado en 'diferencias_detalladas.xlsx'")