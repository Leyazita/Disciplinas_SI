tempos = {}
for i in range(5):
    nome = input(f"Insira o nome do {i+1}º corredor: ")
    voltas = []
    for j in range(3):
        volta = float(input(f"Insira o tempo da {j+1}º volta em segundos: "))
        voltas.append(volta)
    tempos[nome] = voltas
 
melhor_tempo = float('inf')
melhor_corredor = ""
melhor_volta = 0
for i, (nome, voltas) in enumerate(tempos.items()):
    for j, volta in enumerate(voltas):
         if volta < melhor_tempo:
            melhor_tempo = volta
            melhor_corredor = nome
            melhor_volta = j+1

menor_media = float('inf')
campeao = ""
for nome, voltas in tempos.items():
    media = sum(voltas) / len(voltas)
    if media < menor_media:
        menor_media = media
        campeao = nome


print("melhor volta: ", melhor_volta)
print("melhor corredor: ", melhor_corredor)
print("melhor tempo: ", melhor_tempo)
print("campeao: ", campeao)