from decimal import Decimal, InvalidOperation

from banco import Banco


def ler_valor():
    try:
        valor = Decimal(
            input("Valor: ").replace(",", ".")
        )
        return valor

    except InvalidOperation:
        raise ValueError(
            "Valor inválido."
        )


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


def main():
    banco = Banco()

    while True:
        exibir_menu()

        opcao = input(
            "Escolha uma opção: "
        ).strip()

        try:
            if opcao == "1":
                titular = input(
                    "Nome do titular: "
                )

                conta = banco.criar_conta(
                    titular
                )

                print(
                    f"Conta criada com sucesso!"
                )

                print(
                    f"Número: {conta.numero}"
                )

            elif opcao == "2":
                numero = int(
                    input(
                        "Número da conta: "
                    )
                )

                conta = banco.obter_conta(
                    numero
                )

                valor = ler_valor()

                conta.depositar(valor)

                print(
                    "Depósito realizado."
                )

            elif opcao == "3":
                numero = int(
                    input(
                        "Número da conta: "
                    )
                )

                conta = banco.obter_conta(
                    numero
                )

                valor = ler_valor()

                conta.sacar(valor)

                print(
                    "Saque realizado."
                )

            elif opcao == "4":
                numero = int(
                    input(
                        "Número da conta: "
                    )
                )

                conta = banco.obter_conta(
                    numero
                )

                print(
                    f"Titular: {conta.titular}"
                )

                print(
                    f"Saldo: R$ {conta.saldo:.2f}"
                )

            elif opcao == "5":
                numero = int(
                    input(
                        "Número da conta: "
                    )
                )

                conta = banco.obter_conta(
                    numero
                )

                print(
                    f"\nExtrato de {conta.titular}"
                )

                if not conta.extrato:
                    print(
                        "Nenhuma movimentação."
                    )
                else:
                    for item in conta.extrato:
                        print(item)

            elif opcao == "6":
                contas = banco.listar_contas()

                if not contas:
                    print(
                        "Nenhuma conta cadastrada."
                    )
                else:
                    print("\nContas:")

                    for conta in contas:
                        print(
                            f"Conta {conta.numero}"
                        )
                        print(
                            f"Titular: {conta.titular}"
                        )
                        print(
                            f"Saldo: R$ {conta.saldo:.2f}"
                        )
                        print("-" * 30)

            elif opcao == "0":
                print(
                    "Sistema encerrado."
                )
                break

            else:
                print(
                    "Opção inválida."
                )

        except ValueError as erro:
            print(
                f"Erro: {erro}"
            )


if __name__ == "__main__":
    main()