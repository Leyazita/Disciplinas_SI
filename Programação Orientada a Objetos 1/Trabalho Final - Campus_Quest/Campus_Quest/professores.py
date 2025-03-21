import random
from jogador import Personagem
from abc import ABC, abstractmethod
from random import randint
    
class Professor(Personagem):
        def __init__(self, nome, disciplina, frase):
                super().__init__(vida=30, ataque=randint(10, 40))
                self.nome = nome
                self.disciplina = disciplina
                self.frase = frase

        def get_vida_atual(self):
                return self.vida
        
        def atacar(self):
              print(random.choice(self.frase))
              return self.ataque 
        
        def reduz_vida(self, ataque_adv):
                self.vida -= ataque_adv
                
        def reinicia_vida(self):
                self.vida = 50        