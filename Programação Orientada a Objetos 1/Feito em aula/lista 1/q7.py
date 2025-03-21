def decimal_binario(n):
    if n > 1:
        decimal_binario(n//2) #divide o numero e arredonda para baixo
    print(n % 2, end = '' )
    
n = int(input("Digite um número: "))
decimal_binario(n)
print("\n")