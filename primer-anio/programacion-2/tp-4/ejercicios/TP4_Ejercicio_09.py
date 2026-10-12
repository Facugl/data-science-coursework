# Luna, Facundo

import numpy as np
import matplotlib.pyplot as plt

y = np.linspace(-10, 10, 200)
x = y ** 2

plt.plot(x, y, color="green", label="Ej_9")

plt.title("Valores x e y")
plt.legend()

plt.show()
