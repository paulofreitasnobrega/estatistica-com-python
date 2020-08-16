"""
Exercício 001:
Existem 10 cadeiras numeradas de 1 a 10. De quantas formas duas pessoas podem
sentar-se, devendo haver ao menos uma cadeira entre elas.
"""

import numpy as np
from scipy import special


# qunatidade de arranjos possíveis de 10 elementos, tomados de 2 a 2.
arranjos = special.perm(10, 2)

# sendo a pessoa A (x) e pessoa B (y), tanto x, quanto y possuem 10
# locais diferentes para sentar-se.
y, x = np.mgrid[1:11:1, 1:11:1]

# estando x ocupando a cadeira P, e y a cadeira Q, então a distância
# entre x e y será (P-Q) ou (x-y).
#
# Havendo 10 possibilidades de acomodação para x, e 10 para y, obtem-se
# uma matriz 10x10, representando as distâncias entre x e y.
#
# sendo x < y, a distância entre x e y será negativa. Por essa razão,
# normaliza-se os sinais utilizando valores absolutos.
matriz = abs(x - y)

# estando x na caideira 1 e y na cadeira 2. A distância entre x e y será
# [1-2] = 1. Sendo 1 a representatividade da distância não permitida,
# obtem-se a quantidade de arranjos que resultam desta distância.
privacao = np.count_nonzero(matriz == 1)

# a quantidade de formas que duas pessoas podem sentar-se, devendo haver
# ao menos uma cadeira entre elas. Será a subtração da quantidade de arranjos
# possíveis de 10 elementos, tomados de 2 a 2, entre a quantidade de arranjos
# que violam a distância mínima.
resultado = arranjos - privacao

# exibindo a matriz de distâncias
print(matriz)

# exibindo o resultado
print("Resultado: {}".format(resultado))
