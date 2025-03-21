def media(nome, notas):
    if nome in notas:
        media = sum(notas[nome]) / len(notas[nome])
        return media
    else:
        return "Aluno não encontrado."

notas = {}
while True:
    nome = input("Insira o nome do aluno (ou um 's' para sair): ")
    if nome == 's':
        break
    nota1 = float(input("Insira a primeira nota: "))
    nota2 = float(input("Insira a segunda nota: "))
    notas[nome] = (nota1, nota2)
    
nome = input("Insira o nome do aluno para ver a média: ")
print("Media: ", media(nome, notas))