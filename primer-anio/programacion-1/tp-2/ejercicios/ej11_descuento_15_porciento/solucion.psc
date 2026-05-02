Algoritmo Descuento
	Escribir 'Ingresa un número para aplicarle un descunto del 15%.'
	Repetir
		Leer numero
		Si (numero<0) Entonces
			Escribir 'Ingresa un monto mayor o igual a 0.'
		FinSi
	Hasta Que numero>=0
	numero <- numero*0.85
	Escribir 'Luego de aplicar el descuento: ', numero
FinAlgoritmo
