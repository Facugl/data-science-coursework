# Luna, Facundo

inicio = int(input("Ingrese el número de inicio de la secuencia: "))
fin = int(input("Ingrese el número de fin de la secuencia: "))

cantidad_numeros = 0
sumatoria = 0

for numero in range(inicio, fin):
    cantidad_numeros = cantidad_numeros + 1
    sumatoria = sumatoria + numero

promedio = sumatoria / cantidad_numeros

print(f"La cantidad de números ingresados es {cantidad_numeros}")
print(f"La sumatoria de los números es {sumatoria}")
print(f"El promedio de los números es {promedio}")
