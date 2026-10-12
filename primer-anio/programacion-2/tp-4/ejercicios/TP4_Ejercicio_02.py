# Luna, Facundo

stock = {'tornillos': 0, 'tuercas': 0, 'arandelas': 0}

while True:
    producto = input("Ingrese el producto a agregar al stock ('FIN' para terminar): ")

    if producto == "FIN":
        break

    if producto not in stock:
        print("Error: el producto no está definido en el stock")
        continue

    cantidad = int(input(f"Ingrese la cantidad de {producto} a agregar: "))
    stock[producto] = stock[producto] + cantidad

print("Stock:", stock)
