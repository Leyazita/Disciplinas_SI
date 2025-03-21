def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

while True:
    
    n = int(input("digite um numero: "))
    if(n > 1):
        print(fibonacci(n))
    else:
        break