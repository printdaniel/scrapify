import pandas as pd

class DataWork:
    def __init__(self):
        pass

    def load_data(self):
        # Cargar datos
        try:
            self.df_nuevas = pd.read_csv('exploratory_analysis/notebooks.csv')
            self.df_usadas = pd.read_csv('exploratory_analysis/notebooks_usadas.csv')
        except FileNotFoundError as e:
            print("Archivo no encontrado", e)


    def format_data_type(self):
        # * Convertir a númerics los datos de precios
        self.df_nuevas['precio'] = pd.to_numeric(self.df_nuevas['precio'], errors='coerce')
        self.df_usadas['precio'] = pd.to_numeric(self.df_usadas['precio'], errors='coerce')
        print("Esto esta bien")

    def data_analystic(self):
        #############################################
        #  Top 5 Notebooks más caras Nuevas vs Usadas
        #############################################
        
        # Ordenar el DataFrame por la columna 'precio' de manera descendente
        self.df_nuevas_sorted = self.df_nuevas.sort_values('precio', ascending=False)
        self.df_usadas_sorted = self.df_usadas.sort_values('precio', ascending=False)
        
        # Tomar los primeros 5 valores
        self.nuevas_top_5 = self.df_usadas_sorted.head(5)
        self.usadas_top_5 = self.df_usadas_sorted.head(5)
        
        # Calcular las métricas para cada categoría
        self.precio_nuevas_mean = self.df_nuevas['precio'].mean()
        self.precio_nuevas_median = self.df_nuevas['precio'].median()
        self.precio_nuevas_percentiles = self.df_nuevas['precio'].quantile([0.25, 0.50, 0.75])

        self.precio_usadas_mean = self.df_usadas['precio'].mean()
        self.precio_usadas_median = self.df_usadas['precio'].median()
        self.precio_usadas_percentiles = self.df_usadas['precio'].quantile([0.25, 0.50, 0.75])
        print("This is fine")


    def data_export(self):
        # Crear los diccionarios con los valores calculados
        diccionario_nuevas = {
            'categoria': 'nuevas',
            'precio': self.precio_nuevas_mean,
            'mediana': self.precio_nuevas_median,
            'percentil_25': self.precio_nuevas_percentiles[0.25],
            'percentil_50': self.precio_nuevas_percentiles[0.50],
            'percentil_75': self.precio_nuevas_percentiles[0.75]
        }
        
        diccionario_usadas = {
            'categoria': 'usadas',
            'precio': self.precio_usadas_mean,
            'mediana': self.precio_usadas_median,
            'percentil_25': self.precio_usadas_percentiles[0.25],
            'percentil_50': self.precio_usadas_percentiles[0.50],
            'percentil_75': self.precio_usadas_percentiles[0.75]
        }
        
        # Crear el DataFrame a partir de los diccionarios
        self.df_merger = pd.DataFrame([diccionario_nuevas, diccionario_usadas])
        self.df_merger.to_csv('database/estadisticas.csv')

    def imprimir_analisis(self):
        # Mostrar el DataFrame resultante
        print("Nuevas")
        print(self.nuevas_top_5)
        print("\n Usadas")
        print(self.usadas_top_5)
        print("\n Estadísticas")
        print(self.df_merger)



if __name__ == '__main__':
    dtw = DataWork()
    dtw.load_data()
    dtw.format_data_type()
    dtw.data_analystic()
    dtw.data_export()
