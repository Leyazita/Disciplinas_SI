def sort_string(string):
    string = list(string)
    for i in range(len(string)):
        for j in range(len(string)): 
            if string[i] < string[j]:
                string[i], string[j] = string[j], string[i] 
    return string

string = input("Digite a string: ")
print(sort_string(string))