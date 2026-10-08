Algoritmo CaraDadoEnLetras
	Definir cara Como Entero
	
	// Aleatorio(1,6) genera un entero al azar entre 1 y 6 inclusive
	cara <- Aleatorio(1, 6)
	
	Escribir "Se lanzo el dado y salio el numero ", cara
	
	Segun cara Hacer
		1:
			Escribir "En letras: UNO"
		2:
			Escribir "En letras: DOS"
		3:
			Escribir "En letras: TRES"
		4:
			Escribir "En letras: CUATRO"
		5:
			Escribir "En letras: CINCO"
		6:
			Escribir "En letras: SEIS"
		De Otro Modo:
			Escribir "Valor fuera del rango valido de un dado."
	FinSegun
	
FinAlgoritmo
