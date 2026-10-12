# Luna, Facundo

import numpy as np

array = np.array([1, 2, 4, 7])

mascara_mayores_a_1 = array > 1
mascara_pares = array % 2 == 0

print(f"Array original: {array}")
print(f"Máscara de mayores a 1: {mascara_mayores_a_1}")
print(f"Números mayores a 1: {array[mascara_mayores_a_1]}")
print(f"Máscara de pares: {mascara_pares}")
print(f"Números pares: {array[mascara_pares]}")
