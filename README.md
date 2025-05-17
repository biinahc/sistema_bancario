# Simulador de Banco em Python

Este é um simples simulador de banco desenvolvido em Python para fins de aprendizado e demonstração por [Biinahc](https://github.com/biinahc). Ele oferece funcionalidades básicas como depósito, saque e visualização de extrato, além de implementar um sistema de autenticação por senha, limite de saques diários e limite por saque.

## Funcionalidades

* **Autenticação:** Protege o acesso ao sistema solicitando uma senha ao iniciar. A senha padrão é `1234`.
* **Depósito:** Permite aos usuários adicionar valores positivos ao saldo da conta.
* **Saque:** Permite aos usuários retirar valores do saldo, com as seguintes restrições:

    * O valor do saque não pode exceder o saldo atual.
    * O valor máximo por saque é de R$ 500.00.
    * É permitido um máximo de 3 saques por dia.
* **Extrato:** Exibe um histórico de todas as operações de depósito e saque realizadas, juntamente com o saldo atual da conta.
* **Interface de Menu:** Uma interface de linha de comando simples e intuitiva, baseada em texto, para facilitar a interação do usuário.
* **Feedback Sonoro:** Utiliza a biblioteca `winsound` (disponível principalmente em sistemas Windows) para emitir sons que indicam sucesso nas operações (depósito e saque), erros (senha incorreta, valores inválidos, limites excedidos) e ao sair do sistema.

## Como Executar

1.  **Pré-requisitos:** Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo em \[https://www.python.org/downloads/](https://www.python.org/downloads/).
2.  **Download:** Faça o download deste repositório para o seu computador utilizando o Git:

    ```bash
    git clone [https://github.com/biinahc/Sistema-Bancario.git](https://github.com/biinahc/Sistema-Bancario.git)
    ```

    Ou, se preferir, baixe o arquivo `.py` diretamente da página do repositório.
3.  **Execução:** Abra um terminal ou prompt de comando, navegue até o diretório onde o arquivo `seu_script.py` (substitua pelo nome real do seu arquivo Python) está salvo e execute o seguinte comando:

    ```bash
    python seu_script.py
    ```

## Utilização

Ao executar o script, siga as instruções na tela:

1.  **Autenticação:** Digite a senha quando solicitado. A senha padrão é `1234`.
2.  **Menu Principal:** Após a autenticação bem-sucedida, um menu com as seguintes opções será exibido:

    * `[d] 💰 Depositar`: Digite `d` para realizar um depósito e siga as instruções para inserir o valor.
    * `[s] 💸 Sacar`: Digite `s` para realizar um saque e siga as instruções para inserir o valor. O sistema verificará os limites e o saldo.
    * `[e] 📜 Extrato`: Digite `e` para visualizar o extrato das operações e o saldo atual.
    * `[q] ❌ Sair`: Digite `q` para encerrar o programa.

## Observações

* O saldo inicial da conta é R$ 0.00.
* O limite máximo para cada saque é de R$ 500.00.
* O número máximo de saques permitidos por dia é 3.
* A funcionalidade de feedback sonoro pode não funcionar em sistemas operacionais diferentes do Windows, pois utiliza a biblioteca `winsound`. O programa continuará funcionando normalmente sem os sons.

## Contribuição

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novas funcionalidades. Para isso, siga os seguintes passos:

1.  Faça um fork do repositório (\[https://github.com/biinahc/Sistema-Bancario/fork](https://github.com/biinahc/Sistema-Bancario/fork)).
2.  Crie uma branch para sua modificação (`git checkout -b feature/sua-melhoria`).
3.  Faça commit das suas alterações (`git commit -am 'Adiciona alguma melhoria'`).
4.  Faça push para a branch (`git push origin feature/sua-melhoria`).
5.  Abra um Pull Request no seu repositório forked.

## Autor

[Biinahc](https://github.com/biinahc)

---
