# Luna, Facundo

suma_total = 0
suma_positivos = 0
cantidad_positivos = 0

for i in range(1, 11):
    numero = float(input(f"Ingrese el número {i}: "))
    suma_total = suma_total + numero

    if numero > 0:
        suma_positivos = suma_positivos + numero
        cantidad_positivos = cantidad_positivos + 1

promedio_total = suma_total / 10
promedio_positivos = suma_positivos / cantidad_positivos

print(f"El promedio de todos los números ingresados es {promedio_total}")
print(f"El promedio de los números positivos es {promedio_positivos}")
