Algoritmo RepetirMultiplos5
	i <- 1
	Repetir
		esMultiploDe5 <- (i MOD 5)=0
		Si (esMultiploDe5) Entonces
			Escribir i
		FinSi
		i <- i+1
	Hasta Que i>=101
FinAlgoritmo
