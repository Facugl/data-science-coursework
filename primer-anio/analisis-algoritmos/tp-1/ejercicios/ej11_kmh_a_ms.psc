Algoritmo ConversorVelocidad
    Definir velocidadEnKMH, velocidadEnMS Como Real
	
	Escribir "Ingresa la velocidad en Km/h:"
    Leer velocidadEnKMH
	
	velocidadEnMS <- velocidadEnKMH * 1000 / (60*60)
	
    Escribir "La velocidad en m/s es:", velocidadEnMS
FinAlgoritmo