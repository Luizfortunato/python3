# Crie um program que leia um número e mostre o seu dobro, triplo e sua raiz quadrada.
# Esse programa é uma forma diferente de se resolver o exercício ex006

print('Inicio do programa!!!\n')

N = int(input('Digite um número: '))

print('\nO número digitado foi: {}'.format(N))

print('\nO dobro de {} é: {}'.format(N, N*2))

print('\nO triplo de {} é: {}'.format(N, N*3))

print('\nA raiz quadrada de {} é: {:.2f}'.format(N, N**0.5))

print('\nFim do programa!!!')
