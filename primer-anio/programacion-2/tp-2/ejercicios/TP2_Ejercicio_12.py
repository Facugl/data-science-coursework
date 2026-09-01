# Luna, Facundo

num1 = float(input("Ingrese el primer número real:"))
num2 = float(input("Ingrese el segundo número real:"))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
potencia = num1 ** num2

print(f"La suma entre {num1} y {num2} es {suma}")
print(f"La resta entre {num1} y {num2} es {resta}")
print(f"La multiplicación entre {num1} y {num2} es {multiplicacion}")

if num2 != 0:
    division = num1 / num2
    print(f"La división entre {num1} y {num2} es {division}")
else:
    print(f"La división entre {num1} y {num2} no está definida en el campo de los números reales.")

print(f"La potencia entre {num1} y {num2} es {potencia}")
