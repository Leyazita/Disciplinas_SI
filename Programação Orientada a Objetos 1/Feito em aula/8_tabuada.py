m = int(input("montar a tabuada de: "))
c = int(input("começar por: "))
t = int(input("terminar em: "))


for x in range(c, t+1):
    print(m, "x", x, "=", m*x)