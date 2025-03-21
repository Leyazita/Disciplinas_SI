class Conta:
    
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
        
    def extrato(self):
        print('Titular da conta: ', self.nome)
        print('Saldo da conta: ', self.saldo)
    
    def deposito(self, deposito):
        self.saldo += deposito
        print('Deposito realizado com sucesso.')
        return self.saldo
    
    def sacar(self, sacar):
        if self.saldo >= sacar:
            self.saldo -= sacar
            print('Saque realizado com sucesso.')
        else:
            print('Voce tentou sacar:', sacar)
            print('Saldo insuficiente.')
        return self.saldo
    
    def saldo(self):
        return self.saldo
    
    def transferir(self, valor, conta):
        if self.saldo >= valor:
            self.saldo -= valor
            conta.saldo += valor
            print('Transferencia realizada com sucesso.')
        else:
            print('Voce tentou transferir:', valor)
            print('Saldo insuficiente.')
        return self.saldo


while True:
    print('1 - Criar conta')
    print('2 - Depositar')
    print('3 - Sacar')
    print('4 - Extrato')
    print('5 - Transferir')
    print('6 - Sair')
    opcao = int(input('Digite a opcao desejada: '))
    
    if opcao == 1:
        nome = input('Digite o nome do titular da conta: ')
        saldo = float(input('Digite o saldo inicial: '))
        conta = Conta(nome, saldo)
        print('Conta criada com sucesso!')
    elif opcao == 2:
        deposito = float(input('Digite o valor do deposito: '))
        conta.deposito(deposito)
    elif opcao == 3:
        sacar = float(input('Digite o valor do saque: '))
        conta.sacar(sacar)
    elif opcao == 4:
        Conta.extrato()
    elif opcao == 5:
        valor = float(input('Digite o valor da transferencia: '))
        conta.transferir(valor, conta)
    elif opcao == 6:
        break