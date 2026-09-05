import pytest

from ledger import Conta, SaldoInsuficienteError, TransacaoInvalidaError


def test_deposito_e_saque_atualizam_saldo():
    conta = Conta()
    conta.depositar(1000)
    conta.sacar(250)

    assert conta.saldo == 750
    assert len(conta.transacoes) == 2


def test_nao_permite_saque_com_saldo_negativo():
    conta = Conta()
    conta.depositar(100)

    with pytest.raises(SaldoInsuficienteError):
        conta.sacar(150)


def test_estorno_recalcula_saldo_imediatamente():
    conta = Conta()
    deposito = conta.depositar(1000)
    saque = conta.sacar(300)

    conta.estornar(saque["id"])

    assert conta.saldo == 1000
    assert saque["status"] == "ESTORNADO"
    assert deposito["status"] == "CONCLUIDO"


def test_nao_permite_estornar_duas_vezes():
    conta = Conta()
    deposito = conta.depositar(200)
    conta.estornar(deposito["id"])

    with pytest.raises(TransacaoInvalidaError):
        conta.estornar(deposito["id"])
