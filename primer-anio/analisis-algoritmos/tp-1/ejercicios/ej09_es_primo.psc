Algoritmo EsPrimo
	Definir n, i Como Entero
	Definir esPrimo Como Logico
	
	Repetir
		Escribir "Ingresa un numero. Debe ser mayor a 1:"
		Leer n
		Si (n <= 1) Entonces
			Escribir "Numero invalido. Intente nuevamente."
		FinSi
	Hasta Que n > 1
	
	esPrimo <- Verdadero
	i <- 2
	
	Mientras i <= n / 2 Y esPrimo Hacer
		Si (n MOD i = 0) Entonces
			esPrimo <- Falso
		FinSi
		i <- i + 1
	FinMientras
	
	Si esPrimo Entonces
		Escribir "Es primo."
	SiNo
		Escribir "No es primo."
	FinSi
	
FinAlgoritmo