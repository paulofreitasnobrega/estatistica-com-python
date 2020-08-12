"""
CONJUNTO DE TESTES

Material complementar do Curso: Estatística com Python

Ano: 2020
Nível: Básico
Aluno: Paulo Freitas Nobrega
Professor: Rodrigo Fernando Dias
Plataforma: Alura Cursos Online

Parte I: Frequências e Medidas
https://cursos.alura.com.br/course/estatistica-distribuicoes-e-medidas

Parte II: Probabilidade e Amostragem
https://cursos.alura.com.br/course/estatistica-probabilidade-e-amostragem
"""

import pytest

from estatistica import (
    media, media_aparada, media_ponderada, mediana,
    percentis, desvio_medio_absoluto, desvio_absoluto_mediano,
    variancia, desvio_padrao, fatorial, permutacoes, arranjos,
    combinacoes, dist_binomial_pmf, dist_binomial_cdf,
    dist_binomial_sf
)


# Parte I: Frequências e medidas


@pytest.mark.parametrize('list, expected', [
    # conjunto normal
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 5),
    # média de 0
    ([0], 0),
    # conjunto vazio
    ([], 0),
    # valores negativos
    ([15, 28.5, -3.33, 4], 11.0425)
])
def test_media(list: list, expected: list):
    """Testa a função media"""
    assert media(list) == expected


@pytest.mark.parametrize('list, cut, expected', [
    # média aritmética
    ([1, 2, 3, 4, 5, 0, 450, 6, 7, 8, 9], 0, 45),
    # média aparada (10%)
    ([1, 2, 3, 4, 5, 0, 450, 6, 7, 8, 9], .1, 5)
])
def test_media_aparada(list: list, cut: float, expected: list):
    """Testa a função média aparada"""
    assert media_aparada(list, cut) == expected


@pytest.mark.parametrize('list, weights, expected', [
    # média aritmética
    ([7, 8, 7.5, 5, 10], [.1, .1, .1, .1, .1], 7.5),
    # média ponderada
    ([7, 8, 7.5, 5, 10], [1, 1, .5, .2, .1], 7.410714285714285)
])
def test_media_ponderada(list: list, weights: list, expected: list):
    """Testa a função média ponderada"""
    assert media_ponderada(list, weights) == expected


@pytest.mark.parametrize('list, expected', [
    ([8, 10, 4, 8, 6, 10, 8], 8)
])
def test_mediana(list: list, expected: list):
    """Testa a função mediana"""
    assert mediana(list) == expected


@pytest.mark.parametrize('list, percentis_list, expected', [
    ([2.4, 2.7, 2.9, 3.1, 3.3, 3.5, 3.5, 3.8, 3.9, 4.0, 4.0,
     4.1, 4.2, 4.3, 4.4, 4.4, 4.6, 4.8, 4.9, 5.0, 5.0, 5.0, 5.2,
     5.3, 5.4, 5.5, 5.7, 5.9, 6.0, 6.1, 6.2, 6.3, 6.5, 6.6, 6.7,
     6.8, 6.8, 7.0, 7.1, 7.1], [.87], [6.7])
])
def test_percentis(list: list, percentis_list: list, expected: list):
    """Testa a função percentis"""
    assert percentis(list, percentis_list) == expected


@pytest.mark.parametrize('list, expected', [
    ([8, 10, 4, 8, 6, 10, 8], 1.5510204081632648)
])
def test_desvio_medio_absoluto(list: list, expected: list):
    """Testa a função desvio médio absoluto"""
    assert desvio_medio_absoluto(list) == expected


@pytest.mark.parametrize('list, expected', [
    ([8, 10, 4, 8, 6, 10, 8], 2.9652)
])
def test_desvio_absoluto_mediano(list: list, expected: list):
    """Testa a função desvio absoluto mediano"""
    assert desvio_absoluto_mediano(list) == expected


@pytest.mark.parametrize('list, expected', [
    ([8, 10, 4, 8, 6, 10, 8], 4.57142857142857)
])
def test_variancia(list: list, expected: list):
    """Testa a função variancia"""
    assert variancia(list) == expected


@pytest.mark.parametrize('list, expected', [
    ([8, 10, 4, 8, 6, 10, 8], 2.1380899352993947)
])
def test_desvio_padrao(list: list, expected: list):
    """Testa a função desvio padrão"""
    assert desvio_padrao(list) == expected


# Parte II: Probabilidade e Amostragem
