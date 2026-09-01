# Luna, Facundo

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = None

print(f"El resultado de sumar {num1} + {num2} es {suma}")
print(f"El resultado de restar {num1} - {num2} es {resta}")
print(f"El resultado de multiplicar {num1} x {num2} es {multiplicacion}")

if division is not None:
    print(f"El resultado de dividir {num1} / {num2} es {division}")
else:
    print(f"La división entre {num1} y {num2} no está definida en el campo de los números reales.")
