# Luna, Facundo

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 200)
y1 = x ** 2
y2 = x ** 3

plt.plot(x, y1, label="**2")
plt.plot(x, y2, label="**3")

plt.title("Ejercicio_10")
plt.legend()
plt.grid(True)

plt.show()
