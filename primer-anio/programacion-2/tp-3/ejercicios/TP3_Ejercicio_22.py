# Luna, Facundo

suma = 0
producto = 1

for i in range(1, 6):
    numero = float(input(f"Ingrese el número {i}: "))
    suma = suma + numero
    producto = producto * numero

print(f"La suma total de los números es {suma}")
print(f"El producto de los números es {producto}")
