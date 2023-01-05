""" Programa resolve o exercício ex013 de uma forma diferente

Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário com um aumento de 15%"""

print('Inicio do programa!!!\n')

salario = float(input('Informe o valor do seu salário R$:'))

salario = salario + (salario * 0.15)

print('Você ganhou um aumento de 15% e o seu novo salário é R$:{:.2f}'.format(salario))

print('\nFim do programa!!!')
