"""
Programa para resolver o ex012 de uma maneira diferente
Faça um algoritmo que leia o preço de um produto e mostre o seu novo valor com 5% de desconto.
"""

print('Inicio do programa!!!\n')

preco = float(input('Informe o preço do produto R$:'))

preco = preco - (preco * 0.05)

print('\nO nova preço do produto com 5% de desconto é R$:{:.2f}'.format(preco))

print('\nFim do progrma!!!')
