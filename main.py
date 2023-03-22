from scrap.scrap import ScrapMercadoLibre
from exploratory_analysis.data_work import DataWork
from database.database import DataBase

scrap = ScrapMercadoLibre()
data_work = DataWork()
#db = DataBase()



if __name__ == '__main__':
    while True:
        print("Menú")
        print("1 Extraer datos (Notebooks nuevas vs Notebooks usadas)")
        print("2 Ejecutar Análisis de datos")
        print("3 Mostrar análisis (Precio, Promedio, Percentiles)")
        print("4 Extraer datos (Notebooks nuevas vs Notebooks usadas)")
        print("5 Extraer datos (Notebooks nuevas vs Notebooks usadas)")
        print("6 Extraer datos (Notebooks nuevas vs Notebooks usadas)")
        print("6 Extraer datos (Notebooks nuevas vs Notebooks usadas)")

        opcion = input("Seleciones una opción: ")

        if opcion == "1":
            scrap.save_data_csv()
    
        if opcion == "2":
            data_work.main()
    

        if opcion == "3":
            data_work.imprimir_analisis()
