from random import randint as rd

lista = [rd(0, 100) for i in range(100)]

media = sum(lista) / len(lista)
mediana = sorted(lista)[len(lista) // 2]
variancia = sum([(i - media) ** 2 for i in lista]) / len(lista)
desvio_padrao = variancia ** 0.5

print("Media: ", media)
print("Mediana: ", mediana)
print("Variancia: ", variancia)
print("Desvio padrao: ", desvio_padrao)