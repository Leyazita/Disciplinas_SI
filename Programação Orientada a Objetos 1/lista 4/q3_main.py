from q3 import Cliente, Conta, ContaCorrente, ContaPoupanca, Banco

banco = Banco()

cliente1 = Cliente("João", "111.111.111-11")
cliente2 = Cliente("Maria", "222.222.222-22")
conta1 = ContaCorrente("1111", 1000, [])
conta2 = ContaPoupanca("2222", 2000, [])
cliente1.contas.append(conta1)
cliente2.contas.append(conta2)
banco.addCliente(cliente1)
banco.addCliente(cliente2)
banco.addConta(conta1)
banco.addConta(conta2)

def menu():
    print("1. Sacar")
    print("2. Depositar")
    print("3. Transferir")
    print("4. Histórico")
    print("5. Informações do banco")
    print("6. Sair")

while True:
    menu()
    opcao = input("Digite a opção desejada: ")
    
    if opcao == "1":
        cpf = input("Digite o CPF do cliente: ")
        numero = input("Digite o número da conta: ")
        valor = float(input("Digite o valor do saque: "))
        if banco.sacar(cpf, numero, valor):
            print("Saque realizado com sucesso.")
        else:
            print("Não foi possível realizar o saque.")
    
    elif opcao == "2":
        cpf = input("Digite o CPF do cliente: ")
        numero = input("Digite o número da conta: ")
        valor = float(input("Digite o valor do depósito: "))
        if banco.depositar(cpf, numero, valor):
            print("Depósito realizado com sucesso.")
        else:
            print("Não foi possível realizar o depósito.")
    
    elif opcao == "3":
        cpf = input("Digite o CPF do cliente: ")
        numero = input("Digite o número da conta: ")
        valor = float(input("Digite o valor da transferência: "))
        cpfDestino = input("Digite o CPF do destinatário: ")
        numeroDestino = input("Digite o número da conta do destinatário: ")
        if banco.transferir(cpf, numero, valor, cpfDestino, numeroDestino):
            print("Transferência realizada com sucesso.")
        else:
            print("Não foi possível realizar a transferência.")
    
    elif opcao == "4":
        cpf = input("Digite o CPF do cliente: ")
        numero = input("Digite o número da conta: ")
        banco.historico(cpf, numero)
    
    elif opcao == "5":
        banco.infoBanco()
    
    elif opcao == "6":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida.")
        
        
#Aviso: se nao digitar o cpf como foi cadastrado(com . e -) o deposito/saque/transferencia 
#nao sera realizado. Ex: 111.111.111-11

#Quando for testar o historico, precisa realizar uma operacao antes. Ex: depositar, sacar, transferir
