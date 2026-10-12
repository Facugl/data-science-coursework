# Luna, Facundo

import matplotlib.pyplot as plt

years = [1900, 1970, 1990, 2000, 2020]
poblacion = [1650, 3692, 5263, 6070, 7800]

plt.plot(years, poblacion)

plt.title("Población Histórica Mundial")
plt.xlabel("Year")
plt.ylabel("Población")

plt.show()
