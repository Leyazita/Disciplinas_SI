class Conta():
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))
    
    def deposita(self, valor):
        self.saldo += valor
        
    def saca(self, valor):
        self.saldo -= valor
        
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    
class Pessoa():
    
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        
    def imprimir(self):
        print("Nome: ", self.nome)
        print("CPF: ", self.cpf)
        

while True:
    print("1 - Criar conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Transferir")
    print("5 - Extrato")
    print("6 - Sair")
    opcao = int(input("Escolha uma operaçao: "))  
   
   
    if opcao == 1:
        nome = input("Digite o nome do titular: ")
        cpf = input("Digite o CPF do titular: ")
        numero = input("Digite o número da conta: ")
        saldo = float(input("Digite o saldo inicial: "))   
        conta = Conta(numero, Pessoa(nome, cpf), saldo)
        print("Conta criada com sucesso!")
    elif opcao == 2:
        if conta:
            valor = float(input("Digite o valor a ser depositado: "))
            conta.deposita(valor)
            print("Depósito realizado com sucesso!")
        else:
            print("Conta não encontrada")
    elif opcao == 3:
        if conta:
            valor = float(input("Digite o valor a ser sacado: "))
            conta.saca(valor)
        else:
            print("Conta não encontrada")
    elif opcao == 4:
        if conta:
            valor = float(input("Digite o valor a ser transferido: "))
            destino = input("Digite a conta destino: ")
            conta.transfere(valor, destino)
        else:
            print("Conta não encontrada")
    elif opcao == 5:
        if conta:
            conta.extrato()
        else:
            print("Conta não encontrada")
    elif opcao == 6:
        break
