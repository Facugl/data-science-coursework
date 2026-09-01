# Luna, Facundo

nombre_padre1 = str(input("Ingrese el nombre completo del padre_1: "))
nombre_padre2 = str(input("Ingrese el nombre completo del padre_2: "))
nombre_hijo = str(input("Ingrese el nombre del hijo/a: "))

apellido_padre1 = nombre_padre1.split(' ')[1]
apellido_padre2 = nombre_padre2.split(' ')[1]

nombre_completo_hijo = f"{nombre_hijo} {apellido_padre1} {apellido_padre2}"

print(f"El nombre completo del hijo/a es {nombre_completo_hijo}")
