from jogador import *
from professores import *
from abc import ABC, abstractmethod
from random import randint, choice
from time import sleep


class Arena(ABC):
    @abstractmethod
    def lutar(self, professores, aluno, arena):
        pass
    
    
class Luta(Arena):
    def __init__(self):
        self.arena = 0
        
    def lutar(self, professores, aluno, arena):
        professor = choice(list(professores.keys()))
        self.arena = arena
        rodada = 1
        print('-------------------------------')
        print(f'Arena {arena}')
        while True:
            print('-------------------------------')
            print(f'Rodada {rodada}')
            print('-------------------------------')
            print(f'Professor {professor}')
            print(f'Ataque - {professores[professor].atacar()}')
            aluno.reduz_vida(professores[professor].ataque)
            sleep(2)
            print(f'Aluno {aluno.nome}')
            print(f'Ataque - {aluno.atacar()}')
            professores[professor].reduz_vida(aluno.ataque)
            sleep(2)
            print()
            rodada += 1
            
            if (aluno.get_vida_atual() <= 0):
                print('Aluno perdeu!')
                professores[professor].reinicia_vida()
                break
            elif (professores[professor].get_vida_atual() <= 0):
                print('Professor Perdeu')
                professores[professor].reinicia_vida()
                break