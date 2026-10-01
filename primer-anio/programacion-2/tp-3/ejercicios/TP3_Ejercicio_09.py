# Luna, Facundo

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if num1 > num2:
    print(f"El número mayor es {num1}")
elif num2 > num1:
    print(f"El número mayor es {num2}")
else:
    print("Ambos números son iguales")

if num1 > 0:
    print(f"El primer número ({num1}) es positivo")
elif num1 < 0:
    print(f"El primer número ({num1}) es negativo")
else:
    print(f"El primer número ({num1}) es cero")

if num2 > 0 and num2 < 100:
    print(f"El segundo número ({num2}) es mayor a 0 y menor a 100")
else:
    print(f"El segundo número ({num2}) no es mayor a 0 y menor a 100")
