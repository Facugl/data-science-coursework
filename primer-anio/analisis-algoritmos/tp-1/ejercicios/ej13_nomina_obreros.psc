Algoritmo NominaObreros
	Definir numObrero Como Entero
	Definir horasTrabajadas Como Real
	Definir valorHora Como Real
	Definir pagoObrero, totalNomina Como Real

	valorHora <- 1500
	totalNomina <- 0

	Para numObrero <- 1 Hasta 50 Con Paso 1 Hacer
		Escribir "--- Obrero Nro: ", numObrero, " ---"
		Escribir "Ingrese horas trabajadas: "
		Leer horasTrabajadas

		pagoObrero <- horasTrabajadas * valorHora
		totalNomina <- totalNomina + pagoObrero

		Escribir "Pago a cancelar: $", pagoObrero
	FinPara

	Escribir "===== RESUMEN GENERAL ====="
	Escribir "Total nomina a cancelar (50 obreros): $", totalNomina

FinAlgoritmo