class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []
        
class Conta:
    def __init__(self, numero, saldo, transacoes):
        self.numero = numero
        self.saldo = saldo
        self.transacoes = transacoes
        
class ContaCorrente(Conta):
    def __init__(self, numero, saldo, transacoes):
        super().__init__(numero, saldo, transacoes)
        
class ContaPoupanca(Conta):
    def __init__(self, numero, saldo, transacoes):
        super().__init__(numero, saldo, transacoes)
        
class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []    
        
    def addCliente(self, cliente):
        self.clientes.append(cliente)
        
    def addConta(self, conta):
        self.contas.append(conta)
        
    def clienteCpf(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None
    
    def clienteNumeroConta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None
    
    def sacar(self, cpf, numero, valor):
        cliente = self.clienteCpf(cpf)
        conta = self.clienteNumeroConta(numero)
        if cliente and conta:
            if conta.saldo >= valor:
                conta.saldo -= valor
                conta.transacoes.append('Saque: ' + str(valor))
                return True
        return False
    
    def depositar(self, cpf, numero, valor):
        cliente = self.clienteCpf(cpf)
        conta = self.clienteNumeroConta(numero)
        if cliente and conta:
            conta.saldo += valor
            conta.transacoes.append('Depósito: ' + str(valor))
            return True
        return False
    
    def transferir(self, cpf, numero, valor, cpfDestino, numeroDestino):
        cliente = self.clienteCpf(cpf)
        conta = self.clienteNumeroConta(numero)
        clienteDestino = self.clienteCpf(cpfDestino)
        contaDestino = self.clienteNumeroConta(numeroDestino)
        if cliente and conta and clienteDestino and contaDestino:
            if conta.saldo >= valor:
                conta.saldo -= valor
                contaDestino.saldo += valor
                conta.transacoes.append('Transferência: ' + str(valor))
                return True
        return False
    
    def historico(self, cpf, numero):
        cliente = self.clienteCpf(cpf)
        conta = self.clienteNumeroConta(numero)
        if cliente and conta:
            for transacao in conta.transacoes:
                print(transacao)
                
    def infoBanco(self):
        print(f"Total de clientes: {len(self.clientes)}")
        print(f"Total de contas: {len(self.contas)}")
        for cliente in self.clientes:
            print(f"Cliente: {cliente.nome} tem {len(cliente.contas)} contas")
            