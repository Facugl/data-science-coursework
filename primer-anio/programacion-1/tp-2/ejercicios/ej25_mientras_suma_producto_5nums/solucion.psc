Algoritmo SumaYProductoDe5Nums
	i <- 1
	suma <- 0
	producto <- 1
	Mientras i<=5 Hacer
		Repetir
			Escribir 'Ingresa en número.'
			Leer numero
			suma <- suma+numero
			producto <- producto*numero
		Hasta Que i<=5
		i <- i+1
	FinMientras
	Escribir 'La suma de los 5 números es: ', suma
	Escribir 'El producto de los 5 números es: ', producto
FinAlgoritmo
