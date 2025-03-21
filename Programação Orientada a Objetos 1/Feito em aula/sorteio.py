from random import randint as rd

inicial = input("Qual o numero inicial do sorteio? ")
final = input("Qual o numero final do sorteio? ")

num_sorteio = input("quantos numeros deseja sortear? ")
num_sorteado = []

for i in range(num_sorteio):
    num_sorteado.append(rd.randint(inicial, final))
    if num_sorteado[i] in num_sorteado[:i]:
        num_sorteado.pop()
