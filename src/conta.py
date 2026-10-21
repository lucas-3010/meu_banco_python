from decimal import Decimal, ROUND_HALF_UP

CENTAVOS = Decimal("0.01")


def normalizar_valor(valor, operacao: str) -> Decimal:
    if isinstance(valor, bool) or not isinstance(valor, Decimal):
        raise ValueError(
            f"O valor do {operacao} deve ser um Decimal."
        )

    if not valor.is_finite():
        raise ValueError(
            f"O valor do {operacao} deve ser um número finito."
        )

    valor = valor.quantize(CENTAVOS, rounding=ROUND_HALF_UP)

    if valor <= 0:
        raise ValueError(
            f"O valor do {operacao} deve ser maior que zero."
        )

    return valor


class Conta:
    def __init__(self, numero: int, titular: str):
        self.numero = numero
        self.titular = titular
        self.saldo = Decimal("0.00")
        self.extrato = []

    def depositar(self, valor: Decimal):
        valor = normalizar_valor(valor, "depósito")

        self.saldo += valor

        self.extrato.append(
            f"Depósito: +R$ {valor:.2f}"
        )

    def sacar(self, valor: Decimal):
        valor = normalizar_valor(valor, "saque")

        if valor > self.saldo:
            raise ValueError(
                "Saldo insuficiente."
            )

        self.saldo -= valor

        self.extrato.append(
            f"Saque: -R$ {valor:.2f}"
        )

    def mostrar_saldo(self):
        return self.saldo

    def mostrar_extrato(self):
        return self.extrato
