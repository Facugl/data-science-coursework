# Luna, Facundo

import csv
import matplotlib.pyplot as plt

years = []
poblacion = []

archivo = open("poblacion.csv", "r")
datos = list(csv.DictReader(archivo))
archivo.close()

datos.sort(key=lambda fila: int(fila["year"]))

for fila in datos:
    years.append(int(fila["year"]))
    poblacion.append(int(fila["poblacion"]))

plt.plot(years, poblacion, color="green")
plt.scatter(years, poblacion, color="red")

plt.title("Población Histórica Mundial")
plt.xlabel("Year")
plt.ylabel("Población")

plt.show()
