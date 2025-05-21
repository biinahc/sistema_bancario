import winsound
from datetime import datetime

usuarios = []
contas = []

AGENCIA = "0001"
LIMITE_SAQUES = 3
LIMITE_TRANSACOES = 10

def tocar_sucesso():
    winsound.Beep(1000, 300)
    winsound.Beep(1200, 300)

def tocar_erro():
    winsound.Beep(400, 500)

def tocar_despedida():
    winsound.Beep(1000, 500)
    winsound.Beep(1200, 500)

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("⚠️ Saldo insuficiente.")
        tocar_erro()
    elif valor > limite:
        print("🚫 O valor do saque excede o limite.")
        tocar_erro()
    elif numero_saques >= limite_saques:
        print("❌ Limite de saques diários atingido.")
        tocar_erro()
    elif valor <= 0:
        print("❌ Valor inválido.")
        tocar_erro()
    else:
        saldo -= valor
        extrato += f"🔻 Saque: R$ {valor:.2f} | {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        numero_saques += 1
        tocar_sucesso()
        print(f"💸 Saque de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print("❌ Valor inválido.")
        tocar_erro()
    else:
        saldo += valor
        extrato += f"✅ Depósito: R$ {valor:.2f} | {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        tocar_sucesso()
        print(f"✨ Depósito de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n📜 === EXTRATO BANCÁRIO SC === 📜")
    print(extrato if extrato else "🚫 Nenhuma movimentação registrada.")
    print(f"\n💰 Saldo atual: R$ {saldo:.2f}")
    print("🔷============================🔷\n")

def criar_usuario(usuarios):
    cpf = input("🔎 Informe o CPF (somente números): ").strip()
    cpf = ''.join(filter(str.isdigit, cpf))

    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("⚠️ CPF já cadastrado, faça Login!")
        tocar_erro()
        return

    nome = input("👤 Nome completo: ")
    nascimento = input("📅 Data de nascimento (dd/mm/aaaa): ")
    endereco = input("🏠 Endereço (logradouro, nro - bairro - cidade/UF): ")

    usuarios.append({
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("✅ Usuário criado com sucesso!")
    tocar_sucesso()

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("🔎 Informe o CPF do usuário: ").strip()
    cpf = ''.join(filter(str.isdigit, cpf))
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)

    if not usuario:
        print("🚫 Usuário não encontrado.")
        tocar_erro()
        return None

    print(f"✅ Conta criada com sucesso! Agência: {agencia}, Conta: {numero_conta}")
    tocar_sucesso()
    return {"agencia": agencia, "numero": numero_conta, "usuario": usuario}

def login(usuarios):
    print("\n🔐 LOGIN NO SISTEMA")
    cpf = input("Informe seu CPF (somente números): ").strip()
    cpf = ''.join(filter(str.isdigit, cpf))

    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    if usuario:
        print(f"\n👋 Bem-vindo(a) ao banco SC, {usuario['nome']}!")
        tocar_sucesso()
        return usuario
    else:
        print("\n❌ CPF não cadastrado. Por favor, crie um usuário.")
        tocar_erro()
        return None


saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
numero_transacoes = 0
numero_contas = 1


usuario_logado = None
while not usuario_logado:
    print("""
🟢 BEM-VINDO AO BANCO VIRTUAL SC, VOCÊ JÁ PODE ACESSAR SUA CONTA! 🟢

[1] 🔐 Fazer login com CPF
[2] 📝 Criar novo usuário
[3] ❌ Sair
""")
    escolha = input("Escolha uma opção: ").strip()

    if escolha == "1":
        usuario_logado = login(usuarios)
    elif escolha == "2":
        criar_usuario(usuarios)
    elif escolha == "3":
        print("👋 Saindo do sistema. Até logo!")
        tocar_despedida()
        exit()
    else:
        print("❌ Opção inválida!")
        tocar_erro()


menu = """
💳 MENU DO BANCO SC

[d] 💰 Depositar
[s] 💸 Sacar
[e] 📜 Extrato
[u] 👤 Criar Usuário
[c] 🏦 Criar Conta Corrente
[q] ❌ Sair

=> """

while True:
    opcao = input(menu).strip().lower()

    if opcao in ["d", "s"] and numero_transacoes >= LIMITE_TRANSACOES:
        print("❌ Limite de transações diárias atingido.")
        tocar_erro()
        continue

    if opcao == "d":
        try:
            valor = float(input("🟢 Valor do depósito: R$ "))
        except ValueError:
            print("❌ Digite um valor válido.")
            tocar_erro()
            continue
        saldo, extrato = depositar(saldo, valor, extrato)
        numero_transacoes += 1

    elif opcao == "s":
        try:
            valor = float(input("🔴 Valor do saque: R$ "))
        except ValueError:
            print("❌ Digite um valor válido.")
            tocar_erro()
            continue
        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )
        numero_transacoes += 1

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "u":
        criar_usuario(usuarios)

    elif opcao == "c":
        conta = criar_conta(AGENCIA, numero_contas, usuarios)
        if conta:
            contas.append(conta)
            numero_contas += 1

    elif opcao == "q":
        print("\n👋 Obrigado por utilizar nosso sistema bancário SC! Até a próxima, volte logo !")
        tocar_despedida()
        break

    else:
        print("❌ Opção inválida.")
        tocar_erro()
