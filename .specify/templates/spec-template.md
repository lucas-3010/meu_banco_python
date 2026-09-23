# Especificação do Sistema Bancário

## Visão Geral

Desenvolver um sistema bancário em Python para gerenciamento de contas correntes através do terminal.

O sistema deve permitir que usuários criem contas, realizem operações financeiras e consultem informações da conta com segurança.

---

# Objetivos

- Aplicar Programação Orientada a Objetos (POO)
- Praticar validação de dados
- Utilizar tratamento de exceções
- Simular operações bancárias reais
- Seguir boas práticas de desenvolvimento

---

# Requisitos Funcionais

## RF01 - Criar Conta

O sistema deve permitir a criação de uma nova conta bancária.

Dados necessários:

- Nome do titular

Resultado esperado:

- Número da conta gerado automaticamente
- Saldo inicial igual a R$ 0,00

---

## RF02 - Depositar Dinheiro

O usuário deve conseguir depositar valores positivos.

Critérios:

- Valor maior que zero
- Atualização do saldo
- Registro no extrato

---

## RF03 - Sacar Dinheiro

O usuário deve conseguir sacar valores da conta.

Critérios:

- Valor maior que zero
- Saldo suficiente
- Registro no extrato

---

## RF04 - Consultar Saldo

O usuário deve visualizar o saldo atual da conta.

Informações exibidas:

- Número da conta
- Nome do titular
- Saldo

---

## RF05 - Consultar Extrato

O usuário deve visualizar todas as movimentações.

Informações:

- Depósitos
- Saques
- Data/Hora (versão futura)

---

## RF06 - Listar Contas

O sistema deve exibir todas as contas cadastradas.

Informações:

- Número da conta
- Nome do titular
- Saldo atual

---

# Requisitos Não Funcionais

## RNF01 - Linguagem

Python 3.13 ou superior.

---

## RNF02 - Qualidade

Código deve seguir o padrão PEP-8.

---

## RNF03 - Arquitetura

Utilizar Programação Orientada a Objetos.

---

## RNF04 - Tratamento de Erros

O sistema deve impedir:

- Valores negativos
- Saques maiores que o saldo
- Contas inexistentes
- Dados inválidos

---

## RNF05 - Precisão Monetária

Todos os valores financeiros devem utilizar Decimal.

---

# Regras de Negócio

## RN01

Uma conta deve possuir número único.

---

## RN02

Não é permitido depósito de valores menores ou iguais a zero.

---

## RN03

Não é permitido saque de valores menores ou iguais a zero.

---

## RN04

Não é permitido realizar saques maiores que o saldo disponível.

---

## RN05

Toda movimentação deve ser registrada no extrato.

---

# Casos de Uso

## Caso de Uso 01 - Criar Conta

Ator:
Usuário

Fluxo:

1. Informar nome do titular
2. Sistema cria a conta
3. Sistema gera número automaticamente
4. Conta é armazenada

---

## Caso de Uso 02 - Depositar

Ator:
Usuário

Fluxo:

1. Informar conta
2. Informar valor
3. Sistema valida valor
4. Sistema atualiza saldo
5. Sistema registra operação

---

## Caso de Uso 03 - Sacar

Ator:
Usuário

Fluxo:

1. Informar conta
2. Informar valor
3. Sistema verifica saldo
4. Sistema realiza saque
5. Sistema registra operação

---

# Critérios de Aceitação

✅ Criar conta com sucesso

✅ Depositar valor válido

✅ Sacar valor válido

✅ Exibir saldo corretamente

✅ Exibir extrato corretamente

✅ Impedir saldo negativo

✅ Impedir valores inválidos

✅ Registrar movimentações no extrato

---

# Versão 2.0 (Futuro)

Funcionalidades planejadas:

- Transferência entre contas
- Persistência em SQLite
- Login por senha
- Interface gráfica
- API com FastAPI
- Testes automatizados com pytest