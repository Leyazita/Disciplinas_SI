precos = [5, 4.50, 4, 3.50, 3, 2.50, 2, 1.50] # Preço dos ingressos
qtd = [120, 146, 172, 198, 224, 250, 276, 302] # Quantidade de ingressos vendidos

def maiorLucro(precos, qtd): # Função que retorna o maior lucro
    lucro = 0
    for i in range(0, 8):
        valor = (precos[i] * qtd[i])
        if valor > lucro:
            lucro = valor
    return lucro

def PreçoMaiorLucro(precos, qtd): # Função que retorna o preço do ingresso que gera o maior lucro
    lucro = 0
    for i in range(0, 8):
        valor = precos[i] * qtd[i]
        if valor > lucro:
            lucro = valor
            preco = precos[i]
    return preco

for i in range(0, 8): # Imprime a tabela com o preço, ingresso e lucro
    valor = precos[i] * qtd[i]
    lucro = (precos[i] * qtd[i]) - 200
    print("Preço ingresso = %.2f, quantidade = %d, lucro = %.2f" %((precos[i]), qtd[i], lucro))
    
print("Lucro maximo = %.2f" %(maiorLucro(precos, qtd) - 200)) #preço menos o custo do espetáculo
print("Preço do ingresso = %.2f" %(PreçoMaiorLucro(precos, qtd)))
print("Quantidade vendida = %d" %(maiorLucro(precos, qtd)/PreçoMaiorLucro(precos, qtd))) 
#Quantidade vendida = lucro/Preço