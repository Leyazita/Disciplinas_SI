print('Quanto voce ganha por hora trabalhada?')

money = float(input())

print('Quantas horas voce trabalhou no mes?')

time = int(input())

salario = money * time

IR = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
salario_liq = salario - IR - inss - sindicato

print('Salario bruto: R$ %.2f'%(salario))
print('IR: R$ %.2f'%(IR))
print('INSS: R$ %.2f'%(inss))
print('Sindicato: R$ %.2f'%(sindicato))
print('Salario liquido: R$ %.2f'%(salario_liq))
