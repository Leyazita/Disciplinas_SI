from datetime import datetime

class Pessoa:
    def __init__(self, nome, nascimento, altura):
        self.__nome = nome 
        self.__nascimento = nascimento
        self.__altura = altura
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError('Nome deve ser uma string')
        
    @property
    def nascimento(self):
        return self.__nascimento
   
    @nascimento.setter
    def nascimento(self, nascimento):
        self.__nascimento = nascimento
        
    @property
    def idade(self):
        return datetime.now().year - int(self.nascimento.split('/')[2])
    
    def __str__(self):
        return f'Nome: {self.nome}, Nascimento: {self.nascimento}, Altura: {self.__altura}, Idade: {self.idade}'
        
if __name__ == '__main__':
    
    p = Pessoa('Ana', '01/02/1990', 1.50)
    print(p)
    