from decimal import Decimal

import pytest

from conta import Conta


@pytest.fixture
def conta():
    return Conta(1, "Ana")


def test_conta_nova_tem_saldo_zero_e_extrato_vazio(conta):
    assert conta.numero == 1
    assert conta.titular == "Ana"
    assert conta.mostrar_saldo() == Decimal("0.00")
    assert conta.mostrar_extrato() == []


def test_depositar_aumenta_saldo_e_registra_extrato(conta):
    conta.depositar(Decimal("100.50"))
    assert conta.mostrar_saldo() == Decimal("100.50")
    assert conta.mostrar_extrato() == ["Depósito: +R$ 100.50"]


@pytest.mark.parametrize("valor", [Decimal("0"), Decimal("-10")])
def test_depositar_valor_invalido(conta, valor):
    with pytest.raises(ValueError, match="depósito"):
        conta.depositar(valor)
    assert conta.mostrar_saldo() == Decimal("0.00")
    assert conta.mostrar_extrato() == []


def test_sacar_diminui_saldo_e_registra_extrato(conta):
    conta.depositar(Decimal("100"))
    conta.sacar(Decimal("30.25"))
    assert conta.mostrar_saldo() == Decimal("69.75")
    assert conta.mostrar_extrato()[-1] == "Saque: -R$ 30.25"


def test_sacar_saldo_total(conta):
    conta.depositar(Decimal("50"))
    conta.sacar(Decimal("50"))
    assert conta.mostrar_saldo() == Decimal("0")


def test_sacar_saldo_insuficiente(conta):
    conta.depositar(Decimal("10"))
    with pytest.raises(ValueError, match="Saldo insuficiente"):
        conta.sacar(Decimal("10.01"))
    assert conta.mostrar_saldo() == Decimal("10")
    assert len(conta.mostrar_extrato()) == 1


@pytest.mark.parametrize("valor", [Decimal("0"), Decimal("-5")])
def test_sacar_valor_invalido(conta, valor):
    conta.depositar(Decimal("10"))
    with pytest.raises(ValueError, match="saque"):
        conta.sacar(valor)
    assert conta.mostrar_saldo() == Decimal("10")


def test_extrato_mantem_ordem_das_operacoes(conta):
    conta.depositar(Decimal("100"))
    conta.sacar(Decimal("40"))
    conta.depositar(Decimal("5"))
    assert conta.mostrar_extrato() == [
        "Depósito: +R$ 100.00",
        "Saque: -R$ 40.00",
        "Depósito: +R$ 5.00",
    ]
