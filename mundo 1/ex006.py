# Crie um program que leia um número e mostre o seu dobro, triplo e sua raiz quadrada.

print('Início do programa!!!\n')

N = int(input('Digite um número: '))

D = N * 2
T = N * 3
R = N ** 0.5

print('\nO número digitado foi: {}'.format(N))

print('\nO dobro de {} é: {}'.format(N, D))

print('\nO triplo de {} é: {}'.format(N, T))

print('\nA raiz quadrade de {} é: {:.2f}' .format(N, R))

print('\nFim do programa!!!')
