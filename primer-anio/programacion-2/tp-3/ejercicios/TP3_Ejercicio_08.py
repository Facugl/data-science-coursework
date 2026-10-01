# Luna, Facundo

nota = int(input("Ingrese la nota del examen: "))

if nota == 10:
    print("Sobresaliente! Felicitaciones!")
elif nota >= 7:
    print("Promocionado! Bravo!")
elif nota >= 4:
    print("Aprobado. Bien pero a poner más empeño!")
else:
    print("Desaprobado. Prepararse para el recuperatorio!")
