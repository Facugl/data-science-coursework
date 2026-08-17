Algoritmo Estacionamiento
    Definir horaEntrada, horaSalida Como Entero
    Definir tarifaPrimeraHora, tarifaPorHora, tarifa Como Real
    tarifaPrimeraHora <- 200
    tarifaPorHora <- 100
    
    Repetir
        Escribir "Ingresa la hora de entrada (0-23):"
        Leer horaEntrada
        Si (horaEntrada < 0 O horaEntrada > 23) Entonces
            Escribir "Error: la hora debe estar entre 0 y 23."
        FinSi
    Hasta Que horaEntrada >= 0 Y horaEntrada <= 23
    
    Repetir
        Escribir "Ingresa la hora de salida (0-23):"
        Leer horaSalida
        Si (horaSalida < horaEntrada O horaSalida > 23) Entonces
            Escribir "Error: la hora de salida debe ser mayor o igual a la de entrada y estar entre 0 y 23."
        FinSi
    Hasta Que horaSalida >= horaEntrada Y horaSalida <= 23
	// Nota: Se asume que la entrada y la salida ocurren el mismo dia.
    
    Si (horaSalida - horaEntrada <= 1) Entonces
        tarifa <- tarifaPrimeraHora
    SiNo
        tarifa <- tarifaPrimeraHora + tarifaPorHora * ((horaSalida - horaEntrada) - 1)
    FinSi
    
    Escribir "La tarifa total es: $", tarifa
FinAlgoritmo