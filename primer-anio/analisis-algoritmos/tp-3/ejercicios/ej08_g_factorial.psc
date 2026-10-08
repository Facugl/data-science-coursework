Algoritmo FactorialIterativo
	Definir n, i Como Entero
	Definir factorial Como Real
	Repetir
		Escribir "Ingrese un numero entero N mayor o igual a 0:"
		Leer n
		Si n < 0 Entonces
			Escribir "Error: no existe factorial de un negativo."
		FinSi
	Hasta Que n >= 0
	
	factorial <- 1
	// Si n = 0 el bucle no se ejecuta y queda 0! = 1
	Para i <- 2 Hasta n Con Paso 1 Hacer
		factorial <- factorial * i
	FinPara
	
	Escribir "El factorial de ", n, " es: ", factorial
FinAlgoritmo
