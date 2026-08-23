Algoritmo EsPrimo
	Definir n, i Como Entero
	Definir flagPrimo Como Logico
		
	Repetir
		Escribir "Ingresa un numero. Debe ser mayor a 1:"
		Leer n
		Si (n <= 1) Entonces
			Escribir "Numero invalido. Intente nuevamente."
		FinSi
	Hasta Que n > 1
	
	flagPrimo <- Verdadero
	i <- 2
	
	Mientras i <= n / 2 Y flagPrimo Hacer
		Si (n MOD i = 0) Entonces
			flagPrimo <- Falso
		FinSi
		i <- i + 1
	FinMientras
	
	Si flagPrimo Entonces
		Escribir "Es primo."
	SiNo
		Escribir "No es primo."
	FinSi
	
FinAlgoritmo