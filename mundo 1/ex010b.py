""" Programa mostra uma forma diferente de resolver o ex010 com algumas melhorias implementadas

Crie um programa que leia quanto em dinheiro uma pessoa tem na carteira e mostre quantos
dólares / euros / libras / Iene ela pode comprar.
Considere a seguinte cotação:

Dolar 1,00 == R$4,62
Euro 1,00 == R5,01
Libra 1,00 == 6,02
Ienes 1,00 == 0,036 """

print('Inicio do programa!!!\n')

reais = float(input('Digite quantos reais tem em sua carteira: '))

print('\nCom esses R${} você pode adquirir:'.format(reais))
print('_'*25)
print('US$ {:.2f} / Dolares'.format(reais / 4.62))
print('€ {:.2f} / Euros'.format(reais / 5.01))
print('£ {:.2f} / Libras'.format(reais / 6.02))
print('Y {:.2f} / Ienes'.format(reais / 0.036))
print('_'*25)

print('\nFim do programa!!!')
