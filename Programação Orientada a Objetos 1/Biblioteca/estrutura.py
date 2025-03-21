import tkinter as tk
import pickle

class Autor:
    def __init__(self, nome, nacionalidade, data_nascimento, genero):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.data_nascimento = data_nascimento
        self.genero = genero

class Livro:
    def __init__(self, titulo, autor, ano_publicacao, editora):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.editora = editora

class Biblioteca:
    def __init__(self):
        self.autores = {}
        self.livros = {}
    
    def adicionar_livro(self, titulo, autor, ano_publicacao, editora):
        if not all([titulo, autor, ano_publicacao, editora]):
            raise ValueError("Preencha todos os campos!")

        if autor not in self.autores:
            raise ValueError("Autor não encontrado na biblioteca!")

        livro = Livro(titulo, autor, ano_publicacao, editora)
        self.livros[titulo] = livro
        print(f"{titulo} adicionado à biblioteca.")
            
    def adicionar_autor(self, nome, nacionalidade, data_nascimento, genero):
        if not all([nome, nacionalidade, data_nascimento, genero]):
            raise ValueError("Preencha todos os campos!")

        autor = Autor(nome, nacionalidade, data_nascimento, genero)
        self.autores[nome] = autor
        print(f"{nome} adicionado à biblioteca.")
    
    def listar_livros(self):
        for livro in self.livros.values():
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano de Publicação: {livro.ano_publicacao}, Editora: {livro.editora}")
    
    def listar_autores(self):
        for autor in self.autores.values():
            print(f"Nome: {autor.nome}, Nacionalidade: {autor.nacionalidade}, Data de Nascimento: {autor.data_nascimento}, Gênero: {autor.genero}")
    
    def buscar_livro(self, titulo):
        if titulo in self.livros:
            livro = self.livros[titulo]
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano de Publicação: {livro.ano_publicacao}, Editora: {livro.editora}")
        else:
            print(f"{titulo} não encontrado na biblioteca.")
    
    def buscar_autor(self, nome):
        if nome in self.autores:
            autor = self.autores[nome]
            print(f"Nome: {autor.nome}, Nacionalidade: {autor.nacionalidade}, Data de Nascimento: {autor.data_nascimento}, Gênero: {autor.genero}")
        else:
            print(f"{nome} não encontrado na biblioteca.")
            
    def excluir_livro(self, titulo):
        if titulo in self.livros:
            del self.livros[titulo]
            print(f"{titulo} excluído da biblioteca.")
        else:
            print(f"{titulo} não encontrado na biblioteca.")
            
    def excluir_autor(self, nome):
        if nome in self.autores:
            del self.autores[nome]
            print(f"{nome} excluído da biblioteca.")
        else:
            print(f"{nome} não encontrado na biblioteca.")

    def salvar(self):
        with open("biblioteca.dat", "wb") as arquivo:
            pickle.dump(self, arquivo)
            print("Biblioteca salva com sucesso!")
            
    def carregar(self):
        with open("biblioteca.dat", "rb") as arquivo:
            biblioteca = pickle.load(arquivo)
            self.autores = biblioteca.autores
            self.livros = biblioteca.livros
            print("Biblioteca carregada com sucesso!")
            
    def limpar(self):
        self.autores.clear()
        self.livros.clear()
        print("Biblioteca limpa com sucesso!")
        
if __name__ == "__main__":
    #menu interativo
    biblioteca = Biblioteca()
    print("Bem vindo à biblioteca!")
    while True:
        print("1 - Adicionar livro")
        print("2 - Adicionar autor")
        print("3 - Listar livros")
        print("4 - Listar autores")
        print("5 - Buscar livro")
        print("6 - Buscar autor")
        print("7 - Excluir livro")
        print("8 - Excluir autor")
        print("9 - Sair")
        #faça o que for preciso para que o usuário possa escolher uma opção e trate as exceções
        try:
            opcao = int(input("Escolha uma opção: "))   
        except ValueError:
            print("Digite um número inteiro!")
            continue
        
        if opcao == 1:
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano_publicacao = input("Ano de Publicação: ")
            editora = input("Editora: ")
            try:
                biblioteca.adicionar_livro(titulo, autor, ano_publicacao, editora)
            except ValueError as e:
                print(e)
                
        elif opcao == 2:
            nome = input("Nome: ")
            nacionalidade = input("Nacionalidade: ")
            data_nascimento = input("Data de Nascimento: ")
            genero = input("Gênero: ")
            try:
                biblioteca.adicionar_autor(nome, nacionalidade, data_nascimento, genero)
            except ValueError as e:
                print(e)
                
        elif opcao == 3:
            if len(biblioteca.livros) == 0:
                print("A biblioteca está vazia!")
            else:
                biblioteca.listar_livros()
            

        elif opcao == 4:
            if len(biblioteca.autores) == 0:
                print("A biblioteca está vazia!")
            else:
                biblioteca.listar_autores()
            
        elif opcao == 5:
            if len(biblioteca.livros) == 0:
                print("A biblioteca está vazia!")
            else:
                titulo = input("Título: ")
                biblioteca.buscar_livro(titulo) 
        
        elif opcao == 6:
            if len(biblioteca.autores) == 0:
                print("A biblioteca está vazia!")
            else:
                nome = input("Nome: ")
                biblioteca.buscar_autor(nome)
            
        elif opcao == 7:
            titulo = input("Título: ")
            biblioteca.excluir_livro(titulo)
        
        elif opcao == 8:
            if len(biblioteca.autores) == 0:
                print("A biblioteca está vazia!")
            else:
                nome = input("Nome: ")
                biblioteca.excluir_autor(nome)
            
        elif opcao == 9:
            print("Até mais!")
            break
        