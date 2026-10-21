from decimal import Decimal, InvalidOperation

from banco import Banco


def ler_valor():
    try:
        return Decimal(
            input("Valor: ").strip().replace(",", ".")
        )
    except InvalidOperation:
        raise ValueError("Valor inválido.")


def ler_conta(banco):
    try:
        numero = int(input("Número da conta: "))
    except ValueError:
        raise ValueError("Número da conta inválido.")

    return banco.obter_conta(numero)


def exibir_menu():
    print("\n" + "=" * 40)
    print("      SISTEMA BANCÁRIO")
    print("=" * 40)

    print("1 - Criar conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Consultar saldo")
    print("5 - Consultar extrato")
    print("6 - Listar contas")
    print("0 - Sair")

    print("=" * 40)


def criar_conta(banco):
    titular = input("Nome do titular: ")
    conta = banco.criar_conta(titular)

    print("Conta criada com sucesso!")
    print(f"Número: {conta.numero}")


def depositar(banco):
    conta = ler_conta(banco)
    conta.depositar(ler_valor())

    print("Depósito realizado.")


def sacar(banco):
    conta = ler_conta(banco)
    conta.sacar(ler_valor())

    print("Saque realizado.")


def consultar_saldo(banco):
    conta = ler_conta(banco)

    print(f"Titular: {conta.titular}")
    print(f"Saldo: R$ {conta.saldo:.2f}")


def consultar_extrato(banco):
    conta = ler_conta(banco)

    print(f"\nExtrato de {conta.titular}")

    if not conta.extrato:
        print("Nenhuma movimentação.")
    else:
        for item in conta.extrato:
            print(item)


def listar_contas(banco):
    contas = banco.listar_contas()

    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    print("\nContas:")

    for conta in contas:
        print(f"Conta {conta.numero}")
        print(f"Titular: {conta.titular}")
        print(f"Saldo: R$ {conta.saldo:.2f}")
        print("-" * 30)


OPCOES = {
    "1": criar_conta,
    "2": depositar,
    "3": sacar,
    "4": consultar_saldo,
    "5": consultar_extrato,
    "6": listar_contas,
}


def main():
    banco = Banco()

    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Sistema encerrado.")
            break

        acao = OPCOES.get(opcao)

        if acao is None:
            print("Opção inválida.")
            continue

        try:
            acao(banco)
        except ValueError as erro:
            print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
