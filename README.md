# Simulador de Banco em Python

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

### 🔽 Download do Repositório

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



