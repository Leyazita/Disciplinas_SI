import functools as reduce

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def isPar(num):
    return num % 2 == 0

def soma(a, b):
    return a + b

reduce(soma, filter(isPar, lista))




