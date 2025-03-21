agenda = {}
opcao = 0
    

while opcao >= 0:
    print("1 - Inserir um novo nome")
    print("2 - Incluir um novo telefone")
    print("3 - Excluir um telefone")
    print("4 - Excluir um nome")
    print("5 - Consultar telefones")
    opcao = int(input("Digite a opção desejada: "))
     
    if opcao == 1:
            nome = input("Digite o nome: ")
            agenda[nome] = []
    elif opcao == 2:
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            agenda[nome].append(telefone)
    elif opcao == 3:
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            agenda[nome].remove(telefone)
    elif opcao == 4:
            nome = input("Digite o nome: ")
            del agenda[nome]
    elif opcao == 5:
            nome = input("Digite o nome: ")
            print(agenda[nome])
        
            
            