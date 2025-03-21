def index_string(string, index):
    for i in string:
        if i == index:
            return string.index(i)

string = input("Digite a string: ")          
index = input("Procurar o index da letra: ")
print(index_string(string, index))
    