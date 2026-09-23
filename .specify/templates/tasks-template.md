# Checklist de Tarefas

## Status do Projeto

- [ ] Projeto iniciado
- [ ] Desenvolvimento concluído
- [ ] Testes concluídos
- [ ] Projeto finalizado

---

# Fase 1 - Estrutura Inicial

## Estrutura de Pastas

- [ ] Criar pasta src
- [ ] Criar pasta tests
- [ ] Criar pasta docs

## Arquivos Base

- [ ] Criar conta.py
- [ ] Criar banco.py
- [ ] Criar main.py
- [ ] Criar README.md
- [ ] Criar requirements.txt

---

# Fase 2 - Classe Conta

## Atributos

- [ ] Criar atributo numero
- [ ] Criar atributo titular
- [ ] Criar atributo saldo
- [ ] Criar atributo extrato

## Construtor

- [ ] Criar método __init__

## Depósito

- [ ] Criar método depositar()
- [ ] Validar valor positivo
- [ ] Atualizar saldo
- [ ] Registrar operação no extrato

## Saque

- [ ] Criar método sacar()
- [ ] Validar valor positivo
- [ ] Verificar saldo suficiente
- [ ] Atualizar saldo
- [ ] Registrar operação no extrato

## Consultas

- [ ] Criar método mostrar_saldo()
- [ ] Criar método mostrar_extrato()

---

# Fase 3 - Classe Banco

## Estrutura Interna

- [ ] Criar dicionário de contas
- [ ] Criar contador automático de contas

## Funcionalidades

- [ ] Criar método criar_conta()
- [ ] Criar método obter_conta()
- [ ] Criar método listar_contas()

## Validações

- [ ] Validar nome do titular
- [ ] Validar conta existente

---

# Fase 4 - Interface de Terminal

## Menu

- [ ] Exibir menu principal
- [ ] Implementar loop principal

## Opções

- [ ] Opção 1 - Criar conta
- [ ] Opção 2 - Depositar
- [ ] Opção 3 - Sacar
- [ ] Opção 4 - Consultar saldo
- [ ] Opção 5 - Consultar extrato
- [ ] Opção 6 - Listar contas
- [ ] Opção 0 - Encerrar sistema

---

# Fase 5 - Tratamento de Erros

## Valores Inválidos

- [ ] Impedir depósitos negativos
- [ ] Impedir saques negativos
- [ ] Impedir depósitos iguais a zero
- [ ] Impedir saques iguais a zero

## Operações Bancárias

- [ ] Impedir saque sem saldo
- [ ] Impedir acesso a conta inexistente

## Entrada do Usuário

- [ ] Tratar letras em campos numéricos
- [ ] Tratar entradas vazias

---

# Fase 6 - Qualidade do Código

## Padronização

- [ ] Aplicar PEP-8
- [ ] Utilizar type hints
- [ ] Organizar imports

## Dinheiro

- [ ] Utilizar Decimal para valores monetários

## Documentação

- [ ] Adicionar comentários importantes
- [ ] Atualizar README

---

# Fase 7 - Testes Automatizados

## Testes Conta

- [ ] Testar criação da conta
- [ ] Testar depósito válido
- [ ] Testar depósito inválido
- [ ] Testar saque válido
- [ ] Testar saque inválido

## Testes Banco

- [ ] Testar criação de conta
- [ ] Testar busca de conta
- [ ] Testar conta inexistente

## Cobertura

- [ ] Todos os testes passam

---

# Fase 8 - Melhorias Futuras

## Persistência

- [ ] Salvar contas em SQLite
- [ ] Salvar extratos em SQLite

## Segurança

- [ ] Criar senha para contas
- [ ] Implementar autenticação

## Funcionalidades Extras

- [ ] Transferência entre contas
- [ ] Histórico com data e hora
- [ ] Relatório financeiro

---

# Critérios de Conclusão

- [ ] Criar contas
- [ ] Realizar depósitos
- [ ] Realizar saques
- [ ] Consultar saldo
- [ ] Consultar extrato
- [ ] Listar contas
- [ ] Tratar erros
- [ ] Executar testes com sucesso
- [ ] Utilizar Decimal
- [ ] Entregar versão 1.0
