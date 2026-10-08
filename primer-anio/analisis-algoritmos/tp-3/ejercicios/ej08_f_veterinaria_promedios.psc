Algoritmo VeterinariaPromedioEdades
	Definir i Como Entero
	Definir tipoAnimal Como Caracter
	Definir edad Como Real
	Definir sumaGatos, sumaPerros Como Real
	Definir cantGatos, cantPerros Como Entero
	Definir promedioGatos, promedioPerros Como Real
	
	sumaGatos  <- 0
	sumaPerros <- 0
	cantGatos  <- 0
	cantPerros <- 0
	
	Para i <- 1 Hasta 30 Con Paso 1 Hacer
		Escribir "--- Animal Nro ", i, " ---"
		
		Repetir
			Escribir "Ingrese el tipo de animal (G = gato / P = perro):"
			Leer tipoAnimal
			Si tipoAnimal <> "G" Y tipoAnimal <> "P" Entonces
				Escribir "Error: solo se atienden gatos (G) o perros (P)."
			FinSi
		Hasta Que tipoAnimal = "G" O tipoAnimal = "P"
		
		Repetir
			Escribir "Ingrese la edad del animal (en anios):"
			Leer edad
			Si edad < 0 Entonces
				Escribir "Error: la edad no puede ser negativa."
			FinSi
		Hasta Que edad >= 0
		
		Si tipoAnimal = "G" Entonces
			sumaGatos <- sumaGatos + edad
			cantGatos <- cantGatos + 1
		SiNo
			sumaPerros <- sumaPerros + edad
			cantPerros <- cantPerros + 1
		FinSi
	FinPara
	
	Escribir "===== RESUMEN DEL MES ====="
	
	Si cantGatos > 0 Entonces
		promedioGatos <- sumaGatos / cantGatos
		Escribir "Gatos atendidos: ", cantGatos, " - Edad promedio: ", promedioGatos
	SiNo
		Escribir "No se atendieron gatos durante el mes."
	FinSi
	
	Si cantPerros > 0 Entonces
		promedioPerros <- sumaPerros / cantPerros
		Escribir "Perros atendidos: ", cantPerros, " - Edad promedio: ", promedioPerros
	SiNo
		Escribir "No se atendieron perros durante el mes."
	FinSi
	
FinAlgoritmo
