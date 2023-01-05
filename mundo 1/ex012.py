"""Faça um algoritmo que leia o preço de um produto e mostre o seu novo valor com 5% de desconto."""

print('Inicio do programa!!!\n')

preco = float(input('Informe o valor do produto R$:'))

print('O novo valor desse produto já com 5% de desconto é R$:{:.2f}'.format(preco-(preco*0.05)))

print('\nFim do programa')
