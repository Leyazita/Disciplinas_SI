'''
completo = '{a}, {b}, {c:0.2f}, '
completo = completo.format(a = 'Leya', b = 'Barbosa', c = 3.14556)

completo = completo + '{:0.2f}'.format(3.14556)

print(completo)
 --------------------------------------------------
a = input('Digite algo: ')
a = a.split(' ')

print(a)
--------------------------------------------------

lista = ['a', 'b', 'c' ,'v' , 'n', 'm', 'i', 'p']
lista.insert(3, 'q')
lista.sort()
lista.index()

print(lista)
'''
par = []
impar = []
zero = []
num = []

while num >= 0:
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        par.append(num)   
    if num % 2 != 0:
        impar.append(num)
    if num == 0:
        zero.append(num)