Algoritmo PromedioEdadesCurso
	Repetir
		Escribir 'Ingresa la cantidad de alumnos del curso.'
		Leer cantidadAlumnos
	Hasta Que cantidadAlumnos>0
	Si cantidadAlumnos=1 Entonces
		Escribir 'El promedio general de edades del curso es: ', promedioEdades
	FinSi
	suma <- 0
	i <- cantidadAlumnos
	Mientras (i>0) Hacer
		Escribir 'Ingresa la edad del alumno.'
		Repetir
			Leer edadAlumno
			Si edadAlumno<1 Entonces
				Escribir 'Edad no valida.'
			FinSi
		Hasta Que edadAlumno>=1
		suma <- suma+edadAlumno
		i <- i-1
	FinMientras
	promedioEdades <- suma/cantidadAlumnos
	Escribir 'El promedio general de edades del curso es: ', promedioEdades
FinAlgoritmo
