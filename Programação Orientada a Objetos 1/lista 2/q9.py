agenda = []

for i in range(10):
    nome = input("Digite o nome da pessoa: ")
    endereco = input("Digite o endereço da pessoa: ")
    cep = input("Digite o CEP da pessoa: ")
    bairro = input("Digite o bairro da pessoa: ")
    telefone = input("Digite o telefone da pessoa: ")
    agenda.append([nome, endereco, cep, bairro, telefone])

agenda.reverse()

print("Nome - Endereço - CEP - Bairro - Telefone")
for pessoa in agenda:
    print(" - ".join(pessoa))