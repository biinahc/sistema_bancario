# 💻 Simulador de Banco em Python

Este é um simulador de banco desenvolvido em Python com o objetivo de aprendizado e prática de conceitos como modularização, estrutura de dados, controle de fluxo e interação por linha de comando. O projeto foi iniciado por [Biinahc](https://github.com/biinahc) e expandido com novas funcionalidades, incluindo autenticação por CPF, contas bancárias, limite de operações, sons de feedback e uma interface mais intuitiva.

---

## 🚀 Funcionalidades

- **🔐 Login com CPF:** Autenticação baseada em CPF. O usuário deve estar previamente cadastrado para acessar o sistema.
- **📝 Cadastro de Usuário:** Possibilita o registro de novos usuários com:
  - Nome completo
  - Data de nascimento
  - CPF (somente números)
  - Endereço (logradouro, número - bairro - cidade/UF)
- **🏦 Cadastro de Conta Corrente:**
  - Cada conta possui número sequencial e agência fixa `0001`
  - Uma conta é vinculada a um único usuário
  - Um usuário pode ter várias contas
- **💰 Depósito:**
  - Aceita apenas valores positivos
  - Atualiza saldo e registra extrato
- **💸 Saque:**
  - Restrições:
    - Valor não pode exceder o saldo
    - Valor máximo por saque: R$ 500,00
    - Máximo de 3 saques por dia
- **📜 Extrato:**
  - Exibe histórico de transações (depósitos e saques)
  - Mostra saldo atual
- **🎧 Feedback Sonoro:**
  - Sucesso: som agudo
  - Erro: som grave
  - Saída: combinação de tons
- **🖥️ Interface CLI (Linha de Comando):**
  - Menu interativo com opções diretas
  - Navegação simples e orientada

---

## 🧰 Pré-requisitos

- **Python 3.6+**
- **Som no sistema (Windows recomendado)**: Utiliza `winsound` (exclusivo do Windows, opcional)

---

## 📦 Como Executar

1. **Clone o repositório:**

```bash
git clone https://github.com/biinahc/Sistema-Bancario.git
cd Sistema-Bancario

📢 Observações
O sistema não salva dados em arquivos ou banco de dados. Tudo é armazenado na memória durante a execução.

A biblioteca winsound funciona apenas no Windows. Em outros sistemas, os sons não serão emitidos, mas o programa continuará funcionando normalmente.

## Autor

[Biinahc](https://github.com/biinahc)

---