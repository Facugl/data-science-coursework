Algoritmo PromedioEdadesCurso
	Repetir
		Escribir 'Ingresa la cantidad de alumnos del curso.'
		Leer cantidadAlumnos
	Hasta Que cantidadAlumnos>1
	i <- 1
	suma <- 0
	Mientras (i<=cantidadAlumnos) Hacer
		Escribir 'Ingresa la edad del alumno.'
		Leer edadAlumno
		suma <- suma+edadAlumno
		i <- i+1
	FinMientras
	promedioEdades <- suma/cantidadAlumnos
	Escribir 'El promedio general de edades del curso es: ', promedioEdades
FinAlgoritmo
