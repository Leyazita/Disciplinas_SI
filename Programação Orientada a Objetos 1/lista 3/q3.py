from q1 import Pessoa

class Elevador:
    def __init__(self, capacidade, andares):
        self.__capacidade = capacidade
        self.__andares = andares
        self.__andar_atual = 0
        self.__pessoas = []
        
        
    @property
    def capacidade(self):
        return self.__capacidade
    
    @capacidade.setter
    def capacidade(self, capacidade):
        if capaciade > 0:
            self.__capacidade = capacidade
        else:
            print('Capacidade deve ser maior que 0')
            
    @property
    def andares(self):
        return self.__andares
    
    @andares.setter
    def andares(self, andares):
        if andares > 0:
            self.__andares = andares
        else:
            print('Andares deve ser maior que 0')
            
    @property
    def andar_atual(self):
        return self.__andar_atual
    
    @andar_atual.setter
    def andar_atual(self, andar_atual):
        if andar_atual >= 0 and andar_atual <= self.__andares:
            self.__andar_atual = andar_atual
        else:
            print('Andar atual deve estar entre 0 e o número de andares')
            
    @property
    def pessoas(self):
        return self.__pessoas
    
    @pessoas.setter
    def pessoas(self, pessoas):
        if len(pessoas) <= self.__capacidade:
            self.__pessoas = pessoas
        else:
            print('Número de pessoas deve ser menor ou igual a capacidade')
    
    def entra(self, pessoa: Pessoa):
        if len(self.__pessoas) < self.__capacidade:
            self.__pessoas.append(pessoa)
        else:
            print('Elevador cheio')
        
    def sai(self):
        if len(self.__pessoas) > 0:
            self.__pessoas.pop(0)
        else:
            print('Elevador vazio')
            
    def sobe(self):
        if self.__andar_atual < self.__andares:
            self.__andar_atual += 1
        else:
            print('Elevador no último andar')
            
    def desce(self):
        if self.__andar_atual > 0:
            self.__andar_atual -= 1
        else:
            print('Elevador no térreo')
        
    def __str__(self):
        return f'Capacidade: {self.__capacidade}, Andares: {self.__andares}, Andar atual: {self.__andar_atual}, Pessoas: {[i.nome for i in self.__pessoas]}'
    
    def run(self):
        while True:
            print('1 - Entrar')
            print('2 - Sair')
            print('3 - Subir')
            print('4 - Descer')
            print('5 - Finalizar')
            op = int(input('Digite a opção desejada: '))
            if op == 1:
                nome = input('Digite o nome: ')
                nascimento = input('Digite a data de nascimento: ')
                altura = float(input('Digite a altura: '))
                p = Pessoa(nome, nascimento, altura)
                self.entra(p)
            elif op == 2:
                self.sai()
            elif op == 3:
                self.sobe()
            elif op == 4:
                self.desce()
            elif op == 5:
                break
            else:
                print('Opção inválida')
            print(self)
            
if __name__ == '__main__':
    Elevador(4, 6).run()
    