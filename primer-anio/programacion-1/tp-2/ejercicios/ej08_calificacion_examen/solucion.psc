Algoritmo CalificacionExamen
	Escribir 'Ingresa la calificacion del exámen.'
	Leer calificacion
	Si (calificacion<0 O calificacion>10) Entonces
		Escribir 'Calificación no válida.'
	SiNo
		Si calificacion<4 Entonces
			Escribir 'Libre.'
		SiNo
			Si calificacion<7 Entonces
				Escribir 'Regular.'
			SiNo
				Escribir 'Promocionado.'
			FinSi
		FinSi
	FinSi
FinAlgoritmo
