from scrap.scrap import ScrapMercadoLibre
from exploratory_analysis.data_work import DataWork
from database.database import DataBase


scrap = ScrapMercadoLibre()
dtw = DataWork()
db = DataBase()

   
if __name__ == '__main__':
    db.show_data_top()
    db.show_data_last()

