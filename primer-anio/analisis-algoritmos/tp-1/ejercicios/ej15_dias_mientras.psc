Algoritmo ConversionDias
	Definir diasIngresados Como Entero
	Definir anios, meses, semanas, dias Como Entero
	
	anios <- 0
	meses <- 0
	semanas <- 0
	dias <- 0
	
	Escribir "Ingresa la cantidad de dias:"
	Leer diasIngresados
	dias <- diasIngresados
	
	Mientras dias >= 365 Hacer
		anios <- anios + 1
		dias <- dias - 365
	FinMientras
	
	Mientras dias >= 30 Hacer
		meses <- meses + 1
		dias <- dias - 30
	FinMientras
	
	Mientras dias >= 7 Hacer
		semanas <- semanas + 1
		dias <- dias - 7
	FinMientras
	
	Escribir "El numero de dias ingresado (", diasIngresados, ") equivale a:"
	Escribir "Años: ", anios
	Escribir "Meses: ", meses
	Escribir "Semanas: ", semanas
	Escribir "Dias: ", dias
	
FinAlgoritmo