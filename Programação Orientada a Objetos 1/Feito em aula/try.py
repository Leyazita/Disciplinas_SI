def dobrar(x):
    return x*2


a = "2"

#b = float(input("Digite outro valor: "))

try:
    assert isinstance(a, int), "O valor deve ser um número inteiro"
except AssertionError:
    a = int(a)
    
print(dobrar(a))