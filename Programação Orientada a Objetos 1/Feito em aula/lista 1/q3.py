def quadrado(lado):
    return lado * lado

def circulo(raio):
    return raio * raio * 3.14

def triangulo(base, altura):
    return base * altura / 2

forma = input("Informe a forma ou 'sair' para parar: ")
              
while True:
    if forma == 'sair':
        break
   
    else:
        if forma == 'quadrado':
           lado = float(input("Informe o lado: "))
           print(quadrado(lado))
           forma = input("Informe a forma ou 'sair' para parar: ")
          
        elif forma == 'circulo':
            raio = float(input("Informe o raio: "))
            print(circulo(raio))
            forma = input("Informe a forma ou 'sair' para parar: ")
            
        elif forma == 'triangulo':
            base = float(input("Informe a base: "))
            altura = float(input("Informe a altura: "))
            print(triangulo(base, altura))
            forma = input("Informe a forma ou 'sair' para parar: ")
    
       

    