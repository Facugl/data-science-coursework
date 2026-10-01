# Luna, Facundo

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

diferencia = num1 - num2

if diferencia > 0:
    print(f"La diferencia ({diferencia}) es positiva")
elif diferencia < 0:
    print(f"La diferencia ({diferencia}) es negativa")
else:
    print("La diferencia es cero")
