a = 0
b = int(input("ingrese valor b: "))
if b == 100:
    for i in range(0, n, 1):
        for j in range(0, n, 1):
            a += 1
    print("valor a entrando con b=100: ", a)
else:
    for i in range(0, n, 1):
        a += 1
    print("valor a entrando con b<>100: ", a)
