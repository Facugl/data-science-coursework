Algoritmo NombreNVeces
	i <- 1
	Escribir 'Ingresa el nombre de una persona.'
	Leer nombre
	Escribir 'Ingresa la cantidad de repeticiones.'
	Repetir
		Leer n
		Si (n<0) Entonces
			Escribir 'La cantidad no puede ser negativa.'
		FinSi
	Hasta Que n>=0
	Mientras (i<=n) Hacer
		Escribir nombre, ' ', i
		i <- i+1
	FinMientras
FinAlgoritmo
