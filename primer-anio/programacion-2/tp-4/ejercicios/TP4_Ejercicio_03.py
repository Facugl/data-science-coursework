# Luna, Facundo

import csv

total_tornillos = 0

archivo = open("./stock.csv", "r")
datos = list(csv.DictReader(archivo))
archivo.close()

for fila in datos:
    total_tornillos = total_tornillos + int(fila["tornillos"])

print(f"El stock total de tornillos es: {total_tornillos}")
