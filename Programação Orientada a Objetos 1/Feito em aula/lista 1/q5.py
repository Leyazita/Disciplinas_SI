def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
    
def arranjo(n, p):
    return fatorial(n) / fatorial(n-p)

def combinacao(n, p):
    return fatorial(n) / (fatorial(p) * fatorial(n-p))
    
n = int(input("Digite um número: "))
p = int(input("Digite como vai agrupar: "))

print("Arranjo: ", arranjo(n, p))
print("Combinação: ", combinacao(n, p))