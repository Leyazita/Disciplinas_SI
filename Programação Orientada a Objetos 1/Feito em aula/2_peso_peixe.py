peso = float(input('Digite o peso do peixe: '))

if peso <= 50:
    print('Peso esta dentro do estabelecido.')
elif peso > 50:
	excesso = peso - 50
	multa = excesso * 4
	print('O peso do peixe: %.2f Kg\nPeso em excesso: %.2f Kg\nMulta: R$ %.2f'%(peso, excesso, multa))
	