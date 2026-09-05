import pytest

from pix import ChavePixInvalidaError, identificar_chave_pix


def test_identifica_cpf_valido():
    assert identificar_chave_pix("52998224725") == "CPF"


def test_identifica_email_valido():
    assert identificar_chave_pix("aluno@escola.com") == "EMAIL"


def test_identifica_telefone_valido():
    assert identificar_chave_pix("+5511999999999") == "TELEFONE"


def test_identifica_evp_valida():
    assert identificar_chave_pix("550e8400-e29b-41d4-a716-446655440000") == "EVP"


@pytest.mark.parametrize(
    "chave",
    [
        "12345678901",
        "email-invalido",
        "+5511999",
        "550e8400-e29b-11d4-a716-446655440000",
    ],
)
def test_rejeita_chaves_invalidas(chave):
    with pytest.raises(ChavePixInvalidaError):
        identificar_chave_pix(chave)
