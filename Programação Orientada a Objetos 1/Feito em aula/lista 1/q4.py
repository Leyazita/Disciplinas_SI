def fatorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * fatorial_recursivo(n-1)
    
def fatorial_iterativo(n):
    fatorial = 1
    for i in range(1, n+1):
        fatorial *= i
    return fatorial

numero = int(input("Digite um número: "))

print("Fatorial recursivo: ", fatorial_recursivo(numero))
print("Fatorial iterativo: ", fatorial_iterativo(numero))
