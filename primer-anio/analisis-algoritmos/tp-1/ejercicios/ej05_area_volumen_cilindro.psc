Algoritmo AreaVolumenCilindro
	Definir radio, altura, area, volumen Como Real
	
	Repetir
		Escribir "Ingresa el valor del radio del cilindro:"
		Leer radio
		Si radio <= 0 Entonces
			Escribir "El radio debe ser positivo y distinto de 0."
		FinSi
	Hasta Que radio > 0
	
	Repetir
		Escribir "Ingresa el valor de la altura del cilindro:"
		Leer altura
		Si altura <= 0 Entonces
			Escribir "La altura debe ser positiva y distinta de 0."
		FinSi
	Hasta Que altura > 0
	
	area <- (2*PI*radio*radio) + (2*PI*radio*altura) // area lateral + area de c/tapa
	volumen <- (PI*radio*radio*altura)
	
	Escribir "El area del Cilindro es: ", area
	Escribir "El volumen del cilindro es: ", volumen

FinAlgoritmo
