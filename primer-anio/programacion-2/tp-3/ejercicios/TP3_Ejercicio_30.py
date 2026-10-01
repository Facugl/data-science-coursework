# Luna, Facundo

operador = ""

while operador != "FIN":
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operador = str(input("Ingrese la operación a realizar (+, -, *, /, **) o 'FIN' para terminar: "))

    if operador == "+":
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")
    elif operador == "-":
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")
    elif operador == "*":
        resultado = num1 * num2
        print(f"{num1} * {num2} = {resultado}")
    elif operador == "/":
        if num2 != 0:
            resultado = num1 / num2
            print(f"{num1} / {num2} = {resultado}")
        else:
            print("Error: no se puede dividir por cero")
    elif operador == "**":
        resultado = num1 ** num2
        print(f"{num1} ** {num2} = {resultado}")
    elif operador == "FIN":
        print("Fin del programa")
    else:
        print("Error: operador no soportado")
