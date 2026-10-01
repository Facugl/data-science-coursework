# Luna, Facundo

suma_pares = 0
producto_impares = 1

for i in range(1, 11):
    numero = int(input(f"Ingrese el número {i}: "))
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    else:
        producto_impares = producto_impares * numero

print(f"La suma de los números pares es {suma_pares}")
print(f"El producto de los números impares es {producto_impares}")
