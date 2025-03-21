class Tv:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def aumentar_volume(self):
        self.volume += 1

    def diminuir_volume(self):
        self.volume -= 1

    def aumentar_canal(self):
        self.canal += 1

    def diminuir_canal(self):
        self.canal -= 1

    def mudar_canal(self, canal):
        self.canal = canal

    def __str__(self):
        return f"Canal: {self.canal} Volume: {self.volume}"

class Controle:
    def __init__(self):
        self.__observers: list[Tv] = []
        
    def addListener(self, tv: Tv):
        self.__observers.append(tv)
        
    def removeListener(self, tv: Tv):
        self.__observers.remove(tv)
        
    def aumentar_volume(self):
        for tv in self.__observers:
            tv.aumentar_volume()
            
    def diminuir_volume(self):
        for tv in self.__observers:
            tv.diminuir_volume()
            
    def mudar_canal(self, canal):
        for tv in self.__observers:
            tv.mudar_canal(canal)
    
    def __str__(self):
        return f"Observers: {[i.__str__() for i in self.__observers]}"
            
    def run(self):
        while True:
            print(self)
            print('1 - Aumentar volume')
            print('2 - Diminuir volume')
            print('3 - Aumentar canal')
            print('4 - Diminuir canal')
            print('5 - Mudar canal')
            print('6 - Sair')
            op = int(input('Opção: '))
            
            if op == 1:
                self.aumentar_volume()
            elif op == 2:
                self.diminuir_volume()
            elif op == 3:
                self.aumentar_canal()
            elif op == 4:
                self.diminuir_canal()
            elif op == 5:
                canal = int(input('Canal: '))
                self.mudar_canal(canal)
            elif op == 6:
                break
            else:
                print('Opção inválida')
                
            print(self.__observers)
            
if __name__ == '__main__':
    
    tv1 = Tv(1, 0)
    tv2 = Tv(2, 2)
    tv3 = Tv(3, 1)
    
    controle = Controle()
    controle.addListener(tv1)
    controle.addListener(tv2)
    controle.addListener(tv3)
    
    controle.run()
    