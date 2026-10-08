Algoritmo PerimetroCircunferencia
	Definir radio, perimetro Como Real
	
	Repetir
		Escribir "Ingrese el radio de la circunferencia (debe ser mayor a 0):"
		Leer radio
		Si radio <= 0 Entonces
			Escribir "Error: el radio debe ser mayor a 0. Intente nuevamente."
		FinSi
	Hasta Que radio > 0
	
	perimetro <- 2 * PI * radio
	
	Escribir "El perimetro de la circunferencia es: ", perimetro
	
FinAlgoritmo
