def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

while True:
    
    n = int(input("digite um numero: "))
    if(n > 1):
        print(factorial(n))
    else:
        break
    