Algoritmo ParaPromedioEdadesCurso
	Escribir 'Ingresa la cantidad de alumnos del curso. (numero > 0)'
	Repetir
		Leer cantidadAlumnos
		Si (cantidadAlumnos<1) Entonces
			Escribir 'La cantidad no puede ser negativa o 0.'
		FinSi
	Hasta Que cantidadAlumnos>=1
	Para i<-1 Hasta cantidadAlumnos Con Paso 1 Hacer
		Escribir 'Ingresa la edad del alumno:'
		Repetir
			Leer edadAlumno
			Si (edadAlumno<1) Entonces
				Escribir 'La edad del alumno no puede ser negativa o 0.'
			FinSi
		Hasta Que edadAlumno>=1
		sumaEdades <- sumaEdades+edadAlumno
	FinPara
	Escribir 'El promedio general de edades del curso es de: ', (sumaEdades/cantidadAlumnos), ' años.'
FinAlgoritmo
