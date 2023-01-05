"""Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

Exeplo: Digite um número: 6.127
O número 6.127 tem a parte inteira = 6."""

print('*** Início do programa ***\n')
num = float(input('Digite um número: '))
from math import trunc
print('A parte inteira do número {} é: {}'.format(num, trunc(num)))
print('\n*** Fim do programa ***')
