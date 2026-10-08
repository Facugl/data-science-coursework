Algoritmo SumatoriaDiezNumerosAzar
	Definir i, numero, suma Como Entero
	
	suma <- 0
	
	Para i <- 1 Hasta 10 Con Paso 1 Hacer
		// Aleatorio(1,20) genera un entero al azar en el rango [1..20]
		numero <- Aleatorio(1, 20)
		suma <- suma + numero
		Escribir "Numero ", i, ": ", numero
	FinPara
	
	Escribir "----------------------------------------"
	Escribir "La sumatoria de los 10 numeros es: ", suma
	
FinAlgoritmo
