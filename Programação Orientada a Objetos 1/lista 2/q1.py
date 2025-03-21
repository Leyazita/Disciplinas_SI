def tamString(s):
    size = 0
    for i in s:
        size += 1
    return size

string = input("Digite uma palavra: ")
print("A palavra tem", tamString(string), "letras")