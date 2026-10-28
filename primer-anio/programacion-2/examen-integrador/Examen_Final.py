# Luna, Facundo

# EXAMEN FINAL INTEGRADOR - PROGRAMACION II
# Sistema de control de gestion anual de una sucursal de supermercado
#
# Lee ventas.csv (una fila por mes y sector, con unidades vendidas, precio
# unitario y unidades perdidas) y sectores.csv (la ficha de cada sector, con su
# responsable, su meta de merma y su categoria de mercaderia)
#
# Calcula la facturacion y la merma de cada sector, compara la merma contra la
# meta particular de cada uno en lugar de un unico limite general, mide la
# evolucion mes a mes y por trimestre, y presenta todo en un menu de consulta
# con tablas, graficos, un informe de texto y una exportacion para analisis

import csv
import os
import sys
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# CONSTANTES DEL SISTEMA
# ============================================================

AUTOR = "Luna, Facundo"
MATERIA = "Programación II"
CARRERA = "Licenciatura en Ciencia de Datos"
PROFESOR = "Ing. Mario Martínez"
ANIO_LECTIVO = "2026"
VERSION = "1.0"

# Ancho en caracteres de las pantallas, para que los recuadros y los titulos
# centrados queden alineados entre si
ANCHO = 74

# Si la merma supera la meta del sector pero no llega a la meta multiplicada
# por este factor, se considera una desviacion leve (ATENCION) en vez de ALERTA
TOLERANCIA = 1.2

ARCHIVO_VENTAS = "ventas.csv"
ARCHIVO_SECTORES = "sectores.csv"

NOMBRES_MESES = {
    1: "Enero", 2: "Febrero", 3: "Marzo",
    4: "Abril", 5: "Mayo", 6: "Junio",
    7: "Julio", 8: "Agosto", 9: "Septiembre",
    10: "Octubre", 11: "Noviembre", 12: "Diciembre",
}

NOMBRES_TRIMESTRES = {
    1: "1° trimestre (Ene-Mar)",
    2: "2° trimestre (Abr-Jun)",
    3: "3° trimestre (Jul-Sep)",
    4: "4° trimestre (Oct-Dic)",
}

# Tonos que se distinguen tambien en blanco y negro. De todas formas el estado
# nunca se informa solo con el color, siempre va acompanado del texto
COLOR_ESTADO = {
    "OK": "#2e7d32",
    "ATENCIÓN": "#e3a008",
    "ALERTA": "#b91c1c",
    "SIN META": "#6b7280",
}

COLOR_FACTURACION = "#2c6fbb"
COLOR_REFERENCIA = "#333333"


# ============================================================
# PANTALLA DE BIENVENIDA
# ============================================================

print()
print("=" * ANCHO)
print("SISTEMA DE CONTROL DE GESTIÓN DE SUCURSAL".center(ANCHO))
print("Análisis anual de facturación y merma".center(ANCHO))
print("=" * ANCHO)
print(f"  Autor:     {AUTOR}")
print(f"  Materia:   {MATERIA}")
print(f"  Carrera:   {CARRERA}")
print(f"  Profesor:  {PROFESOR}")
print(f"  Año:       {ANIO_LECTIVO}")
print(f"  Versión:   {VERSION}")
print("=" * ANCHO)
print()


# ============================================================
# CONTROL DE LOS ARCHIVOS DE DATOS
# ============================================================

# Se controla antes de pedirle nada al usuario, para que no complete sus datos
# y recien despues se entere de que falta un archivo
archivos_faltantes = []

for archivo_necesario in [ARCHIVO_VENTAS, ARCHIVO_SECTORES]:
    if not os.path.exists(archivo_necesario):
        archivos_faltantes.append(archivo_necesario)

if len(archivos_faltantes) > 0:
    print("No se puede iniciar el sistema porque faltan archivos de datos:")

    for archivo_faltante in archivos_faltantes:
        print(f"  - {archivo_faltante}")

    print()
    print("Los archivos deben estar en la misma carpeta que Examen_Final.py")
    print(f"El programa se está ejecutando en: {os.getcwd()}")
    print()

    sys.exit()


# ============================================================
# IDENTIFICACION DEL USUARIO
# ============================================================

# replace() saca los espacios interiores e isalpha() comprueba que lo que quedo
# sean solo letras, asi no se acepta un nombre con numeros
nombre = ""

while nombre == "":
    nombre = input("Ingrese su nombre y apellido: ").strip().title()

    if nombre == "":
        print("  El nombre no puede quedar vacío")
    elif not nombre.replace(" ", "").isalpha():
        print("  El nombre solo puede contener letras")
        nombre = ""

sucursal = ""

while sucursal == "":
    sucursal = input("Ingrese el nombre de la sucursal: ").strip().upper()

    if sucursal == "":
        print("  La sucursal no puede quedar vacía")

# Iniciales con las que se firma el informe
letras_iniciales = []

for palabra in nombre.split():
    letras_iniciales.append(palabra[0])

iniciales = "".join(letras_iniciales)

print()
print(f"Bienvenido/a al control de gestión, {nombre}")
print(f"Sucursal en análisis: {sucursal}")


# ============================================================
# LECTURA DE LOS ARCHIVOS CSV
# ============================================================

# Se indica utf-8 porque sectores.csv tiene nombres con tilde y sin ese dato
# Windows los leeria con otra codificacion
#
# A cada sector le corresponde un diccionario con su ficha, de modo que
# fichas_sectores es un diccionario de diccionarios
fichas_sectores = {}

archivo = open(ARCHIVO_SECTORES, "r", encoding="utf-8")
datos_sectores = list(csv.DictReader(archivo))
archivo.close()

for fila in datos_sectores:
    sector = fila["sector"].strip().capitalize()

    fichas_sectores[sector] = {
        "responsable": fila["responsable"].strip().title(),
        "meta_merma": float(fila["meta_merma"]),
        "categoria": fila["categoria"].strip().capitalize(),
    }

archivo = open(ARCHIVO_VENTAS, "r", encoding="utf-8")
datos_ventas = list(csv.DictReader(archivo))
archivo.close()

# El archivo puede existir y tener solo el encabezado. Sin ninguna fila no hay
# nada que calcular, asi que conviene avisarlo aca y no dejar que el programa
# siga hasta fallar con los acumuladores vacios
if len(datos_ventas) == 0:
    print()
    print(f"El archivo {ARCHIVO_VENTAS} no tiene registros de ventas cargados")
    print("Debe tener al menos una fila además del encabezado")
    print()

    sys.exit()

print()
print(f"Se leyeron {len(datos_ventas)} registros de ventas "
      f"y {len(fichas_sectores)} fichas de sectores")


# ============================================================
# CALCULOS SOBRE LOS DATOS LEIDOS
# ============================================================

ventas_por_sector = {}
merma_por_sector = {}
unidades_por_sector = {}
ventas_por_mes = {}
merma_por_mes = {}
ventas_por_categoria = {}
merma_por_categoria = {}

# Copia de cada fila con sus importes ya calculados, que es lo que exporta la
# opcion 10
detalle_filas = []

filas_sin_ficha = 0

# El if/else resuelve el arranque de cada acumulador: si la clave todavia no
# figura en el diccionario no se le puede sumar nada, asi que la primera vez se
# asigna el valor y recien a partir de la segunda se acumula
for fila in datos_ventas:
    mes = int(fila["mes"])
    sector = fila["sector"].strip().capitalize()
    unidades = int(fila["unidades"])
    precio_unitario = float(fila["precio_unitario"])
    unidades_merma = int(fila["unidades_merma"])

    facturacion = unidades * precio_unitario
    merma = unidades_merma * precio_unitario

    # Un sector puede no haber vendido nada en el mes, por ejemplo si estuvo
    # cerrado por refacciones. En ese caso no hay facturacion sobre la cual
    # calcular el porcentaje, y se deja en cero para no dividir por cero
    if facturacion > 0:
        porcentaje_merma_fila = round(merma / facturacion * 100, 2)
    else:
        porcentaje_merma_fila = 0.0

    # El // es la division entera: los meses 1 a 3 caen en el trimestre 1, los
    # meses 4 a 6 en el 2, y asi con el resto
    detalle_filas.append({
        "mes": mes,
        "nombre_mes": NOMBRES_MESES[mes],
        "trimestre": (mes - 1) // 3 + 1,
        "sector": sector,
        "unidades": unidades,
        "precio_unitario": precio_unitario,
        "facturacion": round(facturacion, 2),
        "unidades_merma": unidades_merma,
        "merma": round(merma, 2),
        "porcentaje_merma": porcentaje_merma_fila,
    })

    if sector in ventas_por_sector:
        ventas_por_sector[sector] = ventas_por_sector[sector] + facturacion
        merma_por_sector[sector] = merma_por_sector[sector] + merma
        unidades_por_sector[sector] = unidades_por_sector[sector] + unidades
    else:
        ventas_por_sector[sector] = facturacion
        merma_por_sector[sector] = merma
        unidades_por_sector[sector] = unidades

    if mes in ventas_por_mes:
        ventas_por_mes[mes] = ventas_por_mes[mes] + facturacion
        merma_por_mes[mes] = merma_por_mes[mes] + merma
    else:
        ventas_por_mes[mes] = facturacion
        merma_por_mes[mes] = merma

    # La categoria no esta en ventas.csv sino en la ficha, y el in evita el
    # error cuando un sector no la tiene cargada
    if sector in fichas_sectores:
        categoria = fichas_sectores[sector]["categoria"]

        if categoria in ventas_por_categoria:
            ventas_por_categoria[categoria] = ventas_por_categoria[categoria] + facturacion
            merma_por_categoria[categoria] = merma_por_categoria[categoria] + merma
        else:
            ventas_por_categoria[categoria] = facturacion
            merma_por_categoria[categoria] = merma
    else:
        filas_sin_ficha = filas_sin_ficha + 1

if filas_sin_ficha > 0:
    print(f"Aviso: {filas_sin_ficha} registros corresponden a sectores "
          f"sin ficha en {ARCHIVO_SECTORES}")

# Porcentaje de merma de cada sector y estado que resulta de compararlo contra
# la meta propia del sector
porcentajes_merma = {}
estados_sector = {}

for sector in ventas_por_sector:
    # Mismo cuidado que en el detalle: un sector sin ventas en todo el ano no
    # tiene facturacion contra la cual medir la merma
    if ventas_por_sector[sector] > 0:
        porcentaje = merma_por_sector[sector] / ventas_por_sector[sector] * 100
    else:
        porcentaje = 0.0

    porcentajes_merma[sector] = porcentaje

    if sector in fichas_sectores:
        meta = fichas_sectores[sector]["meta_merma"]

        if porcentaje <= meta:
            estados_sector[sector] = "OK"
        elif porcentaje <= meta * TOLERANCIA:
            estados_sector[sector] = "ATENCIÓN"
        else:
            estados_sector[sector] = "ALERTA"
    else:
        estados_sector[sector] = "SIN META"

# A cada fila del detalle se le suman los datos que no venian en ventas.csv,
# para que el archivo exportado quede completo por si solo
for registro in detalle_filas:
    sector_registro = registro["sector"]

    if sector_registro in fichas_sectores:
        meta_registro = fichas_sectores[sector_registro]["meta_merma"]

        registro["categoria"] = fichas_sectores[sector_registro]["categoria"]
        registro["responsable"] = fichas_sectores[sector_registro]["responsable"]
        registro["meta_merma"] = meta_registro
        registro["desvio"] = round(registro["porcentaje_merma"] - meta_registro, 2)
    else:
        registro["categoria"] = ""
        registro["responsable"] = ""
        registro["meta_merma"] = ""
        registro["desvio"] = ""

    registro["estado_anual"] = estados_sector[sector_registro]

# El signo menos invierte el orden, porque sorted() ordena de menor a mayor
sectores_por_facturacion = sorted(ventas_por_sector,
                                  key=lambda s: -ventas_por_sector[s])

# Los meses se ordenan porque un diccionario no garantiza ningun orden. Con los
# importes ordenados se arman los arrays, que permiten calcular sobre toda la
# serie de una sola vez, sin recorrerla con un bucle
meses = sorted(ventas_por_mes)

importes = []
mermas = []

for mes in meses:
    importes.append(ventas_por_mes[mes])
    mermas.append(merma_por_mes[mes])

importes = np.array(importes)
mermas = np.array(mermas)

# std() mide cuanto se apartan los meses del promedio: cuanto mas alto, mas
# desparejo fue el ano. argmax() y argmin() no devuelven el importe sino la
# POSICION donde esta, y con esa posicion se obtiene el mes
total_anual = importes.sum()
merma_anual = mermas.sum()
promedio_mensual = importes.mean()
desvio_mensual = importes.std()
mejor_mes = meses[int(importes.argmax())]
peor_mes = meses[int(importes.argmin())]
porcentaje_merma_anual = merma_anual / total_anual * 100

# where() conserva el importe en los meses que superan el promedio y pone cero
# en el resto
sobre_promedio = np.where(importes > promedio_mensual, importes, 0)

# diff() devuelve la diferencia entre cada mes y el anterior, por eso tiene un
# elemento menos que la serie
diferencias = np.diff(importes)
variaciones = diferencias / importes[:-1] * 100

acumulado = importes.cumsum()

# reshape() reacomoda los doce meses en cuatro filas de tres y sum(axis=1) suma
# cada fila, es decir cada trimestre
hay_ano_completo = len(meses) == 12

if hay_ano_completo:
    trimestres = importes.reshape(4, 3).sum(axis=1)
    trimestres_merma = mermas.reshape(4, 3).sum(axis=1)
else:
    trimestres = np.array([])
    trimestres_merma = np.array([])


# ============================================================
# MENU PRINCIPAL
# ============================================================

# isdigit() comprueba que lo ingresado sean solo digitos, asi que escribir una
# letra no interrumpe el programa sino que vuelve a preguntar
opcion = ""

while opcion != "0":
    print()
    print("-" * ANCHO)
    print("MENÚ PRINCIPAL".center(ANCHO))
    print("-" * ANCHO)
    print("  1. ¿Qué hace este sistema?")
    print("  2. Resumen anual de la sucursal")
    print("  3. Facturación y merma por sector")
    print("  4. Evolución mes a mes")
    print("  5. Análisis por trimestre")
    print("  6. Consultar un sector en particular")
    print("  7. Gráficos de facturación")
    print("  8. Gráficos de merma")
    print("  9. Generar informe en archivo de texto")
    print(" 10. Exportar los datos para análisis (CSV)")
    print("  0. Salir del sistema")
    print("-" * ANCHO)

    opcion = input("Elija una opción (0 a 10): ").strip()

    if not opcion.isdigit():
        print("\n  Debe ingresar un número del 0 al 10")
        opcion = ""

    # ------------------------------------------------------------
    # 1. PANTALLA EXPLICATIVA DEL PROYECTO
    # ------------------------------------------------------------
    elif opcion == "1":
        print()
        print("=" * ANCHO)
        print("¿QUÉ HACE ESTE SISTEMA?".center(ANCHO))
        print("=" * ANCHO)
        print("""
  Una sucursal de supermercado factura todos los meses, pero una parte de
  la mercadería nunca llega a venderse: se vence, se rompe o se descarta
  por mal estado. Esa pérdida se llama MERMA y se mide en dinero, igual
  que la facturación.

  El problema es que la merma no se puede juzgar con un único límite para
  toda la sucursal. Un sector de almacén, donde la mercadería no se echa
  a perder, no puede compararse con una verdulería. Por eso cada sector
  tiene cargada su propia meta en el archivo de fichas.

  El sistema entonces:

    - Lee las ventas del año y la ficha de cada sector desde dos archivos
      CSV separados.
    - Calcula cuánto facturó y cuánto perdió cada sector, y qué porcentaje
      representa esa pérdida sobre lo que facturó.
    - Compara ese porcentaje contra la meta propia del sector y le asigna
      un estado: OK, ATENCIÓN o ALERTA.
    - Mide cómo evolucionó la facturación mes a mes y por trimestre, para
      distinguir un mal mes puntual de una caída sostenida.
    - Muestra los resultados en tablas y en gráficos, y los exporta a un
      informe de texto y a un archivo de datos para seguir analizándolos.

  El objetivo final es que el encargado sepa, sin revisar planilla por
  planilla, qué sector necesita atención y en qué momento del año se le
  fue de las manos.
""")
        print("=" * ANCHO)

    # ------------------------------------------------------------
    # 2. RESUMEN ANUAL
    # ------------------------------------------------------------
    elif opcion == "2":
        print()
        print(f"RESUMEN ANUAL - SUCURSAL {sucursal}")
        print("-" * ANCHO)
        print(f"  Meses analizados:        {len(meses):>19}")
        print(f"  Sectores analizados:     {len(ventas_por_sector):>19}")
        print(f"  Facturación total:       ${total_anual:>18,.2f}")
        print(f"  Merma total:             ${merma_anual:>18,.2f}")
        print(f"  Merma sobre facturación: {porcentaje_merma_anual:>18.2f} %")
        print(f"  Promedio mensual:        ${promedio_mensual:>18,.2f}")
        print(f"  Desvío entre meses:      ${desvio_mensual:>18,.2f}")
        print(f"  Mejor mes:               {NOMBRES_MESES[mejor_mes]:>19}")
        print(f"  Peor mes:                {NOMBRES_MESES[peor_mes]:>19}")

        # Los ceros que dejo where() son los meses que no superan el promedio
        print()
        print("  Meses por encima del promedio:")

        for i in range(len(meses)):
            if sobre_promedio[i] > 0:
                nombre_mes = NOMBRES_MESES[meses[i]]
                millones = sobre_promedio[i] / 1000000
                print(f"    {nombre_mes.ljust(12)} ${millones:>8.1f} millones")

        print()
        print("  Merma según el tipo de mercadería:")

        for categoria in ventas_por_categoria:
            facturado = ventas_por_categoria[categoria]
            perdido = merma_por_categoria[categoria]
            print(f"    {categoria.ljust(16)} {perdido / facturado * 100:>6.2f} %"
                  f"   (${perdido:,.2f} perdidos)")

    # ------------------------------------------------------------
    # 3. TABLA POR SECTOR
    # ------------------------------------------------------------
    elif opcion == "3":
        # ljust() alinea los nombres a la izquierda y los :> alinean los
        # numeros a la derecha, para que las columnas queden parejas
        print()
        print(f"FACTURACIÓN Y MERMA POR SECTOR - SUCURSAL {sucursal}")
        print("-" * ANCHO)
        print(f"  {'Sector'.ljust(12)} {'Facturación':>16} {'Merma':>14} "
              f"{'Real':>7} {'Meta':>6}   Estado")

        for sector in sectores_por_facturacion:
            facturado = ventas_por_sector[sector]
            perdido = merma_por_sector[sector]
            porcentaje = porcentajes_merma[sector]
            estado = estados_sector[sector]

            if sector in fichas_sectores:
                meta = f"{fichas_sectores[sector]['meta_merma']:.2f}"
            else:
                meta = "-"

            print(f"  {sector.ljust(12)} {facturado:>16,.2f} {perdido:>14,.2f} "
                  f"{porcentaje:>6.2f}% {meta:>6}   {estado}")

        print("-" * ANCHO)
        print(f"  {'TOTAL'.ljust(12)} {total_anual:>16,.2f} {merma_anual:>14,.2f} "
              f"{porcentaje_merma_anual:>6.2f}%")

        print()
        print("  Participación de cada sector en la facturación:")

        for sector in sectores_por_facturacion:
            participacion = ventas_por_sector[sector] / total_anual * 100
            barra = "*" * int(participacion)
            print(f"    {sector.ljust(12)} {participacion:>5.1f}%  {barra}")

    # ------------------------------------------------------------
    # 4. EVOLUCION MES A MES
    # ------------------------------------------------------------
    elif opcion == "4":
        print()
        print(f"EVOLUCIÓN MES A MES - SUCURSAL {sucursal}")
        print("-" * ANCHO)
        print(f"  {'Mes'.ljust(12)} {'Facturación':>16} {'Variación':>11} "
              f"{'Acumulado':>18}")

        for i in range(len(meses)):
            nombre_mes = NOMBRES_MESES[meses[i]]

            # El primer mes no tiene con que compararse. Del segundo en
            # adelante se usa variaciones[i - 1], corrida una posicion porque
            # diff() devuelve un elemento menos
            if i == 0:
                variacion = "-"
            else:
                variacion = f"{variaciones[i - 1]:+.2f}%"

            print(f"  {nombre_mes.ljust(12)} {importes[i]:>16,.2f} "
                  f"{variacion:>11} {acumulado[i]:>18,.2f}")

        meses_en_alza = int((diferencias > 0).sum())
        meses_en_baja = int((diferencias < 0).sum())

        print("-" * ANCHO)
        print(f"  Meses con suba respecto del anterior:  {meses_en_alza}")
        print(f"  Meses con baja respecto del anterior:  {meses_en_baja}")

        # Con un solo mes cargado no hay variaciones que comparar, porque
        # diff() necesita dos valores para calcular una diferencia
        if len(variaciones) == 0:
            print("  Se necesitan al menos dos meses para comparar variaciones")
        else:
            print(f"  Mejor variación: {variaciones.max():+.2f}% en "
                  f"{NOMBRES_MESES[meses[int(variaciones.argmax()) + 1]]}")
            print(f"  Peor variación:  {variaciones.min():+.2f}% en "
                  f"{NOMBRES_MESES[meses[int(variaciones.argmin()) + 1]]}")

    # ------------------------------------------------------------
    # 5. ANALISIS POR TRIMESTRE
    # ------------------------------------------------------------
    elif opcion == "5":
        print()
        print(f"ANÁLISIS POR TRIMESTRE - SUCURSAL {sucursal}")
        print("-" * ANCHO)

        if not hay_ano_completo:
            print(f"  Se necesitan los 12 meses y el archivo tiene {len(meses)}")
        else:
            print(f"  {'Trimestre'.ljust(24)} {'Facturación':>18} "
                  f"{'Merma':>14} {'% merma':>9}")

            for i in range(len(trimestres)):
                nombre_trimestre = NOMBRES_TRIMESTRES[i + 1]
                porcentaje = trimestres_merma[i] / trimestres[i] * 100
                print(f"  {nombre_trimestre.ljust(24)} {trimestres[i]:>18,.2f} "
                      f"{trimestres_merma[i]:>14,.2f} {porcentaje:>8.2f}%")

            print("-" * ANCHO)
            print(f"  Mejor trimestre: "
                  f"{NOMBRES_TRIMESTRES[int(trimestres.argmax()) + 1]}")
            print(f"  Peor trimestre:  "
                  f"{NOMBRES_TRIMESTRES[int(trimestres.argmin()) + 1]}")

            # Comparar el ultimo trimestre contra el primero resume el ano en
            # un solo numero
            variacion_anual = (trimestres[3] - trimestres[0]) / trimestres[0] * 100
            print(f"  Variación del 4° trimestre contra el 1°: "
                  f"{variacion_anual:+.2f}%")

    # ------------------------------------------------------------
    # 6. CONSULTA DE UN SECTOR
    # ------------------------------------------------------------
    elif opcion == "6":
        print()
        print("SECTORES DISPONIBLES")
        print("-" * ANCHO)

        for sector in sorted(ventas_por_sector):
            print(f"  - {sector}")

        consulta = input("\nIngrese el sector a consultar: ").strip().capitalize()

        if consulta == "":
            print("  No se consultó ningún sector")
        elif consulta in ventas_por_sector:
            facturado = ventas_por_sector[consulta]
            perdido = merma_por_sector[consulta]
            unidades_vendidas = unidades_por_sector[consulta]

            # El sector figura en ventas.csv, pero su ficha puede no estar
            # cargada en sectores.csv. En ese caso no hay responsable ni meta
            # que mostrar, y esos renglones se completan con un guion en lugar
            # de interrumpir la consulta
            if consulta in fichas_sectores:
                responsable = fichas_sectores[consulta]["responsable"]
                categoria = fichas_sectores[consulta]["categoria"]
                meta = f"{fichas_sectores[consulta]['meta_merma']:.2f} %"
            else:
                responsable = "-"
                categoria = "-"
                meta = "-"

            print()
            print(f"FICHA DEL SECTOR {consulta.upper()}")
            print("-" * ANCHO)
            print(f"  Responsable:            {responsable}")
            print(f"  Tipo de mercadería:     {categoria}")
            print(f"  Unidades vendidas:      {unidades_vendidas:,}")
            print(f"  Facturación anual:      ${facturado:,.2f}")
            print(f"  Merma anual:            ${perdido:,.2f}")
            print(f"  Merma real:             {porcentajes_merma[consulta]:.2f} %")
            print(f"  Meta del sector:        {meta}")
            print(f"  Estado:                 {estados_sector[consulta]}")
            print(f"  Participación:          "
                  f"{facturado / total_anual * 100:.1f} % de la sucursal")

            # El desvio dice en cuantos puntos porcentuales el sector se pasa
            # de su meta, que es el dato con el que se decide si intervenir
            if consulta not in fichas_sectores:
                print(f"\n  El sector no tiene ficha cargada en "
                      f"{ARCHIVO_SECTORES}, así que no hay meta contra la cual "
                      f"compararlo")
            else:
                desvio = (porcentajes_merma[consulta]
                          - fichas_sectores[consulta]["meta_merma"])

                if desvio <= 0:
                    print(f"\n  El sector está {abs(desvio):.2f} puntos por debajo "
                          f"de su meta: no requiere intervención")
                else:
                    print(f"\n  El sector está {desvio:.2f} puntos por encima de su "
                          f"meta")
                    print(f"  Si cumpliera la meta se habrían evitado "
                          f"${desvio / 100 * facturado:,.2f} de pérdida")
        else:
            # startswith() rescata la consulta cuando se escribio solo el
            # comienzo del nombre o se erro el final
            parecidos = []

            for sector in ventas_por_sector:
                if sector.startswith(consulta[:3]):
                    parecidos.append(sector)

            print(f"  El sector {consulta} no figura en {ARCHIVO_VENTAS}")

            if len(parecidos) > 0:
                print(f"  ¿Quiso decir {', '.join(parecidos)}?")

    # ------------------------------------------------------------
    # 7. GRAFICOS DE FACTURACION
    # ------------------------------------------------------------
    elif opcion == "7":
        print("\n  Abriendo los gráficos de facturación...")
        print("  Cierre la ventana del gráfico para volver al menú")

        # subplots(1, 2) crea una figura con dos graficos lado a lado y
        # devuelve uno por variable, para configurarlos por separado
        figura, (grafico_meses, grafico_trimestres) = plt.subplots(1, 2, figsize=(13, 5))
        figura.suptitle(f"Facturación anual - Sucursal {sucursal}")

        # La division por un millon evita que el eje quede con numeros de
        # nueve cifras
        importes_en_millones = importes / 1000000

        grafico_meses.plot(meses, importes_en_millones, color=COLOR_FACTURACION,
                           linewidth=2, zorder=2)
        grafico_meses.scatter(meses, importes_en_millones,
                              color=COLOR_FACTURACION, s=40, zorder=3)

        # La linea del promedio deja ver de un vistazo que meses lo superan
        grafico_meses.axhline(promedio_mensual / 1000000,
                              color=COLOR_REFERENCIA, linestyle="--",
                              linewidth=1, label="Promedio mensual")

        grafico_meses.set_title("Evolución mensual")
        grafico_meses.set_xlabel("Mes")
        grafico_meses.set_ylabel("Facturación (millones de $)")

        # Sin set_xticks matplotlib pondria valores intermedios como 2.5
        grafico_meses.set_xticks(meses)
        grafico_meses.grid(True, color="#dddddd", linewidth=0.6)
        grafico_meses.set_axisbelow(True)
        grafico_meses.legend()

        if hay_ano_completo:
            etiquetas_trimestres = ["1° trim.", "2° trim.", "3° trim.", "4° trim."]
            trimestres_en_millones = trimestres / 1000000

            grafico_trimestres.bar(etiquetas_trimestres, trimestres_en_millones,
                                   color=COLOR_FACTURACION, width=0.6, zorder=2)

            # El valor escrito sobre cada barra evita tener que seguir la
            # linea del eje para leerlo
            for i in range(len(trimestres_en_millones)):
                grafico_trimestres.text(i, trimestres_en_millones[i],
                                        f"{trimestres_en_millones[i]:.0f}",
                                        ha="center", va="bottom",
                                        color=COLOR_REFERENCIA)

            grafico_trimestres.set_title("Facturación por trimestre")
            grafico_trimestres.set_xlabel("Trimestre")
            grafico_trimestres.set_ylabel("Facturación (millones de $)")
            grafico_trimestres.grid(True, axis="y", color="#dddddd", linewidth=0.6)
            grafico_trimestres.set_axisbelow(True)
        else:
            grafico_trimestres.set_title("Facturación por trimestre")
            grafico_trimestres.text(0.5, 0.5, "Se necesita el año completo",
                                    ha="center", va="center")

        plt.tight_layout()
        plt.show()

    # ------------------------------------------------------------
    # 8. GRAFICOS DE MERMA
    # ------------------------------------------------------------
    elif opcion == "8":
        print("\n  Abriendo los gráficos de merma...")
        print("  Cierre la ventana del gráfico para volver al menú")

        figura, (grafico_metas, grafico_pesos) = plt.subplots(1, 2, figsize=(13, 5))
        figura.suptitle(f"Merma anual por sector - Sucursal {sucursal}")

        # Ordenados por merma, el que mas se desvia queda arriba de todo
        sectores_por_merma = sorted(porcentajes_merma,
                                    key=lambda s: porcentajes_merma[s])

        porcentajes = []
        metas = []
        colores = []
        textos = []

        for sector in sectores_por_merma:
            porcentajes.append(porcentajes_merma[sector])
            colores.append(COLOR_ESTADO[estados_sector[sector]])
            textos.append(f"{porcentajes_merma[sector]:.2f}%  "
                          f"{estados_sector[sector]}")

            # Al sector sin ficha se le carga un nan (no es un numero) en lugar
            # de un cero, porque un cero se dibujaria como una meta de 0% que
            # no existe. Matplotlib directamente no dibuja los nan
            if sector in fichas_sectores:
                metas.append(fichas_sectores[sector]["meta_merma"])
            else:
                metas.append(np.nan)

        # barh() dibuja las barras en horizontal, que permite que los nombres
        # de los sectores se lean derechos y sin rotar
        posiciones = np.arange(len(sectores_por_merma))

        grafico_metas.barh(posiciones, porcentajes, color=colores, height=0.6,
                           zorder=2)

        # Cada meta se marca con un trazo sobre su propia barra: la barra que
        # pasa su marca es la que se desvio
        grafico_metas.scatter(metas, posiciones, marker="|", s=600,
                              color=COLOR_REFERENCIA, linewidths=2, zorder=3,
                              label="Meta del sector")

        # El porcentaje y el estado escritos al lado de cada barra hacen que el
        # estado nunca quede informado solamente por el color
        for i in range(len(posiciones)):
            grafico_metas.text(porcentajes[i] + 0.15, posiciones[i], textos[i],
                               va="center", fontsize=9, color=COLOR_REFERENCIA)

        grafico_metas.set_yticks(posiciones)
        grafico_metas.set_yticklabels(sectores_por_merma)
        grafico_metas.set_title("Merma real contra la meta de cada sector")
        grafico_metas.set_xlabel("Merma sobre facturación (%)")
        grafico_metas.set_xlim(0, max(porcentajes) * 1.5)
        grafico_metas.grid(True, axis="x", color="#dddddd", linewidth=0.6)
        grafico_metas.set_axisbelow(True)
        grafico_metas.legend(loc="lower right")

        # Este panel esta en pesos y el anterior en porcentaje: son medidas
        # distintas, por eso van separadas. Un sector puede tener un porcentaje
        # bajo y aun asi ser el que mas plata pierde, porque factura mucho
        sectores_por_perdida = sorted(merma_por_sector,
                                      key=lambda s: merma_por_sector[s])

        perdidas = []

        for sector in sectores_por_perdida:
            perdidas.append(merma_por_sector[sector] / 1000000)

        grafico_pesos.barh(sectores_por_perdida, perdidas,
                           color=COLOR_FACTURACION, height=0.6, zorder=2)

        for i in range(len(perdidas)):
            grafico_pesos.text(perdidas[i], i, f" {perdidas[i]:.1f}",
                               va="center", color=COLOR_REFERENCIA)

        grafico_pesos.set_title("Pérdida en dinero por sector")
        grafico_pesos.set_xlabel("Merma (millones de $)")
        grafico_pesos.set_xlim(0, max(perdidas) * 1.2)
        grafico_pesos.grid(True, axis="x", color="#dddddd", linewidth=0.6)
        grafico_pesos.set_axisbelow(True)

        plt.tight_layout()
        plt.show()

    # ------------------------------------------------------------
    # 9. INFORME EN ARCHIVO DE TEXTO
    # ------------------------------------------------------------
    elif opcion == "9":
        # lower() y replace() evitan mayusculas y espacios en el nombre del
        # archivo
        nombre_archivo = "informe_" + sucursal.lower().replace(" ", "_") + ".txt"

        # "w" abre el archivo para escritura y lo crea si no existe
        informe = open(nombre_archivo, "w", encoding="utf-8")

        informe.write("=" * ANCHO + "\n")
        informe.write("INFORME ANUAL DE FACTURACIÓN Y MERMA".center(ANCHO) + "\n")
        informe.write(f"Sucursal {sucursal}".center(ANCHO) + "\n")
        informe.write("=" * ANCHO + "\n\n")
        informe.write(f"Generado por: {nombre} ({iniciales})\n")
        informe.write(f"Sistema: control de gestión versión {VERSION}\n")
        informe.write(f"Autor del sistema: {AUTOR}\n\n")

        informe.write("RESUMEN ANUAL\n")
        informe.write("-" * ANCHO + "\n")
        informe.write(f"Facturación total:       ${total_anual:,.2f}\n")
        informe.write(f"Merma total:             ${merma_anual:,.2f}\n")
        informe.write(f"Merma sobre facturación: {porcentaje_merma_anual:.2f} %\n")
        informe.write(f"Promedio mensual:        ${promedio_mensual:,.2f}\n")
        informe.write(f"Mejor mes:               {NOMBRES_MESES[mejor_mes]}\n")
        informe.write(f"Peor mes:                {NOMBRES_MESES[peor_mes]}\n\n")

        informe.write("DETALLE POR SECTOR\n")
        informe.write("-" * ANCHO + "\n")

        for sector in sectores_por_facturacion:
            informe.write(f"{sector.ljust(12)} "
                          f"facturó ${ventas_por_sector[sector]:>16,.2f}   "
                          f"merma {porcentajes_merma[sector]:>5.2f}%   "
                          f"{estados_sector[sector]}\n")

        informe.write("\nSECTORES QUE REQUIEREN REVISIÓN\n")
        informe.write("-" * ANCHO + "\n")

        sectores_a_revisar = 0

        # Un sector sin ficha tampoco esta en OK, pero no se lo puede comparar
        # contra una meta que no tiene, asi que se lo informa por separado para
        # que de todas formas no pase inadvertido en el informe
        for sector in sectores_por_facturacion:
            if estados_sector[sector] == "SIN META":
                informe.write(f"{sector}: {porcentajes_merma[sector]:.2f}% de "
                              f"merma, sin ficha cargada en {ARCHIVO_SECTORES}. "
                              f"No tiene meta asignada\n")

                sectores_a_revisar = sectores_a_revisar + 1
            elif estados_sector[sector] != "OK":
                meta = fichas_sectores[sector]["meta_merma"]
                desvio = porcentajes_merma[sector] - meta
                responsable = fichas_sectores[sector]["responsable"]

                informe.write(f"{sector}: {porcentajes_merma[sector]:.2f}% contra "
                              f"una meta de {meta:.2f}% ({desvio:+.2f} puntos). "
                              f"Responsable: {responsable}\n")

                sectores_a_revisar = sectores_a_revisar + 1

        if sectores_a_revisar == 0:
            informe.write("Ningún sector superó su meta de merma\n")

        informe.write("\n" + "=" * ANCHO + "\n")
        informe.write("Fin del informe".center(ANCHO) + "\n")
        informe.write("=" * ANCHO + "\n")

        informe.close()

        print(f"\n  Informe generado en el archivo {nombre_archivo}")
        print(f"  Se listaron {sectores_a_revisar} sectores para revisar")

    # ------------------------------------------------------------
    # 10. EXPORTACION DE LOS DATOS PARA ANALISIS
    # ------------------------------------------------------------
    elif opcion == "10":
        nombre_csv = "analisis_" + sucursal.lower().replace(" ", "_") + ".csv"

        # Una observacion por fila y una variable por columna, que es el
        # formato que esperan las herramientas de analisis: asi el archivo se
        # puede abrir con Excel o leer con pandas y reagrupar por sector, por
        # mes o por trimestre sin prepararlo antes
        columnas = ["mes", "nombre_mes", "trimestre", "sector", "categoria",
                    "responsable", "unidades", "precio_unitario",
                    "facturacion", "unidades_merma", "merma",
                    "porcentaje_merma", "meta_merma", "desvio", "estado_anual"]

        # El newline vacio es lo que pide el modulo csv al escribir: sin eso
        # Windows deja una linea en blanco entre registro y registro
        salida = open(nombre_csv, "w", newline="", encoding="utf-8")

        # DictWriter es la contraparte de DictReader: recibe diccionarios y los
        # escribe como filas, usando las columnas para ordenar cada dato
        escritor = csv.DictWriter(salida, fieldnames=columnas)
        escritor.writeheader()

        for registro in detalle_filas:
            escritor.writerow(registro)

        salida.close()

        print(f"\n  Datos exportados en el archivo {nombre_csv}")
        print(f"  {len(detalle_filas)} filas y {len(columnas)} columnas")
        print("  El archivo se puede abrir con Excel o leer con pandas para")
        print("  seguir analizando los datos fuera de este sistema")

    elif opcion != "0":
        print(f"\n  La opción {opcion} no existe en el menú")


# ============================================================
# CIERRE DEL SISTEMA
# ============================================================

print()
print("=" * ANCHO)
print(f"Gracias por usar el sistema, {nombre}".center(ANCHO))
print(f"Control de gestión - Sucursal {sucursal}".center(ANCHO))
print("=" * ANCHO)
print()
