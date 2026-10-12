# Luna, Facundo

# EJERCICIO FINAL INTEGRADOR
# Analisis anual de ventas y merma de una sucursal de supermercado
#
# El archivo ventas.csv tiene una fila por cada mes y cada sector, con las unidades
# vendidas, el precio unitario y las unidades perdidas por vencimiento, rotura, etc
# El programa calcula la facturacion de cada sector,
# cuanto representa la merma sobre esa facturacion y como evoluciono la venta mes a mes

import csv
import numpy as np
import matplotlib.pyplot as plt

# Supongo hasta un 3% de merma por sector. Por encima de ese valor
# el encargado debe revisar el sector
MERMA_ACEPTABLE = 3.0

# El CSV identifica los meses por numero. Este diccionario traduce ese
# numero al nombre, para que los resultados se lean mejor
NOMBRES_MESES = {
    1: "Enero", 2: "Febrero", 3: "Marzo",
    4: "Abril", 5: "Mayo", 6: "Junio",
    7: "Julio", 8: "Agosto", 9: "Septiembre",
    10: "Octubre", 11: "Noviembre", 12: "Diciembre",
}


# Se eliminan espacios y se formatea el texto
# El while vuelve a preguntar mientras el dato quede vacio. Como strip() ya
# saco los espacios, escribir solo espacios tambien cuenta como vacio
nombre = ""

while nombre == "":
    nombre = input("Ingrese su nombre: ").strip().title()

    if nombre == "":
        print("El nombre no puede quedar vacío")

sucursal = ""

while sucursal == "":
    sucursal = input("Ingrese la sucursal: ").strip().upper()

    if sucursal == "":
        print("La sucursal no puede quedar vacía")

print(f"Bienvenido/a al control de gestión, {nombre}")
print(f"Sucursal: {sucursal}")

ventas_por_sector = {}
merma_por_sector = {}
ventas_por_mes = {}


archivo = open("ventas.csv", "r")
datos = list(csv.DictReader(archivo))
archivo.close()


# El if/else resuelve el arranque de cada acumulador: si el sector todavia no
# figura en el diccionario no se le puede sumar nada, asi que la primera vez se
# asigna el valor y recien a partir de la segunda se acumula
for fila in datos:
    mes = int(fila["mes"])
    sector = fila["sector"].strip().capitalize()
    unidades = int(fila["unidades"])
    precio_unitario = float(fila["precio_unitario"])
    unidades_merma = int(fila["unidades_merma"])

    facturacion = unidades * precio_unitario
    merma = unidades_merma * precio_unitario

    if sector in ventas_por_sector:
        ventas_por_sector[sector] = ventas_por_sector[sector] + facturacion
        merma_por_sector[sector] = merma_por_sector[sector] + merma
    else:
        ventas_por_sector[sector] = facturacion
        merma_por_sector[sector] = merma

    if mes in ventas_por_mes:
        ventas_por_mes[mes] = ventas_por_mes[mes] + facturacion
    else:
        ventas_por_mes[mes] = facturacion

# ljust() alinea los nombres a la izquierda y los :>15 alinean los numeros a la
# derecha, para que las columnas queden parejas en pantalla
print("\nFacturación y merma anual por sector:")
print(f"  {'Sector'.ljust(12)} {'Facturación':>15} {'Merma':>13} {'% merma':>8}   Estado")

porcentajes_merma = {}

for sector in ventas_por_sector:
    facturacion = ventas_por_sector[sector]
    merma = merma_por_sector[sector]
    porcentaje = merma / facturacion * 100
    porcentajes_merma[sector] = porcentaje

    if porcentaje > MERMA_ACEPTABLE:
        estado = "ALERTA"
    else:
        estado = "OK"

    print(f"  {sector.ljust(12)} {facturacion:>15.2f} {merma:>13.2f} {porcentaje:>7.2f}%   {estado}")


# El operador in verifica que la clave exista antes de usarla, que es lo que
# evita que el programa corte con un error
#
# Esta consulta es opcional: sirve para mirar un sector en particular, pero el
# resumen anual y los graficos no dependen de ella. Por eso dejarla vacia no es
# un error, solo se informa que no se consulto nada y el programa sigue
consulta = input("\nIngrese un sector para consultar su merma: ")
consulta = consulta.strip().capitalize()

if consulta == "":
    print("No se consultó ningún sector")
elif consulta in porcentajes_merma:
    print(f"El sector {consulta} tuvo una merma del {porcentajes_merma[consulta]:.2f}%")
else:
    print(f"Error: el sector {consulta} no figura en el archivo de ventas")


# sorted() devuelve los meses de menor a mayor, porque un diccionario no
# garantiza ningun orden. Con los importes en ese orden se arma el array
#
# sum() y mean() operan sobre todo el array sin necesidad de recorrerlo con un
# bucle. argmax() y argmin() no devuelven el importe sino la POSICION donde
# esta, y esa posicion se usa para saber de que mes se trata
meses = sorted(ventas_por_mes)

importes = []

for mes in meses:
    importes.append(ventas_por_mes[mes])

importes = np.array(importes)

total_anual = importes.sum()
promedio_mensual = importes.mean()
mejor_mes = meses[int(importes.argmax())]
peor_mes = meses[int(importes.argmin())]

print("\nResumen anual de la sucursal:")
print(f"  Facturación total: ${total_anual:.2f}")
print(f"  Promedio mensual: ${promedio_mensual:.2f}")
print(f"  Mejor mes: {NOMBRES_MESES[mejor_mes]}")
print(f"  Peor mes: {NOMBRES_MESES[peor_mes]}")

# where() compara el array contra el promedio y arma uno nuevo del mismo largo:
# conserva el importe en los meses que lo superan y pone cero en el resto
# La division por un millon tambien se aplica a todo el array de una sola vez
sobre_promedio = np.where(importes > promedio_mensual, importes, 0)
sobre_promedio_en_millones = (sobre_promedio / 1000000).round(1)

# Los ceros que dejo where() son los meses que no superan el promedio,
# asi que el if los saltea y solo se listan los que si lo hacen
print("  Meses por encima del promedio:")

for i in range(len(meses)):
    if sobre_promedio_en_millones[i] > 0:
        nombre_mes = NOMBRES_MESES[meses[i]]
        millones = sobre_promedio_en_millones[i]
        print(f"    {nombre_mes.ljust(12)} ${millones:>5.1f} millones")

# subplots(1, 2) crea una figura con dos graficos lado a lado y devuelve uno
# por variable, de modo que cada uno se configura por separado
#
# El primero combina plot y scatter para ver la tendencia anual y marcar cada
# mes. set_xticks(meses) fuerza las marcas en los enteros 1 a 12, ya que por
# defecto matplotlib pondria valores intermedios como 2.5, que no existen
#
# El segundo es de barras y compara la merma de los sectores entre si. La
# rotacion de las etiquetas evita que los nombres se superpongan
#
# axhline() traza una linea horizontal a la altura que se le indique. Se usa
# la misma constante que decide el estado OK/ALERTA, asi que la linea siempre
# coincide con el limite real: las barras que la superan son las senaladas
figura, (grafico_meses, grafico_merma) = plt.subplots(1, 2, figsize=(12, 5))

grafico_meses.plot(meses, importes, color="green")
grafico_meses.scatter(meses, importes, color="red")
grafico_meses.set_title("Facturación mensual")
grafico_meses.set_xlabel("Mes")
grafico_meses.set_ylabel("Facturación")
grafico_meses.set_xticks(meses)
grafico_meses.grid(True)

etiqueta_limite = f"Límite admitido: {MERMA_ACEPTABLE}%"

grafico_merma.bar(list(porcentajes_merma), list(porcentajes_merma.values()))
grafico_merma.axhline(MERMA_ACEPTABLE, color="red", linestyle="--",
                      label=etiqueta_limite)
grafico_merma.set_title("Merma anual por sector")
grafico_merma.set_xlabel("Sector")
grafico_merma.set_ylabel("Merma (%)")
grafico_merma.tick_params(axis="x", rotation=20)
grafico_merma.legend()

plt.show()