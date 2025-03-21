def multiplication_of_positions(lista1, lista2):
    lista3 = []
    for i in range(len(lista1)):
        lista3.append(lista1[i] * lista2[i])
    return lista3


lista1 = []
lista2 = []
for i in range(10):
    lista1.append(int(input("Digite um número para lista 1: ")))
    lista2.append(int(input("Digite outro número para lista 2: ")))
    
print(lista1)
print(lista2)
print(multiplication_of_positions(lista1, lista2))