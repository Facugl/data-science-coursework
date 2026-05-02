Algoritmo ParaSumaProducto5Nums
	suma <- 0
	producto <- 1
	Para i<-1 Hasta 5 Con Paso 1 Hacer
		Escribir 'Ingresa un número:'
		Leer numero
		suma <- suma+numero
		producto <- producto*numero
	FinPara
	Escribir 'La suma de los números ingresados es: ', suma
	Escribir 'El producto de los números ingresados es: ', producto
FinAlgoritmo
