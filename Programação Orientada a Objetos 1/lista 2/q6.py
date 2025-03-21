def swap_positions(lista):
    inicio = 0
    fim = len(lista) - 1

    while inicio < fim:
        lista[inicio], lista[fim] = lista[fim], lista[inicio]
        inicio += 1
        fim -= 1
    return lista

#lista = []
#for i in range(0, 10):
#lista.append(input("Digite um valor: ")) 

lista = [i for i in range(10)]
print(lista) 
print("Invertendo a lista...")
print(swap_positions(lista))

