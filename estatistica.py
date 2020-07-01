"""
Curso: Estatística com Python

Parte I: Frequências e Medidas
https://cursos.alura.com.br/course/estatistica-distribuicoes-e-medidas

Parte II: Probabilidade e Amostragem
https://cursos.alura.com.br/course/estatistica-probabilidade-e-amostragem

Ano: 2020
Nível: Básico
Aluno: Paulo Freitas Nobrega
Professor: Rodrigo Fernando Dias
Plataforma: Alura Cursos Online

Material de apoio:
- Data Science do Zero (Joel Grus)
- Estatísitica Prática para Cientistas de Dados (Peter Bruce)
- Estatística Básica (Sonia Vieira)
- Estatística Básica (Valéria Ferreira)
- Estatística Aplicada (Abraham Laredo Sicsú)
- Matemática com Python (Guilherme A. Barucke)
- Python para Análise de Dados (Wes Mckinney)
"""


# Parte I: Frequências e Medidas


def media(conjunto: list) -> float:
    """
    Calcula a média de um conjunto de dados
    """

    return sum(conjunto) / len(conjunto)


def media_aparada(conjunto: list, corte: float = 0) -> float:
    """
    Calcula a média aparada de um conjunto de dados
    """

    c, n, p = sorted(conjunto), len(conjunto), round(corte*10)

    if n <= p*2:
        raise ValueError("Proporção de corte muito grande")

    return media(c[p:n-p])


def media_ponderada(conjunto: list, pesos: list) -> float:
    """
    Calcula a média ponderada de um conjunto de dados
    """

    if len(conjunto) != len(pesos):
        raise ValueError("Conjuntos com números de registros diferentes")

    mult = [registro*pesos[i] for i, registro in enumerate(conjunto)]

    return sum(mult) / sum(pesos)


def mediana(conjunto: list) -> float:
    """
    Calcula a mediana de um conjunto de dados
    """

    c, n = sorted(conjunto), len(conjunto)

    # impariedade
    impariedade = True if n % 2 else False

    # ref centro do conjunto
    meio = n//2

    return c[meio] if impariedade else media([c[meio-1], c[meio]])


def percentis(conjunto: list, percentis: list) -> list:
    """
    Calcula os percentis de um conjunto de dados
    """

    c, n = sorted(conjunto), len(conjunto)

    # divisao
    # (i*n/100) - contudo os percentis são atribuidos em
    # em porcentagem. [.5] = 50%. Assim ignora-se a divisão.
    p = [i*n for i in percentis]

    # Se a divisão resultar num número fracionário, arredonde-o
    # para cima (em programação, por índices começarem em 0, se
    # arredonda para baixo) e o valor do quartil será a observação
    # encontrada nesta posição.

    # Se a divisão for um número inteiro, o quartil será a media
    # aritmética da observação que ocupar a posição encontrada
    # com a observação que ocupar a posição imediatamente seguinte.
    return [c[int(x)] if x % 2 else media([c[int(x)-1], c[int(x)]]) for x in p]


def desvio_medio_absoluto(conjunto: list) -> float:
    """
    Calcula o desvio médio absoluto de um conjunto de dados
    """

    # desvios
    desvios = [abs(x-media(conjunto)) for x in conjunto]

    return sum(desvios) / len(conjunto)


def desvio_absoluto_mediano(conjunto: list, fator: float = 1.4826) -> float:
    """
    Calcula o desvio absoluto mediano da mediana de um conjunto de dados
    """

    # desvios
    desvios = [abs(x-mediana(conjunto)) for x in conjunto]

    # fator = fator de escalamento constante
    return mediana(desvios) * fator


def variancia(conjunto: list, amostral: bool = True) -> float:
    """
    Calcula a variância de um conjunto de dados
    """

    # desvios
    desvios = [(x-media(conjunto))**2 for x in conjunto]

    # amostral ou populacional
    n = len(conjunto)-1 if amostral else len(conjunto)

    return sum(desvios)/n


def desvio_padrao(conjunto: list, amostral: bool = True) -> float:
    """
    Calcula o desvio padrão de um conjunto de dados
    """

    return variancia(conjunto, amostral)**.5


# Parte II: Probabilidade e Amostragem


def fatorial(n: int) -> int:
    """
    Calcula o fatorial de um número
    """
    return 1 if n < 1 else n * fatorial(n-1)


def permutacoes(n: int, k: int) -> float:
    """
    Calcula permutações
    """

    return fatorial(n) / fatorial(n-k)


def combinacoes(n: int, k: int) -> float:
    """
    Calcula combinações
    """

    return permutacoes(n, k) / fatorial(k)


def dist_binomial_pmf(s, n: int, p: float) -> list:
    """
    Determina a probabilidade de observar k sucessos em n
    ensaios, em que a probabilidade de sucesso para cada
    ensaio seja p
    """

    # n = número de ensaios
    # p = probabilidade de sucesso
    # q = probabilidade de fracasso
    # k = número de sucesso desejado
    q = 1 - p

    # s é um variável auxiliar
    # poderá conter um valor inteiro ou uma lista de inteiros
    if not isinstance(s, list):
        s = [s]

    return [combinacoes(n, k) * (p**k) * (q**(n-k)) for k in s]


def dist_binomial_cdf(k: int, n: int, p: float) -> float:
    """
    Determina a probabilidade de se observar k sucessos
    ou menos em n ensaios, em que a probabilidade de
    sucesso para cada ensaio seja p
    """

    # sucessos = [0, ..., k+1]
    sucessos = [i for i in range(k+1)]

    return sum(dist_binomial_pmf(sucessos, n, p))


def dist_binomial_sf(k: int, n: int, p: float) -> float:
    """
    Determina a probabilidade de se observar k sucessos
    ou mais em n ensaios, em que a probabilidade de
    sucesso para cada ensaio seja p
    """

    return 1 - dist_binomial_cdf(k, n, p)
