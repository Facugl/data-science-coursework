Algoritmo MayorDeTres
    Definir A, B, C Como Real
	
    Escribir "Ingrese el primer valor:"
    Leer A
	
    Repetir
        Escribir "Ingrese el segundo valor (distinto del primero):"
        Leer B
        Si B = A Entonces
            Escribir "Error: el valor debe ser distinto al primero. Intente nuevamente."
        FinSi
    Hasta Que B <> A
	
	Repetir
        Escribir "Ingrese el tercer valor (distinto del primero y el segundo):"
        Leer C
        Si C = A O C = B Entonces
            Escribir "Error: el valor debe ser distinto al primero y el segundo. Intente nuevamente."
        FinSi
    Hasta Que C <> A Y C <> B
	
	Si A > B Entonces
		Si A > C Entonces
			Escribir "El mayor es: ", A
		SiNo
			Escribir "El mayor es: ", C
		FinSi
	SiNo
		Si B > C Entonces
			Escribir "El mayor es: ", B
		SiNo
			Escribir "El mayor es: ", C
		FinSi
	FinSi
	
	Si A < B Entonces
		Si A < C Entonces
			Escribir "El menor es: ", A
		SiNo
			Escribir "El menor es: ", C
		FinSi
	SiNo
		Si B < C Entonces
			Escribir "El menor es: ", B
		SiNo
			Escribir "El menor es: ", C
		FinSi
	FinSi
	
FinAlgoritmo
