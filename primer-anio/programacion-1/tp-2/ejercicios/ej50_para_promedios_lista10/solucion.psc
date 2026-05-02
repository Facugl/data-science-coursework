Algoritmo ParaPromedioLista10
	suma <- 0
	cantidadFinal <- 10
	sumaPositivos <- 0
	cantidadPositivos <- 0
	Para i<-1 Hasta cantidadFinal Con Paso 1 Hacer
		Escribir 'Ingresa un número:'
		Leer numero
		suma <- suma+numero
		Si (numero>0) Entonces
			sumaPositivos <- sumaPositivos+numero
			cantidadPositivos <- cantidadPositivos+1
		FinSi
	FinPara
	Escribir 'El promedio de todos los números ingresados es: ', (suma/cantidadFinal)
	Escribir 'El promedio de los números positivos es: ', (sumaPositivos/cantidadPositivos)
FinAlgoritmo
