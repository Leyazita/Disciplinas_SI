class Aluno:
    def __init__(self, matricula, nome, nota1, nota2, nota3):
        self.__matricula = matricula
        self.__nome = nome
        self.__nota1 = nota1
        self.__nota2 = nota2
        self.__nota3 = nota3
        
    def media(self):
        media = (self.__nota1 * 2 + self.__nota2 * 3 + self.__nota3 * 5) / 10
        return media
    
    def final(self):   
        if self.media() >= 7:
            return 0
        elif self.media() < 7 and self.media() >= 5:
            return 14 - self.media()
        
    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def nota1(self):
        return self.__nota1
    
    @nota1.setter
    def nota1(self, nota1):
        self.__nota1 = nota1
        
    @property
    def nota2(self):
        return self.__nota2
    
    @nota2.setter
    def nota2(self, nota2):
        self.__nota2 = nota2
    
    @property
    def nota3(self):
        return self.__nota3
    
    @nota3.setter
    def nota3(self, nota3):
        self.__nota3 = nota3

class Turma(Aluno):
    def __init__(self):
        self.alunos = {}
    
    def addAluno(self, aluno):
        if aluno.matricula not in self.alunos:
            self.alunos[aluno.matricula] = aluno
        else:
            print(f"O(A) aluno(a) {aluno.nome} não foi matriculado. O numero fornecido na matricula ja esta em uso, por favor fornaça outro.")
            
    def encerramento_turma(self):
        self.lista_alunos = []
        for aluno in self.alunos.values():
            self.lista_alunos.append(aluno)
            
    def listagem_turma(self):
        try:
            self.lista_alunos
        except AttributeError:
            self.encerramento_turma()
            
        for aluno in self.lista_alunos:
            if aluno.media() >= 7:
                print(f"O(A) aluno(a) {aluno.nome} está aprovado com média {aluno.media()}")
            else:
                print(f"O(A) aluno(a) {aluno.nome} está com média {aluno.media()} e precisa tirar {aluno.final():.1f} na prova final para ser aprovado.")
         

if __name__ == '__main__':
    turma = Turma()
    turma.addAluno(Aluno(1, "Adriano", 5, 10, 10))
    turma.addAluno(Aluno(2, "João", 10, 7, 8))
    turma.addAluno(Aluno(3, "Maria", 4, 5, 6))
    turma.addAluno(Aluno(4, "José", 8, 7.5, 6))
    turma.addAluno(Aluno(5, "Pedro", 9, 9, 9))
    turma.addAluno(Aluno(6, "Vivi", 10, 10, 10))
    turma.addAluno(Aluno(7, "Ana", 5, 7, 9))
    turma.addAluno(Aluno(9, "Rafaela", 4, 5, 9))
    turma.addAluno(Aluno(9, "Bia", 7, 8, 7))
    
    #se a listagem for chamada primeira, o try except garante que a lista de alunos seja criada
    #turma.listagem_turma()
    
    turma.encerramento_turma()
    turma.listagem_turma()
    
    
    