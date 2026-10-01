# Luna, Facundo

cantidad_alumnos = int(input("Ingrese la cantidad de alumnos del curso: "))

suma_edades = 0

for i in range(1, cantidad_alumnos + 1):
    edad = int(input(f"Ingrese la edad del alumno {i}: "))
    suma_edades = suma_edades + edad

promedio_edad = suma_edades / cantidad_alumnos

print(f"El promedio general de edad del curso es {promedio_edad}")
