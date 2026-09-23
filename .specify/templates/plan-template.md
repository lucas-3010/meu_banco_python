# Plano de Implementação

## Projeto

Sistema Bancário em Python

---

# Objetivo

Desenvolver um sistema bancário orientado a objetos capaz de gerenciar contas, depósitos, saques, consulta de saldo e extrato.

---

# Arquitetura

## Estrutura de Pastas

```text
meu_banco_python/
│
├── src/
│   ├── banco.py
│   ├── conta.py
│   └── main.py
│
├── tests/
│   ├── test_conta.py
│   └── test_banco.py
│
├── docs/
│
├── requirements.txt
│
└── README.md
```

---

# Classes Principais

## Classe Conta

Responsabilidades:

- Armazenar informações da conta
- Realizar depósitos
- Realizar saques
- Gerenciar extrato

Atributos:

```python
numero
titular
saldo
extrato
```

Métodos:

```python
depositar()
sacar()
mostrar_saldo()
mostrar_extrato()
```

---

## Classe Banco

Responsabilidades:

- Gerenciar contas
- Criar contas
- Localizar contas

Atributos:

```python
contas
proximo_numero
```

Métodos:

```python
criar_conta()
obter_conta()
listar_contas()
```

---

# Fase 1 - Estrutura Inicial

Objetivo:

Criar a base do projeto.

Tarefas:

- Criar pasta src
- Criar pasta tests
- Criar arquivo conta.py
- Criar arquivo banco.py
- Criar arquivo main.py

Critério de Conclusão:

Projeto compilando sem erros.

---

# Fase 2 - Classe Conta

Objetivo:

Implementar a entidade principal do sistema.

Tarefas:

- Criar construtor
- Criar saldo inicial
- Criar extrato
- Criar método depositar
- Criar método sacar

Critério de Conclusão:

Conta capaz de realizar operações básicas.

---

# Fase 3 - Classe Banco

Objetivo:

Gerenciar múltiplas contas.

Tarefas:

- Criar armazenamento das contas
- Gerar números automáticos
- Criar contas
- Buscar contas

Critério de Conclusão:

Sistema capaz de controlar várias contas.

---

# Fase 4 - Interface de Terminal

Objetivo:

Permitir interação com o usuário.

Menu:

```text
1 - Criar conta
2 - Depositar
3 - Sacar
4 - Ver saldo
5 - Ver extrato
6 - Listar contas
0 - Sair
```

Tarefas:

- Criar menu principal
- Ler opções
- Chamar métodos corretos

Critério de Conclusão:

Usuário consegue utilizar o sistema inteiro pelo terminal.

---

# Fase 5 - Validações

Objetivo:

Evitar erros de utilização.

Validações:

- Conta inexistente
- Valor negativo
- Valor zero
- Saldo insuficiente
- Nome vazio

Critério de Conclusão:

Sistema não quebra com entradas inválidas.

---

# Fase 6 - Persistência (Versão 2)

Objetivo:

Salvar dados permanentemente.

Tecnologia:

SQLite

Funcionalidades:

- Salvar contas
- Carregar contas
- Salvar movimentações

Critério de Conclusão:

Dados mantidos após fechar o programa.

---

# Fase 7 - Testes Automatizados

Objetivo:

Garantir qualidade.

Ferramenta:

pytest

Testes:

- Criar conta
- Depositar
- Sacar
- Saldo insuficiente
- Valor inválido

Critério de Conclusão:

100% das funcionalidades principais testadas.

---

# Riscos

## Risco 01

Uso incorreto de float para dinheiro.

Mitigação:

Utilizar Decimal.

---

## Risco 02

Perda de dados ao fechar o programa.

Mitigação:

Implementar SQLite.

---

# Definição de Pronto (Definition of Done)

O projeto será considerado concluído quando:

✅ Criar contas

✅ Depositar valores

✅ Sacar valores

✅ Consultar saldo

✅ Consultar extrato

✅ Listar contas

✅ Possuir validações

✅ Possuir testes automatizados

✅ Utilizar Decimal

✅ Código seguindo PEP-8
``