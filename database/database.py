##########################################
from datetime import datetime
from .constantes import *
import psycopg2
import pandas as pd
from psycopg2.extras import execute_values
from IPython.display import display
##########################################

try:
    csv_file = "database/estadisticas.csv"
except FileExistsError:
    raise "El archivo estadística no se encuentra"


class DataBase:

    def __init__(self):
        self.connection = self.conexion()
        self.create_table()

    def conexion(self):
        connection = psycopg2.connect(host="postgres",
                                      database="notebooks",
                                      user="root",
                                      password="root")
        return connection

    def create_table(self):
        cursor = self.connection.cursor()
        query = '''
        CREATE TABLE IF NOT EXISTS estadisticas (
            fecha TIMESTAMP DEFAULT now(),
            categoria VARCHAR(50) NOT NULL,
            precio_promedio FLOAT NOT NULL,
            mediana FLOAT NOT NULL,
            percentil_25 FLOAT NOT NULL,
            percentil_50 FLOAT NOT NULL,
            percentil_75 FLOAT NOT NULL,
            PRIMARY KEY (fecha, categoria)
            );
        '''
        cursor.execute(query)
        self.connection.commit()

    def load_data(self):
        df = pd.read_csv(csv_file)
        df = df.astype({
            'precio': 'float',
            'mediana': 'float',
            'percentil_25': 'float',
            'percentil_50': 'float',
            'percentil_75': 'float'
        })
        values = [tuple(row[2:]) for row in df.itertuples()]
        query = '''
            INSERT INTO estadisticas(categoria, precio_promedio, mediana, percentil_25, percentil_50, percentil_75)
            VALUES %s
        '''
        with self.connection, self.connection.cursor() as cursor:
            execute_values(cursor, query, values)
        print("Datos cargados exitosamente en la tabla estadistica")

    def show_data(self):
        # * Query
        query = "SELECT * FROM estadisticas"

        # Conexión
        cur = self.connection.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()

        # DataFrame and visual data
        df = pd.DataFrame(rows)
        df = df.rename(columns=column_names)
        display(df)

    def show_data_top(self):
        # Query
        query = "SELECT * FROM estadisticas ORDER BY fecha DESC LIMIT 4"

        # Conexión
        cur = self.connection.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()


        # DataFrame and visual data
        df = pd.DataFrame(rows)
        df = df.rename(columns=column_names)
        display(df)

    def show_data_last(self):
        # Query
        query = "SELECT * FROM estadisticas ORDER BY fecha ASC LIMIT 4"

        # Conexión
        cur = self.connection.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()

        # DataFrame and visual data
        df = pd.DataFrame(rows)
        df = df.rename(columns=column_names)
        display(df)
