"""
Exercício 002:
Dado o seguinte conjunto de dados A = {1, 3, 6, 7, 8, 9}
Quantos números pares de 3 algarismos distintos podemos formar?
"""

import numpy as np
from itertools import permutations as perm


# conjunto de dados
conjunto = [1, 3, 6, 7, 8, 9]

# matriz contendo todos os arranjos possíveis de 6 elementos,
# tomados 3 a 3.
matriz = np.array([arranjo for arranjo in perm(conjunto, 3)])

# sendo x, y e z, as representações de centena, dezenha e unidade
# de um número de três algarismos. É possível provar a pariedade
# deste número observando apenas sua unidade (z).
#
# assim, um número par, é todo aquele que possui o resto 0,
# em uma divisão pelo número 2.
resultado = len(matriz[matriz[0:, 2] % 2 == 0])

# exibindo (parcialmente) a matriz de arranjos
print(matriz[:5])

# exibindo o resultado
print("Resultado: {}".format(resultado))
