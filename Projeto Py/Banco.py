class Banco:
  def __init__(self):
    self.saldo = 0
    self.depositos = []
    self.saques = []

  def deposito(self, valor):
    if valor > 0:
      self.saldo += valor
      self.depositos.append(valor)
      print("\n")
      print("==================================================")
      print("\n")
      print(f"Depósito de R$ {valor:.2f} Realizado com sucesso.")
      print("\n")
      print("==================================================")
  def saque(self, valor):
    if len(self.saques) < 3:
      if valor <= 500:
        if self.saldo >= valor:
           self.saldo -= valor
           self.saques.append(valor)
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
        print("O valor do saque não pode exeder R$500,00.")
        print("\n")
        print("==================================================")
    else:
      print("\n")
      print("==================================================")
      print("\n")
      print("Limite diário de saques atingido.")
      print("\n")
      print("==================================================")
      
      

  def extrato(self):
    print("\n")
    print("=======Extrato:=======")
    print("Depósitos:")
    for deposito in self.depositos:
      print(f"R$ {deposito:.2f}")
    print("----------------------")
    print("saques:")
    for saque in self.saques:
      print(f"R$ {saque:.2f}")
    print(f"Saldo atual: R$ {self.saldo:.2f}")
    print("=======================")
  def menu(self):
    while True:
      print("\n")
      print("=======Menu=======")
      print("\n")
      print("(D) Depositar")
      print("(S) Sacar")
      print("(E) Extrato")
      print("(Q) Sair")
      print("\n")
      print("==================")
      opcao = input("Escolha uma opção:").upper()

      if opcao == "D":
        valor = float(input("Digite o valor de depósito: "))
        self.deposito(valor)
      elif opcao == "S":
        valor = float(input("Digite o valor de saque: "))
        self.saque(valor)
      elif opcao == "E":
        self.extrato()
      elif opcao == "Q":
        print("Saindo do sistema. . .")
        break
      else:
        print("opção invalida. tente novamente.")

banco = Banco()
banco.menu()

