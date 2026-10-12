# Luna, Facundo

import matplotlib.pyplot as plt

mes = [3, 4, 5, 6]
gasto_carne = [1650, 2600, 3100, 4000]
gasto_verdura = [2500, 2200, 1800, 600]

gasto_total = []

for i in range(len(mes)):
    gasto_total.append(gasto_carne[i] + gasto_verdura[i])

plt.plot(mes, gasto_carne, label="Gasto en carne")
plt.plot(mes, gasto_verdura, label="Gasto en verdura")
plt.plot(mes, gasto_total, label="Gasto total")

plt.title("Gastos por mes")
plt.xlabel("Mes")
plt.ylabel("Gasto")
plt.xticks(mes, ["Marzo", "Abril", "Mayo", "Junio"])
plt.legend()

plt.show()
