from conta import Conta


class Banco:
    def __init__(self):
        self.contas = {}
        self.proximo_numero = 1

    def criar_conta(self, titular: str):
        if not titular.strip():
            raise ValueError(
                "O nome do titular não pode estar vazio."
            )

        conta = Conta(
            self.proximo_numero,
            titular
        )

        self.contas[self.proximo_numero] = conta

        self.proximo_numero += 1

        return conta

    def obter_conta(self, numero: int):
        if numero not in self.contas:
            raise ValueError(
                "Conta não encontrada."
            )

        return self.contas[numero]

    def listar_contas(self):
        return list(self.contas.values())