from scrap.scrap import ScrapMercadoLibre
from exploratory_analysis.data_work import imprimir_analisis
#from exploratory_analysis import data_work
import subprocess 


scrap = ScrapMercadoLibre()

   
if __name__ == '__main__':
    scrap.save_data_csv()
    subprocess.run(['python','exploratory_analysis/data_work.py'])
    imprimir_analisis()
