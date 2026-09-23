from decimal import Decimal


class Conta:
    def __init__(self, numero: int, titular: str):
        self.numero = numero
        self.titular = titular
        self.saldo = Decimal("0.00")
        self.extrato = []

    def depositar(self, valor: Decimal):
        if valor <= 0:
            raise ValueError(
                "O valor do depósito deve ser maior que zero."
            )

        self.saldo += valor

        self.extrato.append(
            f"Depósito: +R$ {valor:.2f}"
        )

    def sacar(self, valor: Decimal):
        if valor <= 0:
            raise ValueError(
                "O valor do saque deve ser maior que zero."
            )

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
    
    
    