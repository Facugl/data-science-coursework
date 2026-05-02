Algoritmo ParaParesImparesLista10
	sumaPares <- 0
	productoImpares <- 1
	Para i<-1 Hasta 10 Con Paso 1 Hacer
		Escribir 'Ingresa un número:'
		Leer numero
		esPar <- (numero MOD 2)=0
		Si (esPar) Entonces
			sumaPares <- sumaPares+numero
		SiNo
			productoImpares <- productoImpares*numero
		FinSi
	FinPara
	Escribir 'La suma de los números pares ingresados es: ', sumaPares
	Escribir 'El producto de los números impares ingresados es: ', productoImpares
FinAlgoritmo
