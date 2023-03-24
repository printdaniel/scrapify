# Scrapify

Scrapify es un proyecto ETL (Extract, Transform, Load) que se encarga de scrapear datos de computadoras nuevas y usadas para llevar a cabo un análisis estadístico y comparativo de precios y su variación.

## Funcionamiento

El proyecto consta de tres módulos principales:

- `scrap`: encargado de extraer los datos de computadoras nuevas y usadas de Mercado Libre y guardarlos en archivos CSV.
- `exploratory_analysis`: encargado de limpiar y analizar los datos previamente extraídos y mostrar resultados en la terminal y guardar los datos en un archivo CSV.
- `database`: encargado de guardar los datos en una base de datos para su persistencia y para futuros análisis teniendo en cuenta la variación de precios por inflación, etc. Además, este módulo también realiza consultas a la base de datos para mostrar los resultados en la terminal.

## Requerimientos

- Docker
- Python 3
- virtualenv

## Instalación

1. Clonar el repositorio: `git clone https://github.com/tu_usuario/scrapify.git`
2. Entrar al directorio: `cd scrapify`
3. Ejecutar el siguiente comando: `docker-compose up -d --build`
4. Ejecutar el siguiente comando: `docker-compose run myapp`

## Uso

Una vez que se ha ejecutado el contenedor Docker, se puede interactuar con el programa a través del menú:

1. Extraer datos (Notebooks nuevas vs Notebooks usadas)
2. Ejecutar Análisis de datos
3. Mostrar análisis (Precio Promedio, Mediana, Percentiles)
4. Registrar los datos en la base de datos
5. Mostrar registros de la base de datos
6. Mostar últimos cuatro registros
7. Mostrar primeros cuatro registros
8. Exit


## Autores

- Daniel Suárez(dwsuarez98@gmail.com)

## Licencia

Este proyecto está bajo la licencia MIT.
