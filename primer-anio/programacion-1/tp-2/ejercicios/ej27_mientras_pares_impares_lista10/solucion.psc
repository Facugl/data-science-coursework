Algoritmo ParesImparesLista10
	i <- 1
	sumaPares <- 0
	productoImpares <- 1
	Mientras (i<=10) Hacer
		Escribir 'Ingresa un número.'
		Leer numero
		esPar <- numero MOD 2=0
		Si esPar Entonces
			sumaPares <- sumaPares+numero
		SiNo
			productoImpares <- productoImpares*numero
		FinSi
		i <- i+1
	FinMientras
	Escribir 'La suma de todos los números pares es: ', sumaPares
	Escribir 'El producto de todos los números impares es: ', productoImpares
FinAlgoritmo
