import pytest
from estatistica import media


@pytest.mark.parametrize('input, expected', [
    ([1, 2, 3, 4, 5], 3),
    ([1, 8, 14, -7], 4),
    ([-3, -7, -5], -5),
    ([], 0)
])
def test_media(input: list, expected: bool):
    """Testa medias de conjuntos de dados"""

    assert media(input) == expected
