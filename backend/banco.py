import os
import winsound


senha_correta = "1234"


def tocar_erro():
    winsound.Beep(400, 500)  


def tocar_despedida():
    winsound.Beep(1000, 500)  
    winsound.Beep(1200, 500)


senha = input("🔑 Digite sua senha para acessar o banco: ")
if senha != senha_correta:
    print("❌ Senha incorreta! Acesso negado.")
    tocar_erro()
    exit()


saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

menu = """
💳 MENU DO BANCO

[d] 💰 Depositar
[s] 💸 Sacar
[e] 📜 Extrato
[q] ❌ Sair

=> """

while True:
    opcao = input(menu).strip().lower()

    if opcao == "d":
        try:
            valor = float(input("🟢 Informe o valor do depósito: R$ "))
        except ValueError:
            print("❌ Erro: Digite um valor válido.")
            tocar_erro()
            continue

        if valor > 0:
            saldo += valor
            extrato += f"✅ Depósito: R$ {valor:.2f}\n"
            winsound.Beep(1000, 500)
            print(f"\n✨ Depósito realizado com sucesso! Novo saldo: R$ {saldo:.2f} ✨\n")
        else:
            print("\n❌ Operação falhou! O valor informado é inválido.\n")
            tocar_erro()

    elif opcao == "s":
        try:
            valor = float(input("🔴 Informe o valor do saque: R$ "))
        except ValueError:
            print("\n❌ Erro: Digite um valor válido.\n")
            tocar_erro()
            continue

        if valor > saldo:
            print("\n⚠️ Operação falhou! Você não tem saldo suficiente.\n")
            tocar_erro()
        elif valor > limite:
            print("\n🚫 Operação falhou! O valor do saque excede o limite permitido.\n")
            tocar_erro()
        elif numero_saques >= LIMITE_SAQUES:
            print("\n❌ Operação falhou! Número máximo de saques diários atingido.\n")
            tocar_erro()
        elif valor > 0:
            saldo -= valor
            extrato += f"🔻 Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            winsound.Beep(800, 500)
            print(f"\n💸 Saque realizado com sucesso! Novo saldo: R$ {saldo:.2f} 🏦\n")
        else:
            print("\n❌ Operação falhou! O valor informado é inválido.\n")
            tocar_erro()

    elif opcao == "e":
        print("\n📜 === EXTRATO BANCÁRIO === 📜")
        if not extrato:
            print("\n🚫 Nenhuma movimentação registrada.\n")
        else:
            print(extrato)
        print(f"\n💰 Saldo atual: R$ {saldo:.2f}")
        print("🔷============================🔷\n")

    elif opcao == "q":
        print("\n👋 Obrigado por utilizar nosso sistema bancário! Até a próxima! 🏦\n")
        tocar_despedida()
        break

    else:
        print("\n❌ Operação inválida! Por favor, selecione uma opção válida.\n")
        tocar_erro()