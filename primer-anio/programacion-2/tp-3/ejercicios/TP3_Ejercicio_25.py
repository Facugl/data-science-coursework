# Luna, Facundo

suma_multiplos_3 = 0
producto_multiplos_5 = 1

for i in range(1, 11):
    numero = int(input(f"Ingrese el número {i}: "))
    if numero % 3 == 0:
        suma_multiplos_3 = suma_multiplos_3 + numero
    if numero % 5 == 0:
        producto_multiplos_5 = producto_multiplos_5 * numero

print(f"La suma de los números múltiplos de 3 es {suma_multiplos_3}")
print(f"El producto de los números múltiplos de 5 es {producto_multiplos_5}")
