import click
from scrap.scrap import ScrapMercadoLibre
from exploratory_analysis import data_work

@click.group()
def main():
    pass

@main.command()
def extract():
    scrap = ScrapMercadoLibre()

@main.command()
def analyze():
    data_work.imprimir_analisis()
    

if __name__ == '__main__':
    main()
