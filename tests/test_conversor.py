from unittest.mock import Mock

import pytest

from conversor import ConversorMoedas, ServicoCotacaoIndisponivelError


def test_converte_moeda_com_spread_de_1_5_porcento():
    api = Mock()
    api.obter_taxa.return_value = 5.0
    conversor = ConversorMoedas(api)

    resultado = conversor.converter("USD", "BRL", 100)

    assert resultado == 507.50
    api.obter_taxa.assert_called_once_with("USD", "BRL")


def test_lanca_erro_quando_api_esta_indisponivel():
    api = Mock()
    api.obter_taxa.side_effect = ConnectionError("API fora do ar")
    conversor = ConversorMoedas(api)

    with pytest.raises(ServicoCotacaoIndisponivelError):
        conversor.converter("USD", "BRL", 100)
