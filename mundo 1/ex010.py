""""Crie um programa que leia quanto em dinheiro uma pessoa tem na carteira e mostre
quantos dólares ela pode comprar.
Considere a seguinte cotação:

Dolar 1,00 == R$4,62 """

print('Inicio do progrma!!!\n')

real = float(input('Digite qual o valor você possui em sua carteira: R$'))

dolar = real/4.62

print('Com esses R${:.2f} voce pode adquirir até US${:.2f}'.format(real, dolar))

print('\nFim do progrma!!!')
