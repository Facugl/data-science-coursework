# Luna, Facundo

total_alumnos = int(input("Ingrese el total de alumnos del curso:"))
total_mujeres = int(input("Ingrese la cantidad de mujeres:"))
total_varones = int(input("Ingrese la cantidad de varones:"))

if total_alumnos != 0:
    porcentaje_mujeres = (total_mujeres * 100) / total_alumnos
    porcentaje_varones = (total_varones * 100) / total_alumnos
    print(f"El porcentaje de varones es {porcentaje_varones}% y el porcentaje de mujeres es {porcentaje_mujeres}%")
else:
    print("No se puede calcular el porcentaje: el total de alumnos es 0.")
