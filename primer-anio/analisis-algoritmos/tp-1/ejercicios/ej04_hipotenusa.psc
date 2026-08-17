Algoritmo HipotenusaTriangulo
	Definir catetoA, catetoB, hipotenusa Como Real
	
	Repetir
		Escribir "Ingresa el valor del primer Cateto:"
		Leer catetoA
		Si catetoA <= 0 Entonces
			Escribir "Ingreso un valor positivo distinto de 0."
		FinSi
	Hasta Que catetoA > 0
	
	Repetir
		Escribir "Ingresa el valor del segundo Cateto:"
		Leer catetoB
		Si catetoB <= 0 Entonces
			Escribir "Ingreso un valor positivo distinto de 0."
		FinSi
	Hasta Que catetoB > 0
	
	hipotenusa <- raiz((catetoA*catetoA) + (catetoB*catetoB))
	
	Escribir "El valor de la hipotenusa es: ", hipotenusa

FinAlgoritmo
