Algoritmo ParaContadoresLista10
	cantidadMultiplos4 <- 0
	cantidadMultiplos2 <- 0
	cantidadPositivos <- 0
	cantidadNegativos <- 0
	Para i<-1 Hasta 10 Con Paso 1 Hacer
		Escribir 'Ingresa un número:'
		Leer numero
		esMultiplo4 <- (numero MOD 4)=0
		Si (esMultiplo4) Entonces
			cantidadMultiplos4 <- cantidadMultiplos4+1
		FinSi
		esMultiplo2 <- (numero MOD 2)=0
		Si (esMultiplo2) Entonces
			cantidadMultiplos2 <- cantidadMultiplos2+1
		FinSi
		Si (numero>=0) Entonces
			cantidadPositivos <- cantidadPositivos+1
		FinSi
		Si (numero<0) Entonces
			cantidadNegativos <- cantidadNegativos+1
		FinSi
	FinPara
	Escribir 'La cantidad de números múltiplo de 4 es: ', cantidadMultiplos4
	Escribir 'La cantidad de números múltiplo de 2 es: ', cantidadMultiplos2
	Escribir 'La cantidad de números positivos es: ', cantidadPositivos
	Escribir 'La cantidad de números negativos es: ', cantidadNegativos
FinAlgoritmo
