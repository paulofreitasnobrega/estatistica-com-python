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

$$
\mathbf{V}_1 \times \mathbf{V}_2 =  \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
\frac{\partial X}{\partial u} &  \frac{\partial Y}{\partial u} & 0 \\
\frac{\partial X}{\partial v} &  \frac{\partial Y}{\partial v} & 0 \\
\end{vmatrix}
$$

```flow
st=>start: Start
op=>operation: Your Operation
cond=>condition: Yes or No?
e=>end

st->op->cond
cond(yes)->e
cond(no)->op
```