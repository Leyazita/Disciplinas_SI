def print_elements_list(lista):
    for i in lista:
        if type(i) == list:
            print_elements_list(i)
        else:
            print(i)
            
lista = [0,1,[2,[3,4]],5]
print_elements_list(lista)