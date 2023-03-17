import pandas as pd

# Cargar datos
df_nuevas = pd.read_csv('notebooks.csv')
df_usadas = pd.read_csv('notebooks_usadas.csv')

# * Convertir a númerics los datos de precios
df_nuevas['precio'] = pd.to_numeric(df_nuevas['precio'], errors='coerce')
df_usadas['precio'] = pd.to_numeric(df_usadas['precio'], errors='coerce')

#####################################################################
#  Top 5 Notebooks más caras Nuevas vs Usadas
#####################################################################

# Ordenar el DataFrame por la columna 'precio' de manera descendente
df_nuevas_sorted = df_nuevas.sort_values('precio', ascending=False)
df_usadas_sorted = df_usadas.sort_values('precio', ascending=False)

# Tomar los primeros 5 valores
nuevas_top_5 = df_usadas_sorted.head(5)
usadas_top_5 = df_usadas_sorted.head(5)

# Calcular las métricas para cada categoría
precio_nuevas_mean = df_nuevas['precio'].mean()
precio_nuevas_median = df_nuevas['precio'].median()
precio_nuevas_percentiles = df_nuevas['precio'].quantile([0.25, 0.50, 0.75])

precio_usadas_mean = df_usadas['precio'].mean()
precio_usadas_median = df_usadas['precio'].median()
precio_usadas_percentiles = df_usadas['precio'].quantile([0.25, 0.50, 0.75])

# Crear los diccionarios con los valores calculados
diccionario_nuevas = {
    'categoria': 'nuevas',
    'precio': precio_nuevas_mean,
    'mediana': precio_nuevas_median,
    'percentil_25': precio_nuevas_percentiles[0.25],
    'percentil_50': precio_nuevas_percentiles[0.50],
    'percentil_75': precio_nuevas_percentiles[0.75]
}

diccionario_usadas = {
    'categoria': 'usadas',
    'precio': precio_usadas_mean,
    'mediana': precio_usadas_median,
    'percentil_25': precio_usadas_percentiles[0.25],
    'percentil_50': precio_usadas_percentiles[0.50],
    'percentil_75': precio_usadas_percentiles[0.75]
}

# Crear el DataFrame a partir de los diccionarios
df_merger = pd.DataFrame([diccionario_nuevas, diccionario_usadas])
df_merger.to_csv('database/estadisticas.csv')

# Mostrar el DataFrame resultante
def imprimir_analisis():
    print("Nuevas")
    print(nuevas_top_5)
    print("\n Usadas")
    print(usadas_top_5)
    print("\n Estadísticas")
    print(df_merger)
