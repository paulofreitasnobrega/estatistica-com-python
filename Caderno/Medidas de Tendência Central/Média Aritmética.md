# Média Aritmética
A média aritmética, ou simplesmente média, é a medida de tendência central mais conhecida e utilizada para resumir a informação contida em um conjunto de dados. Trata-se da soma de todos os valores, dividido pelo número de elementos.

Em uma amostra da população utiliza-se o símbolo ¯x  (x barra) para representar a média e n (minúsculo) para se referir ao número total de elementos. Tratando-se da população, utiliza-se os símbolos μ e N (maiúsculo) respectivamente.

Média é uma medida suscetível aos efeitos de outliers (casos extremos). Alternativas para média aritmética são: média aparada, média ponderada, etc.

```python
def media(conjunto: list) -> float:
    """
    Calcula a média de um conjunto de dados
    """

    return sum(conjunto) / len(conjunto)
```