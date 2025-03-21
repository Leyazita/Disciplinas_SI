def calcPreço(litros, tipo):
    if(tipo == 'A'):
        if(litros <= 20):
            return litros * 3.45 * 0.97
        else:
            return litros * 3.45 * 0.95
    elif(tipo == 'G'):
        if(litros <= 20):
            return litros * 4.53 * 0.96
        else:
            return litros * 4.53 * 0.94
        
def segundoDesconto(preço, litros, tipo):
    if(tipo == 'A'):
        if(litros > 20):
            return preço - ((litros - 20) * 0.04)
        else:
            return preço
    elif(tipo == 'G'):
        if(litros > 20):
            return preço - ((litros - 20) * 0.06)
        else:
            return preço
        
litros = int(input('Quantos litros?'))
tipo = input('Tipo de combustivel?')

print('Preco: R$ %.2f'%(segundoDesconto(calcPreço(litros, tipo), litros, tipo)))