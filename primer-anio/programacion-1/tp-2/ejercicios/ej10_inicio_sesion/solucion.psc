Algoritmo InicioSesion
	Escribir 'Ingresa tu nombre de Usuario.'
	Leer username
	Escribir 'Ingresa tu contraseña.'
	Leer password
	usernameDB <- 'Franco'
	passwordDB <- '2022'
	Si (username=usernameDB) Entonces
		Si (password=passwordDB) Entonces
			Escribir 'Bienvenido Franco! Inicio de sesión válido!'
		SiNo
			Escribir 'Contraseña incorrecta, no se puede iniciar sesión!'
		FinSi
	SiNo
		Si (password=passwordDB) Entonces
			Escribir 'Nombre de usuario incorrecto, no se puede iniciar sesión!'
		SiNo
			Escribir 'Usuario totalmente desconocido! Fuera hacker!!'
		FinSi
	FinSi
FinAlgoritmo
