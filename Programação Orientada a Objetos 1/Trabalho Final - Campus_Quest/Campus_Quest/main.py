import random
from abc import ABC, abstractmethod
from random import randint
from jogador import Aluno, Personagem
from professores import *
from mundo import *

#testando o jogo

print("Bem vindo ao Campus Quest!")
print("Sera uma luta por arena, deseja iniciar o jogo?")

while True:
        try:
                opcao = int(input("1 - Sim\n2 - Nao\n"))
                if opcao == 1:
                        mundo = Mundo()
                        mundo.run()
                        mundo.iniciar_game()
                        mundo.arena()
                        mundo.fight()
                        mundo.resultados()
                        break
                elif opcao == 2:
                        print("saindo do jogo...")
                        break   
        except ValueError:
                print("Por favor, digite uma opcao valida")