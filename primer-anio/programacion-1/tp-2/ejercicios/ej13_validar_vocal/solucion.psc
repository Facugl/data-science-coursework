Algoritmo ValidarVocal
	Escribir 'Ingresa una letra.'
	Leer letra
	letra <- Minusculas(letra)
	
	Si (letra='a' O letra='e' O letra='i' O letra='o' O letra='u') Entonces
		Escribir 'Es Vocal.'
	SiNo
		Escribir 'No es Vocal.'
	FinSi
FinAlgoritmo
