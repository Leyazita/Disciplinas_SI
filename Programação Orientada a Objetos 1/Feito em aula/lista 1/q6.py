def primo(n):
    if n == 1 or n < 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
n = int(input("Digite um número: "))
m = int(input("Digite outro número: "))

if n < 1 and m < 1:
        print("Nao existe nenhum numero primo dentro desse intervalo")

for i in range(n, m+1):
    if primo(i):
        print(i)
    elif primo == False: 
        continue
    

            
   