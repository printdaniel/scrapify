###################################################
from scrap.scrap import ScrapMercadoLibre
from exploratory_analysis.data_work import DataWork
from database.database import DataBase
###################################################


class Menu:

    def __init__(self):
        self.scrap = ScrapMercadoLibre()
        self.data_work = DataWork()
        self.db = DataBase()

    def run(self):
        while True:
            print("Menú")
            print("1 Extraer datos (Notebooks nuevas vs Notebooks usadas)")
            print("2 Ejecutar Análisis de datos")
            print("3 Mostrar análisis (Precio Promedio, Mediana, Percentiles)")
            print("4 Registrar los datos en la base de datos")
            print("5 Mostrar registros de la base de datos")
            print("6 Mostar últimos cuatro registros")
            print("7 Mostrar primeros cuatro registros")
            print("9 Exit")

            opcion = input("Seleciones una opción: ")

            if opcion == "1":
                self.scrap.save_data_csv()

            elif opcion == "2":
                self.data_work.ejecutar_analisis()

            elif opcion == "3":
                self.data_work.imprimir_analisis()

            elif opcion == "4":
                self.db.load_data()

            elif opcion == "5":
                self.db.show_data()

            elif opcion == "6":
                self.db.show_data_top()

            elif opcion == "7":
                self.db.show_data_last()

            elif opcion == "9":
                print("Programa finalizado")
                break

            else:
                print("Opción incorrecta")


if __name__ == '__main__':
    menu = Menu()
    menu.run()
