Algoritmo PorcentajeVaronesMujeres
	Escribir 'Ingresa el total de alumnos de la clase.'
	Leer totalAlumnos
	Si totalAlumnos<=0 Entonces
		Escribir 'Error: el total debe ser mayor a 0.'
	SiNo
		Escribir 'Ingresa el total de alumnas de la clase.'
		Leer totalMujeres
		Escribir 'Ingresa el total de alumnos varones de la clase.'
		Leer totalVarones
		Si totalMujeres+totalVarones>totalAlumnos Entonces
			Escribir 'Error: los datos ingresados no son válidos.'
		SiNo
			porcentajeMujeres <- (totalMujeres*100)/totalAlumnos
			porcentajeVarones <- (totalVarones*100)/totalAlumnos
			Escribir 'La clase esta compuesta por un ', porcentajeMujeres, ' % de mujeres y un ', porcentajeVarones, ' % de varones .'
		FinSi
	FinSi
FinAlgoritmo
