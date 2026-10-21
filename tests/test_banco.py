import pytest

from banco import Banco
from conta import Conta


@pytest.fixture
def banco():
    return Banco()


def test_criar_conta_numera_sequencialmente(banco):
    c1 = banco.criar_conta("Ana")
    c2 = banco.criar_conta("Bia")
    assert isinstance(c1, Conta)
    assert (c1.numero, c2.numero) == (1, 2)
    assert c1.titular == "Ana"


@pytest.mark.parametrize("nome", ["", "   "])
def test_criar_conta_titular_vazio(banco, nome):
    with pytest.raises(ValueError, match="titular"):
        banco.criar_conta(nome)
    assert banco.listar_contas() == []
    assert banco.proximo_numero == 1


def test_obter_conta_existente(banco):
    conta = banco.criar_conta("Ana")
    assert banco.obter_conta(1) is conta


def test_obter_conta_inexistente(banco):
    with pytest.raises(ValueError, match="não encontrada"):
        banco.obter_conta(99)


def test_listar_contas(banco):
    assert banco.listar_contas() == []
    c1 = banco.criar_conta("Ana")
    c2 = banco.criar_conta("Bia")
    assert banco.listar_contas() == [c1, c2]


def test_contas_sao_independentes(banco):
    from decimal import Decimal

    c1 = banco.criar_conta("Ana")
    c2 = banco.criar_conta("Bia")
    c1.depositar(Decimal("10"))
    assert c2.mostrar_saldo() == Decimal("0.00")
