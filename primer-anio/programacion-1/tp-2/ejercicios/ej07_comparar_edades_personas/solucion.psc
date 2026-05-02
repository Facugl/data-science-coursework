Algoritmo CompararEdadesPersonas
	Escribir 'Ingresa el nombre de la primera persona.'
	Leer nombre1
	Escribir 'Ingresa el apellido de la primera persona.'
	Leer apellido1
	Repetir
		Escribir 'Ingresa la edad de la primera persona. Debe ser un número positivo.'
		Leer edad1
	Hasta Que edad1>=0
	Escribir 'Ingresa el nombre de la segunda persona.'
	Leer nombre2
	Escribir 'Ingresa el apellido de la segunda persona.'
	Leer apellido2
	Repetir
		Escribir 'Ingresa la edad de la segunda persona. Debe ser un número positivo.'
		Leer edad2
	Hasta Que edad2>=0
	Si edad1>edad2 Entonces
		Escribir nombre1, ' ', apellido1, ' tiene mayor edad que ', nombre2, ' ', apellido2, '.'
	SiNo
		Si edad2>edad1 Entonces
			Escribir nombre2, ' ', apellido2, ' tiene mayor edad que ', nombre1, ' ', apellido1, '.'
		SiNo
			Escribir nombre1, ' ', apellido1, ' y ', nombre2, ' ', apellido2, ' tienen la misma edad.'
		FinSi
	FinSi
FinAlgoritmo
