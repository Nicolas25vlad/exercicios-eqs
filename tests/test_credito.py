import pytest

from credito import calcular_limite


@pytest.mark.parametrize(
    "renda,restricao,score,esperado",
    [
        (1400, False, 900, 0.0),
        (5000, True, 900, 0.0),
        (1500, False, 700, 450.0),
        (3000, False, 800, 900.0),
        (3000, False, 801, 1350.0),
    ],
)
def test_calculo_de_limite(renda, restricao, score, esperado):
    assert calcular_limite(renda, restricao, score) == esperado
