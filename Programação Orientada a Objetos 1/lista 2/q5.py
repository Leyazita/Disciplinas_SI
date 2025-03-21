from random import randint

def game(num):
    random = randint(1, 100)
    tentativas = 0
    while True:
        if num == random:
            print("Parabéns, você acertou!")
            print("Número de tentativas: ", tentativas)
            if input("Deseja jogar novamente? (s/n): ") == "s":
                num = int(input("Qual é o numero?: "))
                game(num)
            else:
                break
        elif num > random:
            print("O número é menor que ", num)
            tentativas += 1
            num = int(input("Qual é o numero?: "))
        else:
            print("O número é maior que ", num)
            tentativas += 1
            num = int(input("Qual é o numero?: "))
        if tentativas == 10:
            print("Você perdeu!")
            quit()
            
num = int(input("Qual é o numero?: "))
game(num)