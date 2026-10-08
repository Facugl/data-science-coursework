Algoritmo Hipotenusa
	Definir cateto1, cateto2, hipotenusa Como Real
	
	Repetir
		Escribir "Ingrese la longitud del primer cateto:"
		Leer cateto1
		Si cateto1 <= 0 Entonces
			Escribir "Error: la longitud debe ser mayor a 0."
		FinSi
	Hasta Que cateto1 > 0
	
	Repetir
		Escribir "Ingrese la longitud del segundo cateto:"
		Leer cateto2
		Si cateto2 <= 0 Entonces
			Escribir "Error: la longitud debe ser mayor a 0."
		FinSi
	Hasta Que cateto2 > 0
	
	hipotenusa <- rc(cateto1^2 + cateto2^2)
	
	Escribir "La hipotenusa del triangulo rectangulo es: ", hipotenusa
	
FinAlgoritmo
