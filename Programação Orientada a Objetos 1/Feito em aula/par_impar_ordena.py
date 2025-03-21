par = []
impar = []
num = 0
zero = []
numeros = []

'''while num >= 0:
    num = int(input('Digite um número ou um numero menor que 0 para sair: '))
    if num < 0:
        break
    if num == 0:
        zero.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)'''
        
while True:
    if num < 0:
        break
    else:
        numeros.append(num)
        
par += filter(lambda x: x % 2 == 0, numeros)
impar += filter(lambda x: x % 2 != 0, numeros)
zero += filter(lambda x: x == 0, numeros)
    
par.sort()
impar.sort()

resultado = par + zero + impar

print(resultado)