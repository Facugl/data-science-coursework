# Luna, Facundo

inicio = int(input("Ingrese el número de inicio de la secuencia: "))
fin = int(input("Ingrese el número de fin de la secuencia: "))

cantidad_negativos = 0
cantidad_mayor_igual_cero = 0

for numero in range(inicio, fin):
    if numero < 0:
        cantidad_negativos = cantidad_negativos + 1
    else:
        cantidad_mayor_igual_cero = cantidad_mayor_igual_cero + 1

print(f"La cantidad de números negativos es {cantidad_negativos}")
print(f"La cantidad de números mayores o iguales a cero es {cantidad_mayor_igual_cero}")
