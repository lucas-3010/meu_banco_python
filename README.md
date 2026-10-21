# Meu Banco Python

Sistema bancário simples de linha de comando: criar contas, depositar, sacar,
consultar saldo e extrato.

## Estrutura

- `src/conta.py`: classe `Conta` (saldo, extrato, validação de valores).
- `src/banco.py`: classe `Banco` (criação e busca de contas).
- `src/main.py`: menu interativo.

## Como executar

```bash
python src/main.py
```

Requer Python 3.8 ou superior. Valores aceitam vírgula ou ponto
(`10,50`) e são arredondados para 2 casas decimais.

## Regras de validação

- Depósitos e saques devem ser maiores que zero (após o arredondamento).
- Valores não numéricos, `NaN` e `Infinity` são rejeitados.
- Saques acima do saldo são recusados com "Saldo insuficiente."
