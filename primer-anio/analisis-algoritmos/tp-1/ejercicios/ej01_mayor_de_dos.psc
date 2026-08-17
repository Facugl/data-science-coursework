Algoritmo MayorDeDos
    Definir a, b Como Real
	
    Escribir "Ingrese el primer valor:"
    Leer a
	
    Repetir
        Escribir "Ingrese el segundo valor (distinto del primero):"
        Leer b
        Si b = a Entonces
            Escribir "Error: el valor debe ser distinto al primero. Intente nuevamente."
        FinSi
    Hasta Que b <> a
	
    Si a > b Entonces
        Escribir "El mayor es: ", a
    SiNo
        Escribir "El mayor es: ", b
    FinSi
	
FinAlgoritmo
