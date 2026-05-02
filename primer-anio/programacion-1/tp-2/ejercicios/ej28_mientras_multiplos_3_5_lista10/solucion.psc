Algoritmo SumaYProductoMultiplosLista10
	i <- 1
	sumaMultiplos3 <- 0
	productoMultiplos5 <- 1
	Mientras (i<=10) Hacer
		Escribir 'Ingresa un número.'
		Leer numero
		esMultiploDe3 <- numero MOD 3=0
		Si esMultiploDe3 Entonces
			sumaMultiplos3 <- sumaMultiplos3+numero
		FinSi
		esMultiploDe5 <- numero MOD 5=0
		Si esMultiploDe5 Entonces
			productoMultiplos5 <- productoMultiplos5*numero
		FinSi
		i <- i+1
	FinMientras
	Escribir 'La suma de todos los números múltiplos de 3 es: ', sumaMultiplos3
	Escribir 'El producto de todos los números múltiplos de 5. es: ', productoMultiplos5
FinAlgoritmo
