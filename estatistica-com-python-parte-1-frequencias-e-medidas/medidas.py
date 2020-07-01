"""MEDIDAS SEPARATRIZES E DISPERSÃO"""

"""
Curso: Estatística com Python parte 1: Frequências e Medidas
https://cursos.alura.com.br/course/estatistica-distribuicoes-e-medidas

Nível: Básico
Aluno: Paulo Freitas Nobrega
Professor: Rodrigo Fernando Dias

Material de apoio:
- Data Science do Zero (Joel Grus)
- Estatísitica Prática para Cientistas de Dados (Peter Bruce)
- Estatística Básica (Sonia Vieira)
- Estatística Básica (Valéria Ferreira)
- Estatística Aplicada (Abraham Laredo Sicsú)
- Matemática com Python (Guilherme A. Barucke)
- Python para Análise de Dados (Wes Mckinney)
"""


def media(conjunto: list) -> float:
    """Calcula a média de um conjunto de dados"""
    return round(sum(conjunto)/len(conjunto), 6)


def media_aparada(conjunto: list, corte: float = 0) -> float:
    """Calcula a média aparada de um conjunto de dados"""
    c, n, p = sorted(conjunto), len(conjunto), round(corte*10)

    if n <= p*2:
        raise ValueError("Proporção de corte muito grande")

    return media(c[p:n-p])


def media_ponderada(conjunto: list, pesos: list) -> float:
    """Calcula a média ponderada de um conjunto de dados"""

    if len(conjunto) != len(pesos):
        raise ValueError("Conjuntos com números de registros diferentes")

    mult = [registro*pesos[i] for i, registro in enumerate(conjunto)]

    return round(sum(mult)/sum(pesos), 6)


def mediana(conjunto: list) -> float:
    """Calcula a mediana de um conjunto de dados"""
    c, n = sorted(conjunto), len(conjunto)

    # impariedade
    impariedade = True if n % 2 else False

    # ref centro do conjunto
    meio = n//2

    return c[meio] if impariedade else media([c[meio-1], c[meio]])


def percentis(conjunto: list, percentis: list) -> list:
    """Calcula os percentis de um conjunto de dados"""
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
    """Calcula o desvio médio absoluto de um conjunto de dados"""

    # desvios
    desvios = [abs(x-media(conjunto)) for x in conjunto]

    return round(sum(desvios)/len(conjunto), 6)


def desvio_absoluto_mediano(conjunto: list, fator: float = 1.4826) -> float:
    """Calcula o desvio absoluto mediano da mediana de um conjunto de dados"""

    # desvios
    desvios = [abs(x-mediana(conjunto)) for x in conjunto]

    # fator = fator de escalamento constante
    return round(mediana(desvios)*fator, 6)


def variancia(conjunto: list, amostral: bool = True) -> float:
    """Calcula a variância de um conjunto de dados"""

    # desvios
    desvios = [(x-media(conjunto))**2 for x in conjunto]

    # amostral ou populacional
    n = len(conjunto)-1 if amostral else len(conjunto)

    return round(sum(desvios)/n, 6)


def desvio_padrao(conjunto: list, amostral: bool = True) -> float:
    """Calcula o desvio padrão de um conjunto de dados"""

    return round(variancia(conjunto, amostral)**.5, 6)
