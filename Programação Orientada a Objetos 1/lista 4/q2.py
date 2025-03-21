class Livro:
    def __init__(self, titulo, autor, data, preco):
        self.__titulo = titulo
        self.__autor = autor
        self.__data = data
        self.__preco = preco
    
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
        
    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self, autor):
        self.__autor = autor
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data
        
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, preco):
        self.__preco = preco
        
        
class Biblioteca(Livro):
    def __init__(self):
        self.__livros = []
        
    def addLivro(self, livro):
        self.__livros.append(livro)
        
    def exibirLivros(self):
        for livro in self.__livros:
            print(livro.titulo)
            
    def mostrarDadosLivro(self, titulo):
        for livro in self.__livros:
            if livro.titulo == titulo:
                print(livro.titulo, livro.autor, livro.data, livro.preco)
                       
if __name__ == '__main__':
    
    biblioteca = Biblioteca()
    while True:
        print("1 - Adicionar livro")
        print("2 - Exibir livros")
        print("3 - mostrar dados de um livro")
        print("4 - Sair")
        
        try:
            opcao = int(input("Digite a opção desejada: "))
        
            if opcao == 1:
                titulo = input("Digite o título do livro: ")
                autor = input("Digite o autor do livro: ")
                data = input("Digite a data de lançamento do livro: ")
                preco = float(input("Digite o preço do livro: "))
            
                livro = Livro(titulo, autor, data, preco)
                biblioteca.addLivro(livro)
            if opcao == 2:
                try:
                    biblioteca
                    biblioteca.exibirLivros()
                except NameError:
                    print("Não há livros cadastrados")
            if opcao == 3:
                try:
                    biblioteca
                    titulo = input("Digite o título do livro: ")
                    biblioteca.mostrarDadosLivro(titulo)
                except NameError:
                    print("Não há livros cadastrados")
            if opcao == 4:
                break
            
        except ValueError:
            print("Opção inválida")
            
    