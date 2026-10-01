# Luna, Facundo

cantidad_multiplos_4 = 0
cantidad_multiplos_2 = 0
cantidad_positivos = 0
cantidad_negativos = 0

for i in range(1, 11):
    numero = int(input(f"Ingrese el número {i}: "))

    if numero % 4 == 0:
        cantidad_multiplos_4 = cantidad_multiplos_4 + 1

    if numero % 2 == 0:
        cantidad_multiplos_2 = cantidad_multiplos_2 + 1

    if numero > 0:
        cantidad_positivos = cantidad_positivos + 1
    elif numero < 0:
        cantidad_negativos = cantidad_negativos + 1

print(f"La cantidad de números múltiplo de 4 es {cantidad_multiplos_4}")
print(f"La cantidad de números múltiplo de 2 es {cantidad_multiplos_2}")
print(f"La cantidad de números positivos es {cantidad_positivos}")
print(f"La cantidad de números negativos es {cantidad_negativos}")
