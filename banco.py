import winsound
from datetime import datetime
from abc import ABC, abstractmethod

# --- DECORADOR MODIFICADO ---
def log_transacao(funcao):
    """
    MODIFICADO: Decorador que salva em um arquivo de log (log.txt)
    as informações de uma função chamada: data, hora, nome, argumentos e retorno.
    """
    def wrapper(*args, **kwargs):
        # 1. Captura a data e hora atuais
        timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        
        # 2. Captura o nome da função
        nome_funcao = funcao.__name__
        
        # Executa a função original para obter o resultado
        resultado = funcao(*args, **kwargs)
        
        # 3. Captura os argumentos da função (formatando para leitura)
        # Usamos repr() para ter uma representação fiel dos objetos
        args_formatados = ", ".join(repr(a) for a in args)
        kwargs_formatados = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        argumentos_completos = ", ".join(filter(None, [args_formatados, kwargs_formatados]))

        # 4. Captura o valor retornado pela função
        valor_retornado = repr(resultado)

        # Monta a string de log completa
        log_entry = (
            f"Data/Hora: {timestamp} | "
            f"Função: {nome_funcao} | "
            f"Argumentos: ({argumentos_completos}) | "
            f"Retorno: {valor_retornado}\n" # 7. Garante a nova linha
        )
        
        try:
            # 5 e 6. Abre 'log.txt' em modo de 'append' (adicionar ao final)
            with open("log.txt", "a", encoding="utf-8") as arquivo_log:
                arquivo_log.write(log_entry)
        except Exception as e:
            print(f"--- ERRO CRÍTICO AO GRAVAR LOG: {e} ---")

        return resultado
    return wrapper


# --- Efeitos Sonoros (mantidos do código original) ---

def tocar_sucesso():
    """Toca um som de sucesso."""
    # O winsound só funciona no Windows. Em outros sistemas, isso pode gerar um erro.
    # Adicionamos um try-except para evitar que o programa quebre.
    try:
        winsound.Beep(1000, 200)
        winsound.Beep(1200, 200)
    except ImportError:
        pass # Ignora o erro se a biblioteca não for encontrada

def tocar_erro():
    """Toca um som de erro."""
    try:
        winsound.Beep(400, 400)
    except ImportError:
        pass

def tocar_despedida():
    """Toca um som de despedida."""
    try:
        winsound.Beep(1000, 300)
        winsound.Beep(800, 300)
    except ImportError:
        pass

# --- Modelagem das Classes (Baseado no UML) ---

class Historico:
    """Registra as transações de uma conta."""
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        """Adiciona uma transação ao histórico."""
        timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": timestamp,
            }
        )

    def gerar_relatorio(self, tipo_transacao=None):
        """
        Gera um relatório de transações, opcionalmente filtrado por tipo.
        Usa 'yield' para retornar uma transação de cada vez.
        """
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao


class Transacao(ABC):
    """Classe abstrata para todas as transações."""
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    """Classe para transações de depósito."""
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def __repr__(self):
        return f"Deposito(valor={self.valor})"

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    """Classe para transações de saque."""
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def __repr__(self):
        return f"Saque(valor={self.valor})"

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)

class Conta:
    """Classe base para contas bancárias."""
    def __init__(self, numero, cliente):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    def __repr__(self):
        return f"<Conta(numero={self.numero}, cliente='{self.cliente.nome}')>"

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        """Realiza um saque na conta."""
        if valor <= 0:
            print("❌ Valor de saque inválido.")
            tocar_erro()
            return False
        if valor > self._saldo:
            print("⚠️ Saldo insuficiente para o saque.")
            tocar_erro()
            return False
        
        self._saldo -= valor
        print(f"💸 Saque de R$ {valor:.2f} realizado com sucesso!")
        return True

    def depositar(self, valor):
        """Realiza um depósito na conta."""
        if valor > 0:
            self._saldo += valor
            print(f"✨ Depósito de R$ {valor:.2f} realizado com sucesso!")
            return True
        
        print("❌ Valor de depósito inválido.")
        tocar_erro()
        return False

class ContaCorrente(Conta):
    """Conta corrente com limites específicos."""
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        """Sobrescreve o método sacar para incluir validações de limite."""
        saques_realizados = len(
            [transacao for transacao in self.historico.transacoes 
             if transacao["tipo"] == "Saque"]
        )

        if valor > self.limite:
            print(f"🚫 O valor do saque excede o limite de R$ {self.limite:.2f}.")
            tocar_erro()
            return False
        
        if saques_realizados >= self.limite_saques:
            print(f"❌ Limite de {self.limite_saques} saques diários atingido.")
            tocar_erro()
            return False

        # Chama o método sacar da classe pai (Conta) se todas as validações passarem
        return super().sacar(valor)
        
    def __str__(self):
        return f"Agência: {self.agencia} | C/C: {self.numero} | Titular: {self.cliente.nome}"


class Cliente:
    """Classe para representar um cliente do banco."""
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        # Adicionado para que o objeto Cliente tenha um nome para o log
        self.nome = "Cliente sem nome definido"

    def __repr__(self):
        return f"<Cliente(nome='{self.nome}')>"

    # Decorador aplicado na função que efetivamente faz o registro da transação
    @log_transacao
    def realizar_transacao(self, conta, transacao):
        """
        Inicia o processo de uma transação, agora com validação de limite diário.
        """
        hoje = datetime.now().date()
        transacoes_hoje = [
            t for t in conta.historico.transacoes
            if datetime.strptime(t['data'], '%d/%m/%Y %H:%M:%S').date() == hoje
        ]
        if len(transacoes_hoje) >= 10:
            print("\n❌ Você excedeu o número de 10 transações permitidas para hoje.")
            tocar_erro()
            return

        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        """Adiciona uma conta para o cliente."""
        self.contas.append(conta)

class PessoaFisica(Cliente):
    """Cliente do tipo Pessoa Física."""
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    def __repr__(self):
        return f"<PessoaFisica(nome='{self.nome}', cpf='{self.cpf}')>"


# --- Funções do Menu (Adaptadas para usar Classes) ---

def menu_deposito(cliente):
    """Gerencia a operação de depósito."""
    if not cliente.contas:
        print("🚫 Cliente não possui conta. Crie uma conta primeiro.")
        tocar_erro()
        return

    conta_ativa = cliente.contas[0]

    try:
        valor = float(input("🟢 Valor do depósito: R$ "))
        deposito = Deposito(valor)
        cliente.realizar_transacao(conta_ativa, deposito)
        tocar_sucesso()
    except ValueError:
        print("❌ Digite um valor numérico válido.")
        tocar_erro()


def menu_saque(cliente):
    """Gerencia a operação de saque."""
    if not cliente.contas:
        print("🚫 Cliente não possui conta. Crie uma conta primeiro.")
        tocar_erro()
        return
        
    conta_ativa = cliente.contas[0]
    
    try:
        valor = float(input("🔴 Valor do saque: R$ "))
        saque = Saque(valor)
        cliente.realizar_transacao(conta_ativa, saque)
    except ValueError:
        print("❌ Digite um valor numérico válido.")
        tocar_erro()

def menu_exibir_extrato(cliente):
    """Exibe o extrato da conta do cliente."""
    if not cliente.contas:
        print("🚫 Cliente não possui conta.")
        tocar_erro()
        return

    conta_ativa = cliente.contas[0]
    print("\n📜 === EXTRATO BANCÁRIO SC === 📜")
    
    transacoes = conta_ativa.historico.transacoes
    if not transacoes:
        print("🚫 Nenhuma movimentação registrada.")
    else:
        for transacao in transacoes:
            tipo = "🔻 Saque" if transacao['tipo'] == 'Saque' else "✅ Depósito"
            print(f"{tipo}: R$ {transacao['valor']:.2f} | {transacao['data']}")

    print(f"\n💰 Saldo atual: R$ {conta_ativa.saldo:.2f}")
    print("🔷============================🔷\n")


def menu_gerar_relatorio(cliente):
    """
    Exibe um relatório de transações usando o gerador, com opção de filtro.
    """
    if not cliente.contas:
        print("🚫 Cliente não possui conta.")
        tocar_erro()
        return

    conta_ativa = cliente.contas[0]
    
    tipo_filtro = input("🔎 Deseja filtrar por tipo? (d para depósito, s para saque, ou enter para todos): ").lower().strip()
    
    if tipo_filtro == 'd':
        filtro = "Deposito"
    elif tipo_filtro == 's':
        filtro = "Saque"
    else:
        filtro = None

    print("\n📑 === RELATÓRIO DE TRANSAÇÕES === 📑")
    
    relatorio = conta_ativa.historico.gerar_relatorio(filtro)
    
    houve_transacao = False
    for transacao in relatorio:
        houve_transacao = True
        tipo = "🔻 Saque" if transacao['tipo'] == 'Saque' else "✅ Depósito"
        print(f"{tipo}: R$ {transacao['valor']:.2f} | Data: {transacao['data']}")

    if not houve_transacao:
        print("🚫 Nenhuma transação encontrada para este filtro.")

    print("🔷=================================🔷\n")


def criar_novo_cliente(clientes):
    """Cria e cadastra um novo cliente (Pessoa Física)."""
    cpf = input("🔎 Informe o CPF (somente números): ").strip()
    cpf = ''.join(filter(str.isdigit, cpf))

    if filtrar_cliente(cpf, clientes):
        print("⚠️ CPF já cadastrado!")
        tocar_erro()
        return

    nome = input("👤 Nome completo: ")
    nascimento = input("📅 Data de nascimento (dd/mm/aaaa): ")
    endereco = input("🏠 Endereço (logradouro, nro - bairro - cidade/UF): ")

    novo_cliente = PessoaFisica(nome=nome, data_nascimento=nascimento, cpf=cpf, endereco=endereco)
    clientes.append(novo_cliente)
    print("✅ Cliente criado com sucesso!")
    tocar_sucesso()

def criar_nova_conta(numero_conta, clientes, contas):
    """Cria uma nova conta corrente para um cliente."""
    cpf = input("🔎 Informe o CPF do titular da conta: ").strip()
    cpf = ''.join(filter(str.isdigit, cpf))
    
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("🚫 Cliente não encontrado. Cadastre o cliente primeiro.")
        tocar_erro()
        return

    nova_conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(nova_conta)
    cliente.adicionar_conta(nova_conta)

    print(f"✅ Conta criada com sucesso para {cliente.nome}!")
    print(f"Agência: {nova_conta.agencia}, Conta: {nova_conta.numero}")
    tocar_sucesso()


def filtrar_cliente(cpf, clientes):
    """Busca um cliente na lista pelo CPF."""
    clientes_filtrados = [cliente for cliente in clientes if isinstance(cliente, PessoaFisica) and cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def login(clientes):
    """Realiza o login do cliente no sistema."""
    print("\n🔐 LOGIN NO SISTEMA")
    cpf = input("Informe seu CPF (somente números): ").strip()
    cpf = ''.join(filter(str.isdigit, cpf))

    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        print(f"\n👋 Bem-vindo(a) ao banco SC, {cliente.nome}!")
        tocar_sucesso()
        return cliente
    
    print("\n❌ CPF não cadastrado. Por favor, crie um usuário.")
    tocar_erro()
    return None


def main():
    """Função principal que executa o sistema bancário."""
    clientes = []
    contas = []
    
    cliente_logado = None
    while not cliente_logado:
        print("""
🟢 BEM-VINDO AO BANCO VIRTUAL SC 🟢

[1] 🔐 Fazer login com CPF
[2] 📝 Criar novo cliente
[3] ❌ Sair
""")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            cliente_logado = login(clientes)
        elif escolha == "2":
            criar_novo_cliente(clientes)
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
[r] 📑 Gerar Relatório
[u] 👤 Criar Novo Cliente
[c] 🏦 Criar Nova Conta
[q] ❌ Sair

=> """
    
    while True:
        opcao = input(menu).strip().lower()

        if opcao == "d":
            menu_deposito(cliente_logado)
        elif opcao == "s":
            menu_saque(cliente_logado)
        elif opcao == "e":
            menu_exibir_extrato(cliente_logado)
        elif opcao == "r":
            menu_gerar_relatorio(cliente_logado)
        elif opcao == "u":
            criar_novo_cliente(clientes) 
        elif opcao == "c":
            numero_conta = len(contas) + 1
            criar_nova_conta(numero_conta, clientes, contas)
        elif opcao == "q":
            print("\n👋 Obrigado por utilizar nosso sistema bancário SC! Volte logo!")
            tocar_despedida()
            break
        else:
            print("❌ Opção inválida. Tente novamente.")
            tocar_erro()

if __name__ == "__main__":
    main()