# Luna, Facundo

import csv

departamentos_2_ambientes = 0
departamentos_3_ambientes = 0

archivo = open("propiedades.csv", "r", encoding="utf-8")
datos = list(csv.DictReader(archivo))
archivo.close()

for fila in datos:
    texto_ambientes = fila["ambientes"].strip()

    if texto_ambientes == "":
        continue

    ambientes = int(texto_ambientes)

    if ambientes == 2:
        departamentos_2_ambientes = departamentos_2_ambientes + 1
    elif ambientes == 3:
        departamentos_3_ambientes = departamentos_3_ambientes + 1

print(f"Departamentos de 2 ambientes: {departamentos_2_ambientes}")
print(f"Departamentos de 3 ambientes: {departamentos_3_ambientes}")
