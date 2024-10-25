class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.usuarios = []
        self.contas = []
        self.numero_conta = 1

    def saque(self, *, saldo, valor, extrato, limite, numero_saque, limite_saques):
        if numero_saque < limite_saques:
            if valor <= limite:
                if saldo >= valor:
                    saldo -= valor
                    extrato.append(f"Saque: -R$ {valor:.2f}")
                    print("\n")
                    print("==================================================")
                    print("\n")
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
                    print("\n")
                    print("==================================================")
                else:
                    print("\n")
                    print("==================================================")
                    print("\n")
                    print("Saldo insuficiente para realizar o saque.")
                    print("\n")
                    print("==================================================")
            else:
                print("\n")
                print("==================================================")
                print("\n")
                print("O valor do saque não pode exceder R$500,00.")
                print("\n")
                print("==================================================")
        else:
            print("\n")
            print("==================================================")
            print("\n")
            print("Limite diário de saques atingido.")
            print("\n")
            print("==================================================")
        return saldo, extrato

    def deposito(self, saldo, valor, extrato, /):
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: +R$ {valor:.2f}")
            print("\n")
            print("==================================================")
            print("\n")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            print("\n")
            print("==================================================")
        return saldo, extrato

    def extrato(self, saldo, *, extrato):
        print("\n")
        print("=======Extrato:=======")
        print("Transações:")
        for transacao in extrato:
            print(transacao)
        print("----------------------")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("=======================")

    def criar_usuario(self, nome, data_nascimento, cpf, endereco):
        if any(usuario['cpf'] == cpf for usuario in self.usuarios):
            print("CPF já cadastrado.")
            return
        usuario = {
            'nome': nome,
            'data_nascimento': data_nascimento,
            'cpf': cpf,
            'endereco': endereco
        }
        self.usuarios.append(usuario)
        print("Usuário criado com sucesso.")

    def criar_conta_corrente(self, cpf):
        usuario = next((usuario for usuario in self.usuarios if usuario['cpf'] == cpf), None)
        if not usuario:
            print("Usuário não encontrado.")
            return
        conta = {
            'agencia': '0001',
            'numero_conta': self.numero_conta,
            'usuario': usuario
        }
        self.contas.append(conta)
        self.numero_conta += 1
        print("Conta criada com sucesso.")
        return conta

    def listar_contas(self):
        for conta in self.contas:
            print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Usuário: {conta['usuario']['nome']}")

    def menu(self):
        while True:
            print("\n")
            print("=======Menu=======")
            print("\n")
            print("(D) Depositar")
            print("(S) Sacar")
            print("(E) Extrato")
            print("(C) Criar Usuário")
            print("(A) Criar Conta Corrente")
            print("(L) Listar Contas")
            print("(Q) Sair")
            print("\n")
            print("==================")
            opcao = input("Escolha uma opção: ").upper()

            if opcao == "D":
                valor = float(input("Digite o valor de depósito: "))
                self.saldo, self.depositos = self.deposito(self.saldo, valor, self.depositos)
            elif opcao == "S":
                valor = float(input("Digite o valor de saque: "))
                limite = 500
                limite_saques = 3
                self.saldo, self.saques = self.saque(saldo=self.saldo, valor=valor, extrato=self.saques, limite=limite, numero_saque=len(self.saques), limite_saques=limite_saques)
            elif opcao == "E":
                self.extrato(self.saldo, extrato=self.depositos + self.saques)
            elif opcao == "C":
                nome = input("Digite o nome: ")
                data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
                cpf = input("Digite o CPF (somente números): ")
                endereco = input("Digite o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
                self.criar_usuario(nome, data_nascimento, cpf, endereco)
            elif opcao == "A":
                cpf = input("Digite o CPF do usuário: ")
                self.criar_conta_corrente(cpf)
            elif opcao == "L":
                self.listar_contas()
            elif opcao == "Q":
                print("Saindo do sistema. . .")
                break
            else:
                print("Opção inválida. Tente novamente.")

banco = Banco()
banco.menu()