from abc import ABC, abstractmethod
from random import randint

class Personagem(ABC):
    def __init__(self, vida, ataque):
        self.vida = vida
        self.ataque = ataque

    @abstractmethod
    def get_vida_atual(self):
        pass

    @abstractmethod
    def atacar(self):
        pass
    
    @abstractmethod
    def reduz_vida(self, ataque_adv):
        pass
    
    @abstractmethod
    def reinicia_vida(self):
        pass  

class Aluno(Personagem):
    def __init__(self, nome):
        super().__init__(vida=50, ataque=randint(10, 40))
        self.nome = nome
        self.ira = 5

    def get_vida_atual(self):
        return self.vida

    def atacar(self):
        return self.ataque
    
    def reduz_vida(self, ataque_adv):
        self.vida -= ataque_adv
        
    def reinicia_vida(self):
        self.vida = 50 
        