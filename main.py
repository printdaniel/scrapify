from scrap.scrap import ScrapMercadoLibre
from exploratory_analysis.data_work import DataWork
import subprocess 


scrap = ScrapMercadoLibre()

   
if __name__ == '__main__':
    dtw = DataWork()
    dtw.load_data()
    dtw.format_data_type()
    dtw.data_analystic()
    dtw.data_export()
