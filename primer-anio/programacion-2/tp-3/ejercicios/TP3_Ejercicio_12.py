# Luna, Facundo

temp1 = float(input("Ingrese la primera temperatura: "))
temp2 = float(input("Ingrese la segunda temperatura: "))
temp3 = float(input("Ingrese la tercera temperatura: "))

if temp1 >= temp2 and temp1 >= temp3:
    maxima = temp1
elif temp2 >= temp1 and temp2 >= temp3:
    maxima = temp2
else:
    maxima = temp3

if temp1 <= temp2 and temp1 <= temp3:
    minima = temp1
elif temp2 <= temp1 and temp2 <= temp3:
    minima = temp2
else:
    minima = temp3

promedio = (temp1 + temp2 + temp3) / 3

print(f"La temperatura máxima ingresada es {maxima}")
print(f"La temperatura mínima ingresada es {minima}")
print(f"El promedio de las temperaturas ingresadas es {promedio}")
