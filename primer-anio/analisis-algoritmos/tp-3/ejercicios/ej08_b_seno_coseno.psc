Algoritmo SenoCoseno
	Definir anguloGrados, anguloRadianes Como Real
	Definir valorSeno, valorCoseno Como Real
	
	Escribir "Ingrese el valor de un angulo en grados:"
	Leer anguloGrados
	
	// Las funciones trigonometricas de PSeInt trabajan en radianes
	anguloRadianes <- anguloGrados * PI / 180
	
	valorSeno <- sen(anguloRadianes)
	valorCoseno <- cos(anguloRadianes)
	
	Escribir "Seno de ", anguloGrados, " grados: ", valorSeno
	Escribir "Coseno de ", anguloGrados, " grados: ", valorCoseno
	
FinAlgoritmo
