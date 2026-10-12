# Luna, Facundo

import csv
import matplotlib.pyplot as plt

years_buscados = [2000, 2005, 2010, 2015, 2020]
poblacion_por_year = {}

archivo = open("poblacion.csv", "r")
datos = list(csv.DictReader(archivo))
archivo.close()

for fila in datos:
    year = int(fila["year"])

    if year in years_buscados:
        poblacion_por_year[year] = int(fila["poblacion"])

years = []
poblacion = []

for year in years_buscados:
    years.append(year)
    poblacion.append(poblacion_por_year[year])

plt.bar(years, poblacion)

plt.title("Población Histórica Mundial")
plt.xlabel("Year")
plt.ylabel("Población")
plt.xticks(years)

plt.show()
