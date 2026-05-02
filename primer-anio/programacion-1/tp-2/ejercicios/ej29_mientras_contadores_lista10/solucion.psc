Algoritmo ContadorNumerosLista10
	i <- 1
	cantidadMultiplos4 <- 0
	cantidadMultiplos2 <- 0
	cantidadPositivos <- 0
	cantidadNegativos <- 0
	Mientras (i<=10) Hacer
		Escribir 'Ingresa un número.'
		Leer numero
		esMultiploDe4 <- numero MOD 4=0
		Si esMultiploDe4 Entonces
			cantidadMultiplos4 <- cantidadMultiplos4+1
		FinSi
		esMultiploDe2 <- numero MOD 2=0
		Si esMultiploDe2 Entonces
			cantidadMultiplos2 <- cantidadMultiplos2+1
		FinSi
		Si (numero>=0) Entonces
			cantidadPositivos <- cantidadPositivos+1
		SiNo
			cantidadNegativos <- cantidadNegativos+1
		FinSi
		i <- i+1
	FinMientras
	Escribir 'La cantidad de números múltiplos de 4 es: ', cantidadMultiplos4
	Escribir 'La cantidad de números múltiplos de 2 es: ', cantidadMultiplos2
	Escribir 'La cantidad de números positivos es: ', cantidadPositivos
	Escribir 'La cantidad de números negativos es: ', cantidadNegativos
FinAlgoritmo
