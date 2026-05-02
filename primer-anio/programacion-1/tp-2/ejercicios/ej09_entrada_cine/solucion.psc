Algoritmo EntradaCine
	Definir edad Como Entero
	Definir respuesta Como Cadena
	Definir tieneEntrada Como Lógico
	Repetir
		Escribir 'Ingresa tu edad:'
		Leer edad
		Si edad<0 Entonces
			Escribir 'La edad no puede ser negativa.'
		FinSi
	Hasta Que edad>=0
	Escribir '¿Tienes una entrada para el cine? (si/no):'
	Leer respuesta
	Si respuesta='si' Entonces
		tieneEntrada <- Verdadero
	SiNo
		tieneEntrada <- Falso
	FinSi
	Si edad>=16 Y tieneEntrada Entonces
		Escribir 'Usted SI puede entrar a la sala de cine, que disfrute la película!'
	SiNo
		Escribir 'Usted NO puede entrar a la sala de cine, lo siento mucho!'
	FinSi
FinAlgoritmo
