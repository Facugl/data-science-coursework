Algoritmo PromedioNotas
	Definir nota Como Real
	Definir suma, promedio Como Real
	Definir contador Como Entero

	suma <- 0
	contador <- 0
	
	Escribir "Ingresa una nota (ingresa 0 para finalizar):"
	Leer nota
	
	Mientras nota <> 0 Hacer
		suma <- suma + nota
		contador <- contador + 1
		
		Escribir "Ingresa una nota (ingresa 0 para finalizar):"
		Leer nota
	FinMientras
	
	Si contador > 0 Entonces
		promedio <- suma / contador
		Escribir "El promedio de las notas es: ", promedio
	SinO
		Escribir "No se ingresaron notas para calcular el promedio."
	FinSi
	
FinAlgoritmo