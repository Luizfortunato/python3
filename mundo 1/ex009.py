"""Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada."""

print(' Início do programa!!!\n')

N = int(input('Digite o número que deseja saber a sua tabuada: '))

print('\nSegue a tabuada do {}:'.format(N))

print('_' * 15)
print(' ')
print(' {} x {:2} = {}'.format(N, 0, N * 0))                # {:2} deixa todos os caracteres com 2 casas
print(' {} x {:2} = {}'.format(N, 1, N * 1))
print(' {} x {:2} = {}'.format(N, 2, N * 2))
print(' {} x {:2} = {}'.format(N, 3, N * 3))
print(' {} x {:2} = {}'.format(N, 4, N * 4))
print(' {} x {:2} = {}'.format(N, 5, N * 5))
print(' {} x {:2} = {}'.format(N, 6, N * 6))
print(' {} x {:2} = {}'.format(N, 7, N * 7))
print(' {} x {:2} = {}'.format(N, 8, N * 8))
print(' {} x {:2} = {}'.format(N, 9, N * 9))
print(' {} x {:2} = {}'.format(N, 10, N * 10))

print('_' * 15)

print('\nFim do programa')
