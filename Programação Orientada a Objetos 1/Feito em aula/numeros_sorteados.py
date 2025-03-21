import random

num_sorteados = []
sorteados_repetidos = []

n = input('Digite um numero para inciar a sequencia: ')
n2 = input('Digite um numero para finalizar a sequencia: ')
qtd = input('Digite a quantidade de numeros sorteados: ')

for i in range(int(qtd)):
    num_sorteados.append(random.randint(int(n), int(n2)))
    if num_sorteados[i] in num_sorteados[:i]:
        sorteados_repetidos.append(num_sorteados[i])
        
print('Numeros sorteados: ', num_sorteados)