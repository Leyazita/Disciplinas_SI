from abc import ABC, abstractmethod

class ClasseAbstrata(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def metodo_abstrato(self):
        print("Método abstrato")
        pass
    
    
    
class ClasseFilha(ClasseAbstrata):
    def __init__(self, nome):
        super().__init__(nome)
        self.nome = nome

    def metodo_abstrato(self):
        print("Método abstrato da classe filha")
        
        
        
if __name__ == "__main__":
    c = ClasseFilha("Classe Filha")
    c.metodo_abstrato()
   