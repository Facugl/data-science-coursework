# Luna, Facundo

import numpy as np

l1 = list(range(10))
array = np.array(l1)

mayores_a_3 = np.where(array > 3, array, 0)
pares = np.where(array % 2 == 0, array, 0)

print(f"Array original: {array}")
print(f"Mayores a 3: {mayores_a_3}")
print(f"Pares: {pares}")
