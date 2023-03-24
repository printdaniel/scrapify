#############################
from bs4 import BeautifulSoup
import requests
import pandas as pd
#############################

# Constantes
NOTEBOOKS_ML_U = 'https://listado.mercadolibre.com.ar/notebooks-usadas#D[A:notebooks%20usadas]'
NOTEBOOKS_ML = 'https://listado.mercadolibre.com.ar/notebooks#D[A:notebooks]'


class ScrapMercadoLibre:

    def validator_soup(self, url: str):
        """ 
        Paseador de HTML 
        Args:
            url : strin de url Mercado Libre
        Returns:
            soup: html parsed
        """

        header = {
            'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
        }
        page = requests.get(url, headers=header)

        try:
            soup = BeautifulSoup(page.content, "html.parser")
        except:
            return None
        return soup

    def notebooks_usadas(self):
        """ 
        Extrae los datos de las notebooks usadas
        Returns:
            Nombre
            Precio
        """
        soup = self.validator_soup(NOTEBOOKS_ML_U)
        nombres = soup.find_all(
            'h2', class_='ui-search-item__title shops__item-title')
        precios = soup.find_all('span', class_='price-tag-fraction')

        if len(nombres) == 0 or len(precios) == 0:
            return []

        notebooks_usadas = []
        for nombre, precio in zip(nombres, precios):
            notebook = {
                'nombre': nombre.text.strip(),
                'precio': precio.text.strip()
            }
            notebooks_usadas.append(notebook)

        return notebooks_usadas

    def notebooks(self):
        """ 
        Extrae los datos de las notebooks nuevas
        Returns:
            Nombre
            Precio
        """
        soup = self.validator_soup(NOTEBOOKS_ML)
        nombres = soup.find_all(
            'h2', class_='ui-search-item__title shops__item-title')
        precios = soup.find_all('span', class_='price-tag-fraction')

        if len(nombres) == 0 or len(precios) == 0:
            return []

        notebooks = []
        for nombre, precio in zip(nombres, precios):
            notebook = {
                'nombre': nombre.text.strip(),
                'precio': precio.text.strip()
            }
            notebooks.append(notebook)

        return notebooks

    def save_data_csv(self):
        try:
            notebooks_usadas = self.notebooks_usadas()
            notebooks = self.notebooks()
            print("\n Extracción de datos exitosa \n")
        except EOFError as e:
            print(e)
            return 0
        
        df1 = pd.DataFrame(notebooks_usadas)
        df2 = pd.DataFrame(notebooks)
        
        df1.to_csv('exploratory_analysis/notebooks_usadas.csv', index=False)
        df2.to_csv('exploratory_analysis/notebooks.csv', index=False)
