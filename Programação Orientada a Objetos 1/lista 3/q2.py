from q1 import Pessoa


class Agenda:
    
    __pessoas: dict[str, Pessoa] = {}
   
    @classmethod
    def addPessoa(cls, pessoa: Pessoa):
       cls.__pessoas[pessoa.nome] = pessoa
       
    @classmethod
    def removePessoa(cls, nome: str):
        cls.__pessoas.pop(nome)
    
    @classmethod    
    def buscaPessoa(cls, nome: str):
        return cls.__pessoas.get(nome, None)
    
    @classmethod
    def imprimeAgenda(cls):
        for pessoa in cls.__pessoas:
            print(cls.__pessoas[pessoa])
            
if __name__ == '__main__':
    
    Agenda.addPessoa(Pessoa('Adriano', '01/02/1999', 1.50))
    Agenda.addPessoa(Pessoa('João', '01/02/2001', 1.50))
    Agenda.addPessoa(Pessoa('Maria', '01/02/1985', 1.50))
    Agenda.addPessoa(Pessoa('José', '01/02/1800', 1.50))
    Agenda.addPessoa(Pessoa('Pedro', '01/02/2000', 1.50))
    Agenda.addPessoa(Pessoa('Vivi', '01/02/2002', 1.40))
    Agenda.addPessoa(Pessoa('Ana', '01/02/2005', 1.50))
    Agenda.addPessoa(Pessoa('Rafaela', '01/02/2007', 1.50))
    Agenda.addPessoa(Pessoa('Bia', '01/02/1991', 1.50))
    
    Agenda.imprimeAgenda()
    

    