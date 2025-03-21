from jogador import *
from professores import *
from arena import *
from time import sleep
import os
        
class Mundo:
        def __init__(self):
                self.aluno = None
                self.professores = {}
                self.periodos_profs = {}
                self.num_arena = 0
                
        def run(self):
                self.instancia_professores()
                self.organiza_periodos()
                
        def avanca_fase(self):
                self.arena()
                self.fight()
                self.resultados()
                
        #fazer tratamentos de erros e por em um loop, lembrar de pedir o nome do aluno
        
        def instancia_professores(self):
                airton = Professor('Airton', 'Metodologia', ['Beleza, mas e o artigo?', 'Da uma engordada nesse paragrafo ai'])
                self.professores['Airton'] = airton
                debora = Professor('Débora', 'Sistemas Operacionais', ['Gravem um video', 'Prova quinta'])
                self.professores['Débora'] = debora
                flavio = Professor('Flávio','Programacao Orientadas a Objetos', ['Se tirou nota baixa, desiste nao pessoal', 'Prova na proxima segunda'])
                self.professores['Flávio'] = flavio
                frank = Professor('Frank', 'Matemática Discreta e Circuitos', ['Seminario turma', 'Agora as perguntas...'])
                self.professores['Frank'] = frank
                glauber = Professor('Glauber', 'Algoritmos 2 e Banco de Dados 2', ['Isso ta muito custoso', 'Lista de atividade pessoal'])
                self.professores['Glauber'] = glauber
                imperes = Professor('Imperes', 'BD1 e Web1', ['Com banco de dados da pra fazer muita coisa', 'Falando sobre banco de dados...'])
                self.professores['Imperes'] = imperes
                ismael = Professor('Ismael', 'SI 1, Empreendedorismo, Gestao empresarial',  ['Conta uma piada', 'Conta a mesma piada de sempre'])
                self.professores['Ismael'] = ismael
                juliana = Professor('Juliana', 'ED2 e Prolog', ['Postei ums lista de exercios de fixaçao e uma lista de exercicios avaliativa'])
                self.professores['Juliana'] = juliana
                leonardo = Professor('Leonardo', 'Algoritmos 1', ['Entao turma...', 'Vamos passar 2 meses em portugol'])
                self.professores['Leonardo'] = leonardo
                oseas = Professor('Oseas', 'Ed1', ['Como eu sou humilde', 'Esse cabeçao tem que servir para alguma coisa'])
                self.professores['Oseas'] = oseas
                pamela = Professor('Pâmela', 'Engenharia 1', ['Voces ja tem o projeto?', 'Façam uma cruzadinha sobre o ultimo conteudo'])
                self.professores['Pâmela'] = pamela
                rayner = Professor('Rayner', 'Redes 1 e SD', ['Porque as respostas de vocs estao iguais?', 'Falando por duas horas seguidas...'])
                self.professores['Rayner'] = rayner
                romuere = Professor('Romuere', 'Poo 2', ['Voces ja tem planos para o feriado? rsrs', 'Isso é uma CNN, implementem'])
                self.professores['Romuere'] = romuere
                fredson = Professor('Fredson', 'Redes 2', ['Na empresa....', 'Conta uma historia de vida'])
                self.professores['Fredson'] = fredson
        
        def organiza_periodos(self):
                self.periodos_profs[1] = {'Ismael': self.professores['Ismael'],
                                          'Airton': self.professores['Airton'],
                                          'Juliana': self.professores['Juliana'],
                                          'Leonardo': self.professores['Leonardo']}
                                          
                self.periodos_profs[2] = {'Frank': self.professores['Frank'],
                                          'Ismael': self.professores['Ismael'],
                                          'Juliana': self.professores['Juliana'],
                                          'Glauber': self.professores['Glauber']}

                
                self.periodos_profs[3] = {'Imperes': self.professores['Imperes'],
                                          'Pâmela': self.professores['Pâmela'],
                                          'Débora': self.professores['Débora'],
                                          'Flávio': self.professores['Flávio'],
                                          'Oseas': self.professores['Oseas']}
                
                self.periodos_profs[4] = {'Glauber': self.professores['Glauber'],
                                          'Pâmela': self.professores['Pâmela'],
                                          'Romuere': self.professores['Romuere'],
                                          'Juliana': self.professores['Juliana'],
                                          'Rayner': self.professores['Rayner']}
                
                self.periodos_profs[5] = {'Fredson': self.professores['Fredson'],
                                         'Romuere': self.professores['Romuere'],
                                         'Imperes': self.professores['Imperes'],
                                         'Airton': self.professores['Airton']}
                
        def iniciar_game(self):           
                while True:
                                nome = input("digite seu nome: ")
                                self.aluno = Aluno(nome)
                                print('-------------------------------')
                                print("seja bem vindo ao jogo", nome)
                                print('-------------------------------')
                                sleep(3)
                                os.system('cls')
                                break
                
        def arena(self): 
                print("----------------------------------") 
                print("Arena 1")
                print("Disciplinas: si1, metodologia,  algoritmos 1, logica, gestao empresarial")
                print("Professores: Ismael, Airton, Leornado, Juliana")
                print("----------------------------------")
                
                print("Arena 2")
                print("Disciplinas: circuitos, empreeendedorismo, algoritmos 2, mat. discreta, prolog")
                print("Professores: Frank, Ismael, Juliana, Glauber")
                print("----------------------------------")
                
                print("Arena 3")
                print("Disciplinas: bd 1, engenharia 1, SO, poo1, ed1")
                print("Professores: Imperes, Pâmela, Débora, Flávio, Oseas")
                print("----------------------------------")
                
                print("Arena 4")
                print("Disciplinas: bd2, engenharia 1, poo2, ed2, redes 1")
                print("Professores: Glauber, Pâmela, Romuere, Juliana, Rayner")
                print("----------------------------------")
                
                print("Arena 5")
                print("Disciplinas: redes 2, visao computacional, web 1, tcc, sistemas distribuidos")
                print("Professores: Fredson, Romuere, Imperes, Airton, Rayner") 
                print("----------------------------------")            
                
                sleep(3)
                os.system('cls')
                
        def fight(self):
                luta = Luta()
                
                #verificar qual arena o aluno está
                if (self.aluno.ira == 5):
                        luta.lutar(self.periodos_profs[1], self.aluno, 1)
                elif (self.aluno.ira == 6):
                        luta.lutar(self.periodos_profs[2], self.aluno, 2)
                elif (self.aluno.ira == 7):
                        luta.lutar(self.periodos_profs[3], self.aluno, 3)
                elif (self.aluno.ira == 8):
                        luta.lutar(self.periodos_profs[4], self.aluno, 4)
                elif (self.aluno.ira == 9):
                        luta.lutar(self.periodos_profs[5], self.aluno, 5)
                
        def resultados(self):
                
                if (self.aluno.ira == 10):
                        print('Parabéns! Zerou o game!')
                        return
                
                if self.aluno.vida <= 0:
                        if self.aluno.ira == 5:
                                print('Perdeu na primeira fase vacilão!')
                        else:
                                print("Game over vacilao...")
                                self.aluno.ira -= 1
                     
                else:
                        print("Show de bola, Você ganhou!")
                        self.aluno.reinicia_vida()
                        self.aluno.ira += 1
                        sleep(3)
                        os.system('cls')
                        self.avanca_fase()


