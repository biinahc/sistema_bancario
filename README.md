# 💻 Simulador de Banco em Python

<<<<<<< HEAD
Este é um simulador bancário desenvolvido em Python para fins de aprendizado e demonstração por **Biinahc**. O sistema oferece funcionalidades como depósito, saque, visualização de extrato e autenticação por senha. Além disso, ele agora conta com melhorias no controle de transações.

## 🏦 Funcionalidades

- **Autenticação**: Protege o acesso ao sistema solicitando uma senha ao iniciar. A senha padrão é `1234`.
- **Depósito**: Permite aos usuários adicionar valores positivos ao saldo da conta.
- **Saque**: Permite aos usuários retirar valores do saldo, respeitando as seguintes restrições:
  - O valor do saque não pode exceder o saldo atual.
  - O valor máximo por saque é de R$ 500,00.
  - É permitido um máximo de 3 saques por dia.
- **Extrato**: Exibe um histórico detalhado de todas as transações realizadas, incluindo a **data e hora** de cada movimentação.
- **Limite de Transações Diárias**: Agora, há um limite de **10 transações diárias** (soma de depósitos e saques). Ao atingir esse limite, nenhuma nova transação será permitida.
- **Interface de Menu**: Uma interface de linha de comando simples e intuitiva para facilitar a interação do usuário.
- **Feedback Sonoro**: Utiliza a biblioteca `winsound` (disponível em sistemas Windows) para emitir sons indicando sucesso ou erro nas operações.

## 🚀 Como Executar

### 📌 Pré-requisitos

Certifique-se de ter o Python instalado no seu sistema. Você pode baixá-lo [aqui](https://www.python.org/downloads/).

## 🔽 Download do Repositório

Baixe o repositório para o seu computador utilizando Git:

```bash
git clone https://github.com/biinahc/Sistema-Bancario.git

Ou baixe o arquivo .py diretamente da página do repositório.
▶️ Execução
Abra um terminal ou prompt de comando, navegue até o diretório do script e execute:
python seu_script.py


📜 Utilização
Após a autenticação, você terá acesso ao seguinte menu de opções:
- [d] 💰 Depositar: Adicionar saldo à conta.
- [s] 💸 Sacar: Retirar valores do saldo, respeitando os limites diários.
- [e] 📜 Extrato: Exibir todas as transações, agora com data e hora.
- [q] ❌ Sair: Encerrar o programa.


⚠️ Importante: O sistema agora limita as transações diárias a 10 operações (entre depósitos e saques). Caso esse número seja atingido, não será possível realizar novas transações no dia.
❗ Observações
- O saldo inicial da conta é R$ 0,00.
- O limite máximo por saque é R$ 500,00.
- Agora todas as transações são registradas com data e hora no extrato.
- O limite diário de transações é 10 operações (soma de depósitos e saques).
- A funcionalidade de feedback sonoro pode não funcionar em sistemas que não sejam Windows, pois depende da biblioteca winsound.

🤝 Contribuição
Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novas funcionalidades! Para contribuir:
- Faça um fork do repositório: Sistema Bancário.
- Crie uma branch para sua modificação:
git checkout -b feature/sua-melhoria
- Faça commit das suas alterações:
git commit -am "Adiciona nova funcionalidade"
- Envie as alterações para sua branch:
git push origin feature/sua-melhoria
- Abra um Pull Request no repositório principal.

👩‍💻 Autor
Projeto desenvolvido por Biinahc.



=======
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

1. **Execute o script:**

python banco.py

📢 Observações
O sistema não salva dados em arquivos ou banco de dados. Tudo é armazenado na memória durante a execução.

A biblioteca winsound funciona apenas no Windows. Em outros sistemas, os sons não serão emitidos, mas o programa continuará funcionando normalmente.

 ## 👤 Autora

[Biinahc](https://github.com/biinahc)
>>>>>>> 33778ff (Adicionando sistema bancário modularizado)
