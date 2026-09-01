# Luna, Facundo

primera_palabra = str(input("Ingrese la primera palabra:"))
segunda_palabra = str(input("Ingrese la segunda palabra:"))
tercera_palabra = str(input("Ingrese la tercera palabra:"))

if primera_palabra and segunda_palabra and tercera_palabra:
    acronimo = (primera_palabra[0] + segunda_palabra[0] + tercera_palabra[0]).upper()
    print(f"El acrónimo es {acronimo}")
else:
    print("Debe ingresar las tres palabras para poder formar el acrónimo.")