Algoritmo CajaRegistradora
	Definir precio Como Real
	Definir total, montoPagado, vuelto Como Real
	Definir cantidadProductos Como Entero
	
	total <- 0
	cantidadProductos <- 0
	
	Escribir "===== CAJA REGISTRADORA ====="
	Escribir "Ingresa el precio del producto (ingresa 0 para finalizar):"
	Leer precio
	
	Mientras precio <> 0 Hacer
		total <- total + precio
		cantidadProductos <- cantidadProductos + 1
		
		Escribir "Producto agregado. Precio: $", precio
		Escribir "Ingrese el precio del producto (ingrese 0 para finalizar):"
		Leer precio
	FinMientras
	
	Si cantidadProductos > 0 Entonces
		Escribir "===== TICKET DE COMPRA ====="
		Escribir "Cantidad de productos: ", cantidadProductos
		Escribir "Total a pagar: $", total
		
		Escribir "Ingrese el monto con el que paga el cliente:"
		Leer montoPagado
		
		Mientras montoPagado < total Hacer
			Escribir "El monto ingresado es insuficiente. Ingrese un monto mayor o igual al total:"
			Leer montoPagado
		FinMientras
		
		vuelto <- montoPagado - total
		
		Escribir "Monto pagado: $", montoPagado
		Escribir "Vuelto a entregar: $", vuelto
	SinO
		Escribir "No se registraron productos en esta compra."
	FinSi
	
FinAlgoritmo